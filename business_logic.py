import logging
import sqlite3

from polars import read_excel, ColumnNotFoundError , col , read_database_uri
from polars.datatypes import Utf8 , Int64 

from datetime import datetime
import json
import os

# setting up base for logging level
logging.basicConfig(level=logging.INFO)
the_logs = logging.getLogger(__name__)


class StokOpname_logs :
    def __init__(self):
        self.path = './stok_opname_logs.json'

        # back-up init simple db
        self.initdata = {}

        # check path
        if not os.path.exists(self.path):
            with open(self.path , 'w') as db :
                json.dump(self.initdata , db , indent=4)

        # read simple db
        with open(self.path , 'r') as so :
            self.logs:dict[str,list[str]] = json.load(so)
    
    def logger(self ,product_name:str , record:str )-> dict[str,list[str]]:

        if product_name not in self.logs.keys():
            self.logs[product_name] = [record]

        else :
            self.logs[product_name].append(record)

        with open (self.path , 'w') as writer :
            json.dump(self.logs ,writer , indent=4)

        return self.logs
    
class DBManager:
    def __init__(self , sku_path:str=None):
        self.sqlite_path = './stok_opname.db'
        self.init_db()
        absolute_path = os.path.abspath(self.sqlite_path)
        self.connection_uri = f"sqlite:///{absolute_path}"
        self.sku_path = sku_path if not None else []

        self.log_progress = StokOpname_logs()


    def init_db(self):
        with sqlite3.connect(self.sqlite_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS stok_opname (
                    sku_code VARCHAR(9) PRIMARY KEY,
                    current INTEGER DEFAULT 0,
                    so_1 INTEGER DEFAULT 0,
                    so_2 INTEGER DEFAULT 0,
                    location TEXT NULLABLE,
                    update_at TIMESTAMP DEFAULT (datetime('now', 'localtime'))
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS so_logs (
                        create_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
                        sku_code VARCHAR(9),
                        activity TEXT
                )
            """)
            conn.commit()

    def commit(self , query , param):
        with sqlite3.connect(self.sqlite_path) as reader:
            reader.execute(query, param)
            reader.commit()
            
    def fetchs (self , query , params , one:bool = False)-> list[tuple]|tuple:
        with sqlite3.connect(self.sqlite_path) as reader:
            curr = reader.cursor()
            c_result = curr.execute(query, params)
            return c_result.fetchone() if one else c_result.fetchall()
        
    def insert_basic(self):
        if self.sku_path != []:
            try:
                sku = read_excel(self.sku_path , schema_overrides={'SKU':Utf8})
            except :
                return 'need to have SKU column name on ur data maybe it named differently make sure the data consist of 2 column 1st SKU and 2nd is for column contain qty of it'
            
            sku = sku.with_columns(col(sku.columns[-1]).cast(Int64)).rename({sku.columns[-1]:'Qty'})
            params = list(sku.iter_rows())

        else : 
            sku = []
        query = 'INSERT INTO stok_opname(sku_code , current) VALUES (? , ?)'
        self.commit(query , params)

    def handle_kolian(self , ):

        return

    def show_current(self , params=None):
        query = """SELECT * 
        FROM stok_opname ; """
        return self.fetchs(query= query , params=params)

    def export_all(self , name):
        query = """
        SELECT 
            sku_code as 'SKU'  , 
            so_2 as 'Quantity' 
        FROM stok_opname ;
        """
        result = read_database_uri(query, self.connection_uri)
        result.write_excel(f'./result-{name}.xlsx')
    

    def remove_data(self):

        with sqlite3.connect(self.sqlite_path) as cnc :
            cnc.execute('DELETE FROM stok_opname')
            cnc.commit()

    def remove_spesific (self , sku):

        with sqlite3.connect(self.sqlite_path) as cnc :
            cnc.execute('DELETE FROM stok_opname WHERE sku_code = ?' , (sku,))
            cnc.commit()

    def modify_add_quantity(self , column , params):
        column = ''
        query = f"""
                UPDATE stok_opname
                SET
                    {column} = {column} + ?
                    update_at = (datetime('now', 'localtime'))
                    WHERE sku_code = ? ;
                """
        self.commit(query ,params)
        
    def inserting_main_data(self ,types:str , params:tuple[any]):
        '''### the length param should be 3 consist of sku , qty , and its location'''
        
        if not isinstance (params , tuple[any]) & len(params) != 3:

            record = f'{times} - FAILED - Does not meet value criteria'
            self.log_progress.logger( types , record)
            return

        query = f'''INSERT INTO stok_opname (sku_code , {'so_1' if 'SO1' in types else 'so_2'} , location) VALUES ( ?, ?, ? );'''

        theact = f'ADD {params[1]} Locate {params[-1]}'
        query2 = f'''INSERT INTO so_logs ( sku_code , activity ) VALUES (  ?, ? );'''

        with sqlite3.connect(self.sqlite_path) as conn :
            executor = conn.cursor()
            executor.execute(query , (params))
            executor.execute(query2 , (params[0],theact))
            conn.commit()
        
        skuu = params[0]
        query_timee = f"SELECT update_at FROM stok_opname WHERE sku_code = {skuu}"

        with sqlite3.connect(self.sqlite_path) as conn :
            executor = conn.cursor()
            times = executor.execute(query_timee , (skuu,)).fetchone()[0]

        record = f'{times} - SUCCEED - Updating {skuu} -> {params[1]}'
        self.log_progress.logger(skuu , record)

        self.validate_stockOpname(skuu)
        return f"Succesfully updating data of {skuu} @ {times}"

    def updating_main_data(self , column:str , params:tuple[any])-> None:
        '''### the length param should be 2 consist of new value , and its sku
        
        *the **column** param are the column to be set*'''

        if isinstance (params , str):
            params = (params,)

        if len(params) == 1:
            raise ValueError( " u might be missing parameter to set it might be the value or the filter data at least have a len of 2 which first is for the replace value and one other is for filter")

        query = f'''UPDATE stok_opname 
        SET {column} = ? 
        update_at = (datetime('now', 'localtime'))
        WHERE sku_code = ? ; '''

        theact = f'UPDATE QTY {params[0]} FOR {params[-1]}'
        query2 = f'''INSERT INTO so_logs ( sku_code , activity ) VALUES (  ?, ? );'''

        with sqlite3.connect(self.sqlite_path) as conn :
            executor = conn.cursor()
            executor.execute(query , (params))
            executor.execute(query2 , (params[-1],theact))
            conn.commit()

        self.validate_stockOpname(params[-1])
        return None

    def show_selisih(self)-> dict:
        '''## the result from this method is ready-able to be transform into a pandas dataframe'''

        query = f"""SELECT so.sku_code , abs(so.so_1 - so.so_2) AS selisih , so.location 
                    FROM stok_opname so
                    WHERE so.so_1 <> so.so_2"""
        
        with sqlite3.connect(self.sqlite_path) as conn :
            exc = conn.cursor()
            data_selisih = exc.execute(query).fetchall()

        new_data = {'SKU':[] , 'Selisih':[] , 'Location':[]}
        for data in data_selisih:
            new_data['SKU'].append(data[0])
            new_data['Selisih'].append(data[1])
            new_data['Location'].append(data[2])

        return new_data

    def track_selisih (self , nama_sku) -> dict:
        '''## the result from this method is ready-able to be transform into a pandas dataframe'''

        query = f" SELECT create_at , activity FROM so_logs WHERE sku_code = ? ;"
        with sqlite3.connect(self.sqlite_path) as conn :
            exc = conn.cursor()
            tracker = exc.execute(query , (nama_sku,)).fetchall()

            new_data = {'create_at':[] , 'activity':[] }
            for data in tracker:
                new_data['create_at'].append(data[0])
                new_data['activity'].append(data[1])
        
        return new_data

    def validate_stockOpname(self , produk:str):

        if not isinstance(produk , str):
            self.log_progress.logger(product_name=produk , record= f'{datetime.now().timestamp()} - FAILED - Product Not Found' )
            print( f'sorry there is no such this as {produk} on our list')
            raise ValueError('sorry data misstyped')
        
        query = "SELECT current , so_1 , so_2 , location FROM stok_opname WHERE sku_code = ?"

        with sqlite3.connect('./App3/StokOpname.db') as conn :
            executor = conn.cursor()
            result = executor.execute( query , (produk,)).fetchone()

        awal = result[0]
        pertama = result[1]
        kedua = result[2]
        locations = result[-1]

        if pertama == 0:
            print( "can't  do validate data bcs we don't have other data to compare")
            raise  ValueError('sorry')
        
        if awal != pertama:
            msg = f"{datetime.now().timestamp()} - SELISIH - stok-awal = {awal} | 1st SO = {pertama}"
            self.log_progress.logger(produk , record= msg )
            print(f"sorry both aren't have same or equal value which on 1st SO having {pertama} and current stok arent that way")
            raise ValueError('sorry difference exist')

        if  kedua == 0 :
            print( "can't  do validate data bcs we don't have other data to compare")
            raise ValueError('sorry')

        if pertama != kedua :
            msg = f"{datetime.now().timestamp()} - SELISIH - 1st SO = {pertama} | 2nd SO = {kedua} ||| Re-check on {locations}"
            self.log_progress.logger(produk , record= msg )
            print( f"sorry both aren't have same or equal value which on 1st SO having {pertama} while 2nd SO having {kedua}, u can recheck on {locations}")
            raise ValueError('sorry difference exist')

        return f"Cleared for {produk}"


class SystemMain():
    def __init__(self , path:str=None):
        super().__init__()

        self.sku =self.read_sku(path)
        self.logs = StokOpname_logs()
        self.sqlite_db = DBManager()


    def read_sku(self, path : str):
        if path != None:
            try:
                data_sku = read_excel(path, schema_overrides={'SKU': Utf8})
                self.valid_sku = sorted(data_sku['SKU'].unique().to_list())
            except ColumnNotFoundError:
                the_logs.error("Excel data must have an uppercase 'SKU' column")
                self.valid_sku = []

        else :
            self.valid_sku : list[str]= ['']
        

    def add_data (self , sku , types , location , number , another=0 ):
            
        # check and set logger
        if sku not in set(self.valid_sku):
            self.logs.logger(sku , record= f"{datetime.now().timestamp()} -FAILED- SKU NOT FOUND")


        the_params = (sku , number+another , location)
        self.sqlite_db.inserting_main_data(types=types , params=the_params)

        return self
    
    def update_data (self , sku , types , number , another=0 ):
            
        # check and set logger
        if sku not in set(self.valid_sku):
            self.logs.logger(sku , record= f"{datetime.now().timestamp()} -FAILED- SKU NOT FOUND")


        the_params = ( number+another , sku)
        types_col = 'so_1' if types == 'SO1' else 'so_2'
        self.sqlite_db.updating_main_data(types=types_col , params=the_params)

        return self

    def show_logs(self):
        return print(self.logs)

def main():
    system = SystemMain()

    while True:
        try:
            produk = input('SKU : ')
            tipes:str = input('select ["SO1","SO2"] : ').upper()
            jumlah = int(input('amount : '))
            additi = int(input('add : '))
            location = input('location ["LT1","LT2","LT3","GUDANG1","GUDANG2"]: ').upper()
            try:
                system.add_data(produk , tipes , location , jumlah , additi)
            except :
                continue
        except InterruptedError:
            system.show_logs()  

if __name__ == '__main__':
    main()
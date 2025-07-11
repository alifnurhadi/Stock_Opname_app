# from tkinter import *
# Explicit imports to satisfy Flake8
import os
from pathlib import Path
import random
from tkinter import Frame, Label, Listbox, StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, Toplevel, filedialog , messagebox
from tkinter.ttk import Combobox, OptionMenu, Style
from typing import Any, Dict
from PIL import ImageTk
from business_logic import *
import polars as pl
from rapidfuzz import fuzz , process
from pandastable import Table
import numexpr
numexpr.set_num_threads(4)

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\MARKETING SUPPORT\Documents\asteros\astrs_work\special_\result\app_so\build\assets\frame0")
session_combobox = None

def relative_to_assets(path: str) -> Path:
    return os.path.join(os.path.dirname(__file__), "assets", path)

def readloc():
    try:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        # Construct the full path to locations.txt
        file_path = os.path.join(script_dir, 'locations.txt')
        with open(file_path, 'r') as reader:
            location = reader.read().strip()
            if not location:
                return "locations.txt is empty"
        split_loc = location.split(',')
        locations_display = '\n'.join([loc.strip() for loc in split_loc if loc != ' '])
        return locations_display if locations_display else "No valid locations found"
    except FileNotFoundError:
        return "locations.txt not found in current directory"
    except Exception as e:
        return f"Error reading locations.txt: {str(e)}"
    


# def main_UI():
window = Tk()

window.geometry("901x582")
window.configure(bg = "#CDCDCA")

canvas = Canvas(window, bg="#CDCDCA", height=582, width=901, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)


# separator
canvas.create_rectangle(28.99999976134464, 130.0, 30.00000762939453, 311.0, fill="#000000", outline="")
canvas.create_rectangle(149.00000739073917, 130.0, 150.00001525878906, 311.0, fill="#000000", outline="")
canvas.create_rectangle(349.9999921319501, 130.0, 351.0, 311.0, fill="#000000", outline="")
canvas.create_rectangle(490.9999921319501, 130.0, 492.0, 311.0, fill="#000000", outline="")
canvas.create_rectangle(560.0, 190.0, 839.0, 309.0, fill="#D9D9D9", outline="")

# texto
canvas.create_text(40.0, 43.0, anchor="nw", text="Upload file", fill="#000000", font=("Inter Bold", -12))
canvas.create_text(65.00000762939453, 127.0, anchor="nw", text="SESSION", fill="#000000", font=("Inter Bold", -12))
canvas.create_text(32.0, 324.0, anchor="nw", text="Keterangan :", fill="#000000", font=("Inter Bold", -12))
canvas.create_text(217.00001525878906, 127.0, anchor="nw", text="LOCATION", fill="#000000", font=("Inter Bold", -12))
canvas.create_text(372.0, 127.0, anchor="nw", text="SKU :", fill="#000000", font=("Inter Bold", -12))
canvas.create_text(372.0, 188.0, anchor="nw", text="Quantity :", fill="#000000", font=("Inter Bold", -12))
# canvas.create_text(372.0, 258.0, anchor="nw", text="Qty tambahan :", fill="#000000", font=("Inter Bold", -10))
canvas.create_text(271.0, 329.0, anchor="nw", text="Koli:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(391.0, 329.0, anchor="nw", text="Koli:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(327.0, 329.0, anchor="nw", text="isi:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(447.0, 329.0, anchor="nw", text="isi:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(570.0, 131.0, anchor="nw", text="tulis perhitungan :", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(23.0, 465.0, anchor="nw", text="Voila :", fill="#000000", font=("Inter Bold", -10))
canvas.create_text(159.0, 276.0, anchor="nw", text="*make sure that u place / write location \nwhere it already set at ( show valid loc )\nto prevent any future error.", fill="#FF0000", font=("Inter", -10))
quotes = canvas.create_text(561.0, 191.0, anchor="nw", text="RANDOM QUOTES", fill="#000000", font=("Inter Bold", -24), width=250)
canvas.create_text(795.9999718563797, 152.0, anchor="nw", text=":)", fill="#FFFFFF", font=("Inter Bold", -20))   


def generate_fun():
    global quotes
    canvas.delete(quotes)
    randomtext = ['keep smule' , 'jangan semangat tetaplah sedih','random quotes']
    canvas.itemconfig(quotes, text=random.choice(randomtext))
    quotes =canvas.create_text(561.0, 191.0, anchor="nw", text=random.choice(randomtext), fill="#000000", font=("Inter Bold", -24) , width=300)

# image obj
entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_4 = canvas.create_image(291.0, 359.5, image=entry_image_4)
entry_bg_5 = canvas.create_image(411.0, 359.5, image=entry_image_5)
entry_bg_10 = canvas.create_image(345.0, 359.5, image=entry_image_10)
entry_bg_11 = canvas.create_image(465.0, 359.5, image=entry_image_11)
entry_bg_2 = canvas.create_image(421.5, 223.5, image=entry_image_2)
entry_bg_3 = canvas.create_image(421.5, 291.5, image=entry_image_3) ## this will be replaced by a button
entry_bg_9 = canvas.create_image(250.5, 181.5, image=entry_image_9)
entry_bg_6 = canvas.create_image(204.0, 82.5, image=entry_image_6)
entry_bg_7 = canvas.create_image(129.0, 359.5, image=entry_image_7)
entry_bg_8 = canvas.create_image(258.5, 520.5, image=entry_image_8)
entry_bg_1 = canvas.create_image(421.5, 162.5, image=entry_image_1)


entry_location = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_location.place(x=179.0, y=164.0, width=143.0, height=33.0)
entry_upload = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_upload.place(x=36.0, y=65.0, width=336.0, height=33.0)
entry_keterangan = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_keterangan.place(x=32.0, y=342.0, width=194.0, height=33.0)
entry_result = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_result.place(x=25.0, y=481.0, width=467.0, height=77.0)
entry_sku = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_sku.place(x=372.0, y=145.0, width=99.0, height=33.0)


entry_qty = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_qty.place(x=372.0, y=206.0, width=99.0, height=33.0)
entry_qty_tambahan = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_qty_tambahan.place(x=372.0, y=274.0, width=99.0, height=33.0)
entry_koli1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_koli1.place(x=269.0, y=342.0, width=44.0, height=33.0)
entry_koli2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_koli2.place(x=389.0, y=342.0, width=44.0, height=33.0)
entry_isi1 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_isi1.place(x=323.0, y=342.0, width=44.0, height=33.0)
entry_isi2 = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_isi2.place(x=443.0, y=342.0, width=44.0, height=33.0)
entry_koli1.insert(0,'0')
entry_koli2.insert(0,'0')
entry_isi1.insert(0,'0')
entry_isi2.insert(0,'0')
entry_qty.insert(0,'0')
entry_qty_tambahan.insert(0,'0')


entry_image_12 = PhotoImage(file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(670.0, 162.5, image=entry_image_12)
entry_calculator = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_calculator.place(x=570.0, y=145.0, width=200.0, height=33.0)


def on_session_select(event ,combobox):
    selected = default_value.get()
    combobox.configure(values=[selected])
def reset_session(combobox):
    default_value.set("SO 2")
    combobox.configure(values=sessions)

# Global variables for Combobox
sessions = ["SO 1", "SO 2"]
default_value = StringVar(value="SO 2")

style = Style() 
style.configure( "warnaopsi.TCombobox", background="#f1f2e0", foreground="#000000", borderwidth=2, relief="flat" )
session_combobox = Combobox( canvas, textvariable=default_value, values=sessions, style="warnaopsi.TCombobox", state="readonly" )
session_combobox.place(x=50, y=200, width=80, height=30)
session_combobox.bind("<<ComboboxSelected>>", lambda event: on_session_select(event, session_combobox))
reset_button = Button( canvas, text="Reset Session", command= lambda : reset_session(session_combobox), bg="#D9D9D9", fg="#000716", relief="flat" )
reset_button.place(x=50, y=250, width=70, height=25 , anchor='nw')

logics = DBManager()

canvas.create_text(800.0, 96.0, anchor="nw", text="Maker : Ben", fill="#000000", font=("Inter", -12))
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(835.0, 69.0, image=image_image_1)

RECAP_ENTRIES : Dict[str,Any] = {
    'upload':entry_upload,
    'session':session_combobox,
    'location':entry_location,
    'sku':entry_sku,
    'qty':entry_qty,
    'qty_tambahan':entry_qty_tambahan,
    'keterangan':entry_keterangan,
    'isi1':entry_isi1,
    'isi2':entry_isi2,
    'koli1':entry_koli1,
    'koli2':entry_koli2,
    'calculate':entry_calculator
}

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_browse = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("Browse"), relief="flat")
button_browse.place(x=398.0, y=55.0, width=89.0, height=51.0)
button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_add = Button(image=button_image_3, borderwidth=0, highlightthickness=0, command=lambda: print("Add"), relief="flat")
button_add.place(x=28.0, y=393.0, width=140.0, height=38.0)
button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
button_subtract = Button(image=button_image_6, text="( - ) Reduce", compound="center", font=("Arial", 12, "bold"), fg="white", borderwidth=0, highlightthickness=0, command=lambda: print("reduce clicked"), relief="flat")
button_subtract.place(x=189.0, y=393.0, width=140.0, height=38.0)
button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_showall_selisih = Button(image=button_image_4, text="Show all selisih", compound="center", font=("Arial", 12, "bold"), fg="white", borderwidth=0, highlightthickness=0, command=lambda: print("Show all selisih"), relief="flat")
button_showall_selisih.place(x=540.0, y=503.0, width=140.0, height=38.0)
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_export = Button(image=button_image_5, borderwidth=0, highlightthickness=0, command=lambda: print("Export Out"), relief="flat")
button_export.place(x=721.0, y=502.0, width=140.0, height=38.0)
button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
button_showcurrent = Button(image=button_image_7, text="Show Current Data", compound="center", font=("Arial", 10, "bold"), fg="white", borderwidth=0, highlightthickness=0, command=lambda: print("show current data"), relief="flat")
button_showcurrent.place(x=350.0, y=393.0, width=140.0, height=38.0)
button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
button_track = Button(image=button_image_9, text="Track SKU", compound="center", font=("Arial", 12, "bold"), fg="white", borderwidth=0, highlightthickness=0, command=lambda: print("Track SKU"), relief="flat")
button_track.place(x=722.0, y=340.0, width=140.0, height=38.0)
button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
button_validloc = Button(image=button_image_12, font=("Arial", 8), fg="black", borderwidth=0, highlightthickness=0, command=lambda: print("valid location are :\n"), relief="flat")
button_validloc.place(x=200.0, y=240.0, width=100.0, height=26.0)
button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))
button_clear = Button(image=button_image_13, borderwidth=0, highlightthickness=0, command=lambda: print("clear button clicked"), relief="flat")
button_clear.place(x=438.0, y=449.0, width=46.0, height=23.0)
button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_calculating = Button(image=button_image_2, borderwidth=0, highlightthickness=0, command=lambda: print("now calculating"), relief="flat")
button_calculating.place(x=786.0, y=142.0, width=43.0, height=41.0)
button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
button_test3 = Button(image=button_image_8,borderwidth=0,highlightthickness=0,command=lambda: print(f"session {session_combobox.get()} ___ button_session clicked"),text='in-test 3!',compound='center',font=('Arial',12 , 'bold') , fg='white',relief="flat")
button_test3.place(x=722.0,y=442.0,width=140.0,height=38.0)
button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
button_test2 = Button(image=button_image_10,borderwidth=0,highlightthickness=0,command=lambda: print("button_10 clicked"),text='test->Validate',compound='center',font=('Arial',12 , 'bold') , fg='white',relief="flat")
button_test2.place(x=540.0,y=442.0,width=140.0,height=38.0)
button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
button_test1 = Button(image=button_image_11,borderwidth=0,highlightthickness=0,command=lambda: print('sss'),text='test->Insert basic',font=('Arial',12 , 'bold') , fg='white',compound='center',relief="flat")
button_test1.place(x=540.0,y=340.0,width=140.0,height=38.0)

def debug():
    data = [entry_sku , entry_qty , entry_qty_tambahan , entry_koli1 , 
            entry_koli2 , entry_upload , entry_keterangan , entry_result , 
            entry_location , entry_isi1 , entry_isi2 , entry_calculator]
    for i , d  in enumerate(data, start=1):
        print(f'{i} - {d.get()}')
        
def get_fullqty():
    hitungkolian1 = logics.handle_kolian( int(entry_koli1.get()) , int(entry_isi1.get()))
    hitungkolian2 = logics.handle_kolian( int(entry_koli2.get()) , int(entry_isi2.get()))
    fullqty:int = hitungkolian1 + hitungkolian2 + int(entry_qty.get()) + int(entry_qty_tambahan.get())
    return fullqty

def browse_file():
        filename = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
        )
        if filename:
            entry_upload.delete(0, 'end')
            entry_upload.insert(0, filename)


        init = messagebox.askquestion('Database',"Want to start over a database?")

        if init == "yes":
            dbpath = './stok_opname.db'

            if Path(dbpath).exists():
                os.remove(dbpath)

            logics.init_db()
            messagebox.showinfo('Success!'," older databases already deleted and replaced by new ones")
        else :
            messagebox.showinfo('Notice!',"ENJOYYY !!!")

def create_logs(action , recap_entry: Dict[str, Entry] = RECAP_ENTRIES)->str:
    ket = action
    sku = recap_entry["sku"].get()
    qty = recap_entry["qty"].get()
    qty_tambahan = recap_entry["qty_tambahan"].get()
    isi1 = recap_entry["isi1"].get()
    koli1 = recap_entry["koli1"].get()
    isi2 = recap_entry["isi2"].get()
    koli2 = recap_entry["koli2"].get()
    keterangan = recap_entry["keterangan"].get()
    session = recap_entry["session"].get()

    texts = ''
    
    texts = f"{datetime.now().strftime('%H:%M || "%d/%m')} - {ket}, {sku} - (main: {qty}, opt: {qty_tambahan}) - at {session}"

    if koli1 != '0':
        texts += f"\n - {koli1}@{isi1}"
    if koli2 != '0':
        texts += f"\n - & {koli2}@{isi2}"
    if keterangan :
        texts += f"\n- {keterangan or ''}"

    return texts

def simplecalculate():
    subtracting = []
    adding = []

    raw:str =entry_calculator.get()
    raw_iterate = raw.strip().split('+')

    for num in raw_iterate:
        raww2 = num.strip()
        if '-' in raww2:
            part = raww2.split('-',1)
            positif = part[0].strip()
            negatif = part[-1].strip()

            if 'x' in positif:
                mul1, mul2 = positif.split('x')
                positif = int(mul1.strip()) * int(mul2.strip())
                print(positif)
            adding.append(int(positif))

            if 'x' in negatif:
                mul1, mul2 = negatif.split('x')
                negatif = int(mul1.strip()) * int(mul2.strip())
                print(negatif)
            subtracting.append(int(negatif))

        elif 'x' in raww2 :
            mul1 , mul2 = raww2.split('x')
            mul1 = mul1.strip()
            mul2 = mul2.strip()
            sums = int(mul1)*int(mul2)
            print(sums)
            adding.append(sums)
        else:
            adding.append(int(raww2))
        print(f'add data{adding} , subtract {subtracting}')
        
    reslt = sum(adding) - sum(subtracting)

    entry_calculator.delete(0,'end')
    
    return messagebox.showinfo('Result' , f'hasil itungannya: \n {reslt} \n\n ')

def clear_all_entries():
    global RECAP_ENTRIES
    entries:dict[str,Any] = RECAP_ENTRIES
    clear = messagebox.askquestion('ANSWER','want to clear all?')
    if clear == 'yes':
        for k , v in entries.items():
            print(v.get())
            if k =='upload' or k == 'sku':
                continue
            elif k == 'session':
                reset_session(v)
            elif any(s in k for s in ('qty', 'koli', 'isi')):
                v.delete(0,'end')
                v.insert(0,'0')
            else:
                v.delete(0,'end')

def submitData():
    sku = entry_sku.get()
    session = session_combobox.get()
    location = entry_location.get()
    qty = get_fullqty()
    print(qty)
    addvalue = entry_qty_tambahan.get()
    if addvalue == None or addvalue == '0':
        messagebox.showwarning('Warning',"Make sure -- 'qty tambahan' -- are filled when want to add more value to the current one or it will lead to error result at the end")

    parame1 = (sku,qty,location)
    parame2 = (qty ,location, sku)

    logs = create_logs('tambah')

    try:
        logics.inserting_main_data(session , parame1)
        logics.insertLogs((sku,qty ,logs))
        clear_all_entries()
        
    except:
        messagebox.showinfo('WARNING' ,'There might already value there, might consider to update instead of add')
        updatevalue = messagebox.askquestion('Next Move',f'if "yes" it will update its value and reset older {session} data?')
        if updatevalue == 'no':
            adddingdata = messagebox.askquestion('Other Move', 'want to add more to the current one?')
            if adddingdata == 'yes':
                logics.modify_add_quantity(session,(addvalue,sku))
                logics.insertLogs((sku,qty ,logs))
                clear_all_entries()
                
        else :
            logics.updating_main_data(session , parame2)
            logics.insertLogs((sku,qty ,logs))
            clear_all_entries()

def validate():

    thesku = entry_sku.get()
    result = logics.validate_stockOpname(thesku)

    if "ERROR" in result.keys():
        messagebox.showwarning("ERROR",result['ERROR'])
    elif "SUCCEED" in result.keys():
        messagebox.showinfo('SUCCEED',result['SUCCEED'])

def subtract_it(): 
    global RECAP_ENTRIES
    addvalue = entry_qty_tambahan.get()
    if addvalue == None or addvalue == '0':
        messagebox.showwarning('Warning',"Make sure -- 'qty tambahan' -- are filled when want to add more value to the current one or it will lead to error result at the end")
    param = (addvalue , RECAP_ENTRIES['sku'].get())
    logs = create_logs('kurang')
    param2 = (RECAP_ENTRIES['sku'].get() , addvalue , logs)
    logics.modify_subtract_quantity(RECAP_ENTRIES['session'].get(), param)
    logics.insertLogs(param2)

    messagebox.showinfo('Logs :',f"u've just subtracting data from {RECAP_ENTRIES['sku'].get()} about {addvalue}")


def testingbutton():
    global entry_result
    respon = messagebox.askquestion('Are u sure ?','want to see the logs?')
    userwanttosee = f'ur logs : {create_logs('tambah')}'
    print(userwanttosee)
    if respon:
        entry_result.insert(0,f'ur logs : {create_logs('tambah')}')

suggestion_list = Listbox(window, height=5, width=2, font=("Arial", 10))
suggestion_list.place(x=372.0, y=178.0, width=99.0)
suggestion_list_visible = False

def hide_suggestions():
    global suggestion_list_visible 
    suggestion_list_visible = False
    suggestion_list.place_forget()
 

status_label = Label(window, text="Status: Ready", font=("Arial", 10), bg="#CDCDCA")
status_label.place(x=555, y=55)

def show_suggestions(sku:bool=True):
    if sku:
        global suggestion_list_visible
        suggestion_list_visible = True
        suggestion_list.place(x=372.0, y=178.0, width=99.0)

    
def select_suggestion(event):
    if suggestion_list.curselection():
        selected = suggestion_list.get(suggestion_list.curselection())
        entry_sku.delete(0, "end")
        entry_sku.insert(0, selected)
        hide_suggestions()
        status_label.config(text=f"Status: Selected {selected}")


def reads(use_entry:bool=True):
    if use_entry:
        fullpath = os.path.join(os.path.dirname(__file__),Path(entry_upload.get()).name)
        ss = pl.read_excel(fullpath , schema_overrides={'SKU':pl.Utf8})
        skuvalid = ss['SKU'].to_list()
    else:
        locs:str = readloc()
        return locs.split(sep='\n')
    return skuvalid

def update_suggestions(event , forloc:bool=False):

    if forloc:
        valid_data = reads(use_entry=False)
    else:
        valid_data = reads()

    query = entry_sku.get().strip()
    if len(query) < 2:  # Require at least 2 characters
        hide_suggestions()
        status_label.config(text="Status: Enter at least 2 characters")
        return

    # Fuzzy match
    matches = process.extract(query, valid_data , scorer=fuzz.partial_ratio, limit=5)
    suggestions = [match[0] for match in matches if match[1] > 70]  # Threshold: 70%

    suggestion_list.delete(0, "end")
    for suggestion in suggestions:
        suggestion_list.insert("end", suggestion)

    if suggestions:
        show_suggestions()
        status_label.config(text=f"Status: {len(suggestions)} suggestions")
    else:
        hide_suggestions()
        status_label.config(text="Status: No matches found")


hide_suggestions()
entry_sku.bind("<KeyRelease>", update_suggestions)
suggestion_list.bind("<<ListboxSelect>>", select_suggestion)



table = None
table_window = None

def create_table(parent_frame, dataframe):
    global table ,table_window
    table_window = Toplevel(parent_frame)
    table_window.title("Stock Opname Table")
    table_window.geometry("800x400")
    table_window.protocol("WM_DELETE_WINDOW", lambda: table_window.destroy())
    frame = Frame(table_window)
    frame.pack(fill="both", expand=True)
    table = Table(frame, dataframe=dataframe, showtoolbar=True, showstatusbar=True)
    table.show()
    return table

def show_all(sku:str=None):
    data = logics.show_current()
    sku = []
    current = []
    so_1 =  []
    so_2 = []
    locs = []
    for d in data:
        sku.append(d[0])
        current.append(d[1])
        so_1.append(d[2])
        so_2.append(d[3])
        locs.append(d[4])
    
    df = pl.DataFrame({
        'SKU':sku,
        'Current':current,
        'SO 1':so_1,
        'SO 2':so_2,
        'Location':locs,
    })

    if sku != None:
        df = df.filter(pl.col('SKU')==sku)

    pddf =df.to_pandas()

    if table_window is not None:
        table_window.destroy()

    tablewindow = create_table(window , pddf)
    
    return df

def showall_selisih():
    
    datas = logics.show_selisih()
    print(datas)

    polar = pl.DataFrame(datas)
    pandas = polar.to_pandas()

    if table_window is not None:
        table_window.destroy()

    table = create_table(window ,pandas)

    return

def trackselisih():

    sku = entry_sku.get()
    if sku == None or sku == '':
        messagebox.showwarning('Notice','u forgot to place the sku code , PLACE IT or u"ll get nothing.')
        return
    
    datas = logics.track_selisih(sku)
    print(datas)
    keys = list(datas.keys())
    
    datapl = pl.DataFrame(datas)

    pandas = datapl.to_pandas()

    if table_window is not None:
        table_window.destroy()

    table = create_table(window ,pandas)

    return


def insert_initdata():
    global entry_upload
    path = entry_upload.get()
    try:
        initdata = DBManager(sku_path=path)
        initdata.insert_basic()

    except:
        messagebox.showinfo('INFO','Processing.... \n backuping datas ....')

        export(backup=True)
        query = 'DELETE FROM stok_opname'
        logics.commit(query)
        initdata = DBManager(sku_path=path)
        initdata.insert_basic()



def export(backup:bool=False) :

    datasf = show_all()

    namee = entry_result.get()
    
    fullname = f'./Hasil- {namee if not "" else "SO"+datetime.now().strftime('%b%Y') }'
    if backup:
        fullname = f'Backup Hasil SO Terakhir'

    datasf.write_excel(fullname , autofit=True)


entry_result.bind('<FocusOut>', lambda x : x.widget.delete(0,'end') )

window.bind_class('Button','<Button-1>',lambda x : generate_fun() , add='+')
button_browse.bind('<Button-1>', lambda x : browse_file())
button_validloc.bind("<Button-1>", lambda event: messagebox.showinfo("Valid Locations", f"valid locations are :\n{readloc()}"))
button_calculating.bind('<Button-1>' , lambda x : simplecalculate())
button_add.bind('<Button-1>' , lambda x : submitData())
button_subtract.bind('<Button-1>',lambda x : subtract_it())
button_showcurrent.bind('<Button-1>' , lambda _ : show_all())
button_showall_selisih.bind('<Button-1>' , lambda _ : showall_selisih())
button_track.bind('<Button-1>' , lambda _ : trackselisih())
button_clear.bind('<Button-1>',lambda x :clear_all_entries())
button_export

button_test1.bind('<Button-1>' , lambda x : insert_initdata() )
button_test2.bind('<Button-1>' , lambda x : validate())
button_test3.bind('<Button-1>' , lambda x : testingbutton())

window.resizable(False, False)

"""
Tkinter Bind Cheat Sheet
=======================

Overview:
    widget.bind(event, handler) -> Bind an event to a handler function.
    Event format: "<Modifier-Type-Detail>" (e.g., "<Button-1>", "<Control-Key-a>")

Common Events:
    Mouse:
        "<Button-1>"      : Left click
        "<Button-2>"      : Middle click (or scroll wheel on some systems)
        "<Button-3>"      : Right click
        "<ButtonRelease-1>" : Left button release
        "<Motion>"        : Mouse movement
        "<Enter>"         : Mouse enters widget
        "<Leave>"         : Mouse leaves widget
    Keyboard:
        "<Key>"           : Any key press (use event.char or event.keysym)
        "<Return>"        : Enter key
        "<BackSpace>"     : Backspace key
        "<Key-a>"         : Specific key 'a'
        "<Control-Key-a>" : Ctrl + A
        "<Shift-Key-A>"   : Shift + A (uppercase)
    Window:
        "<Configure>"     : Widget resized
        "<FocusIn>"       : Widget gains focus
        "<FocusOut>"      : Widget loses focus
        "<Destroy>"       : Widget destroyed

Event Object Attributes (in handler):
    event.char        : Character for key events (e.g., 'a')
    event.keysym      : Key symbol (e.g., 'Return', 'space')
    event.x, event.y  : Mouse coordinates relative to widget
    event.widget      : Widget that triggered the event
    event.type        : Event type (e.g., '4' for ButtonPress)

Binding Levels:
    widget.bind(event, handler)        : Bind to specific widget
    widget.bind_class(className, event, handler) : Bind to all widgets of a class (e.g., "Entry")
    root.bind_all(event, handler)      : Bind to all widgets in app

Examples:
    button.bind("<Button-1>", lambda e: print("Left clicked"))
    entry.bind("<Return>", lambda e: print(entry.get()))
    root.bind_all("<Control-q>", lambda e: root.quit())

Notes:
    - Use "+" for multiple handlers: widget.bind(event, handler, add="+")
    - Unbind with widget.unbind(event)
    - Modifiers: Control, Shift, Alt, Command (macOS)
"""

if __name__ == '__main__':
    window.mainloop()


# app = ENTRIES()
# app.mainloop()
#     return window , RECAP_BUTTON, RECAP_ENTRY

# windows , buttons , entrys= main_UI()



# windows.mainloop()
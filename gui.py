import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8

from tkinter import FLAT, Tk, Canvas, Entry, PhotoImage ,StringVar , Text ,Frame
from tkinter.ttk import OptionMenu, Radiobutton ,Style


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\MARKETING SUPPORT\Documents\asteros\astrs_work\database\General\Apps\App3\build\assets\frame0")

# def relative_to_assets(filename):
#     return os.path.join(os.path.dirname(__file__), "assets", filename)


class Main_UI():
    def __init__(self):
        super().__init__()

        self.root = Tk()
        self.root.geometry("901x582")
        self.root.configure(bg = "#F6F6EF")
        self.root.title("ASTEROS STOCK OPNAME")
        self.root.resizable(False,False)

        self.main = Canvas(self.root, bg = "#F6F6EF", height = 582, width = 901, bd = 0, highlightthickness = 0, relief = "ridge")
        self.main.place(x = 0, y = 0)
        

        kolian_image = PhotoImage( file=self.relative_to_assets('entry_kolian.png'))
        calcu_isi_image = PhotoImage( file=self.relative_to_assets('entry_calcu.png'))
        keterangan_image = PhotoImage( file=self.relative_to_assets('entry_keterangan.png'))
        locatio_imagen = PhotoImage( file=self.relative_to_assets('entry_location.png'))
        output_image = PhotoImage( file=self.relative_to_assets('entry_output.png'))
        sku_qty = PhotoImage( file=self.relative_to_assets('entry_sku_qty.png'))
        upload = PhotoImage( file=self.relative_to_assets('entry_upload.png'))
        logo = PhotoImage(file=self.relative_to_assets("image_1.png"))

        # upload file
        self.main.create_text(40.0, 43.0, anchor="nw", text="Upload File", fill="#000000", font=("Inter Bold", 12 * -1))
        self.main.create_image( 204.0, 82.5, image=upload )
        self.upload_entry = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.upload_entry.place( x=36.0, y=65.0, width=336.0, height=30.0 )

        # brand
        self.main.create_text( 800.0, 96.0, anchor="nw", text="Maker : Ben", fill="#000000", font=("Inter", 12 * -1))
        self.main.create_image( 835.0, 69.0, image=logo )

        # TEXT
        # so options
        self.main.create_text( 65.00000762939453, 127.0, anchor="nw", text="SESSION", fill="#000000", font=("Inter Bold", 12 * -1 ))
        sessions = ["SO 1", "SO 2"]
        default_value = StringVar(value="SO 2")
        style = Style()  # Instantiate Style
        style.configure("warnaopsi.TMenubutton", background="#f1f2e0", foreground="#000000", borderwidth=2, relief="flat")
        self.session = OptionMenu(self.root, default_value, *sessions, style="warnaopsi.TMenubutton")
        self.session.place(x=50, y=200, width=80, height=30)

        # Input place holder
        self.sku_name = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.main.create_image( 421.5, 162.5, image=sku_qty )
        self.sku_name.place( x=372.0, y=145.0, width=99.0, height=33.0 )
        self.main.create_text( 372.0, 127.0, anchor="nw", text="SKU :", fill="#000000", font=("Inter Bold", 12 * -1) )

        # qty
        self.amount = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.main.create_image(421.5, 223.5, image = sku_qty)
        self.amount.place( x=372.0, y=206.0, width=99.0, height=33.0 )
        self.main.create_text( 372.0, 188.0, anchor="nw", text="Quantity :", fill="#000000", font=("Inter Bold", 12 * -1) )

        # another
        self.another_qty = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.main.create_image( 421.5, 291.5,  image=sku_qty )
        self.another_qty.place( x=372.0, y=274.0, width=99.0, height=33.0 )
        self.main.create_text( 372.0, 258.0, anchor="nw", text="Add-on QTY ( Ops ) :", fill="#000000", font=("Inter Bold", 8 * -1) )

        # _image
        self.main.create_text( 23.0, 465.0, anchor="nw", text="Voila :", fill="#000000", font=("Inter Bold", 10 * -1) )
        output_frame = Frame(self.root)
        output_frame.grid(row=5, column=0, padx=10, pady=5, sticky="nsew")
        output_frame.grid_columnconfigure(0, weight=1)
        output_frame.grid_rowconfigure(0, weight=1)
        self.main.create_image(258.5, 520.5, image= output_image )
        self.output = Text(output_frame, width=60 , height= 25 , bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 , font=("Arial", 12) ,wrap="word" ,insertbackground="black")
        self.output.place( x=25.0, y=481.0, width=467.0, height=77.0 )
        
        # Keterangan
        self.main.create_text( 32.0, 324.0, anchor="nw", text="Keterangan :", fill="#000000", font=("Inter Bold", 12 * -1) )
        self.main.create_image( 129.0, 359.5, image = keterangan_image )
        self.keterangan_entry = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.keterangan_entry.place( x=32.0, y=342.0, width = 194.0, height=33.0 )

        # location
        self.main.create_text( 217.00001525878906, 127.0, anchor="nw", text="LOCATION", fill="#000000", font=("Inter Bold", 12 * -1) )
        self.main.create_text( 159.0, 276.0, anchor="nw", text="*make sure that u place / write location \nwhere it already set at ( show valid loc )\nto prevent any future error.", fill="#FF0000", font=("Inter", 10 * -1) )
        self.main.create_image( 250.5, 181.5, image=locatio_imagen )
        self.locations = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.locations.place( x=179.0, y=164.0, width=143.0, height=33.0 )

        # divider
        self.main.create_rectangle( 28.99999976134464, 130.0, 30.00000762939453, 311.0, fill="#000000", outline="")
        self.main.create_rectangle( 149.00000739073917, 130.0, 150.00001525878906, 311.0, fill="#000000", outline="")
        self.main.create_rectangle( 349.9999921319501, 130.0, 351.0, 311.0, fill="#000000", outline="")
        self.main.create_rectangle( 490.9999921319501, 130.0, 492.0, 311.0, fill="#000000", outline="")

        # kolian (main)
        self.main.create_text(271.0, 329.0, anchor="nw", text="Koli:", fill="#000000", font=("Inter Bold", 8 * -1) )
        self.main.create_text(327.0, 329.0, anchor="nw", text="isi :", fill="#000000", font=("Inter Bold", 8 * -1) )
        self.main.create_image(345.0, 359.5, image = kolian_image)
        self.isian1 = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 ) 
        self.isian1.place( x=323.0, y=342.0, width=44.0, height=33.0 )
        self.isian2 = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.isian2.place( x=443.0, y=342.0, width=44.0, height=33.0 )

        # kolian (ops)
        self.main.create_text(391.0, 329.0, anchor="nw", text="Koli (ops):", fill="#000000", font=("Inter Bold", 8 * -1) )
        self.main.create_text(447.0, 329.0, anchor="nw", text="isi (ops):", fill="#000000", font=("Inter Bold", 8 * -1) )
        self.main.create_image(465.0, 359.5, image = kolian_image)
        self.kolian1= Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.kolian1.place( x=269.0, y=342.0, width=44.0, height=33.0 )
        self.kolian2 = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.kolian2.place( x=389.0, y=342.0, width=44.0, height=33.0 )

        # simple calc
        self.main.create_text( 570.0, 131.0, anchor="nw", text="tulis perhitungan :", fill="#000000", font=("Inter Bold", 8 * -1) )
        self.main.create_image(670.0,162.5,image= calcu_isi_image)
        self.calcu_input = Entry(bd=0,bg="#D9D9D9",fg="#000716",highlightthickness=0)
        self.calcu_input.place(x=570.0,y=145.0,width=200.0,height=33.0)

        # quotes
        self.main.create_rectangle( 560.0, 190.0, 839.0, 309.0, fill="#D9D9D9", outline="")
        self.main.create_text( 561.0, 191.0, anchor='nw', text="RANDOM QUOTES", fill="#000000", font=("Inter Bold", 24 * -1) )
        
    def relative_to_assets(self, filename) -> Path:
        # return ASSETS_PATH / Path(path)
        return os.path.join(os.path.dirname(__file__), "assets", filename)
        
    def clear_entry(self):
        '''this will clear entry view for when on displays'''
        return
    
    def button_pressed(self , event):
        '''this is to kinda make the button to be freeze when it click'''
        pass

    def button_release(self , event):
        '''this is to kinda make the button to be un-freeze when it click the freeze one'''
        pass

    def generate_quotes(self):
        pass




# entry_bg_2 = canvas.create_image(
#     430.5,
#     240.5,
#     image=entry_image_2
# )

# entry_bg_3 = canvas.create_image(
#     430.5,
#     300.5,
#     image=entry_image_3
# )

# entry_bg_4 = canvas.create_image(
#     204.0,
#     81.0,
#     image=entry_image_4
# )


# entry_bg_5 = canvas.create_image(
#     261.5,
#     461.5,
#     image=entry_image_5
# )


# entry_bg_6 = canvas.create_image(
#     251.5,
#     201.0,
#     image=entry_image_6
# )

# entry_image_2


try:
    Main_UI().root.mainloop()
except:
    Main_UI().main.mainloop()

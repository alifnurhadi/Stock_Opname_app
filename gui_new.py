# from tkinter import *
# Explicit imports to satisfy Flake8
import os
from pathlib import Path
from tkinter import StringVar, Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog , messagebox
from tkinter.ttk import Combobox, OptionMenu, Style
from typing import Any
from PIL import ImageTk
from business_logic import *


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
    
logics = DBManager()

# def main_UI():
window = Tk()

window.geometry("901x582")
window.configure(bg = "#CDCDCA")

canvas = Canvas(window, bg="#CDCDCA", height=582, width=901, bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)


entry_image_9 = PhotoImage(file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(250.5, 181.5, image=entry_image_9)
entry_location = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_location.place(x=179.0, y=164.0, width=143.0, height=33.0)
entry_image_6 = PhotoImage(file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(204.0, 82.5, image=entry_image_6)
entry_upload = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_upload.place(x=36.0, y=65.0, width=336.0, height=33.0)
entry_image_7 = PhotoImage(file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(129.0, 359.5, image=entry_image_7)
entry_keterangan = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_keterangan.place(x=32.0, y=342.0, width=194.0, height=33.0)
entry_image_8 = PhotoImage(file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(258.5, 520.5, image=entry_image_8)
entry_result = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_result.place(x=25.0, y=481.0, width=467.0, height=77.0)
entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(421.5, 162.5, image=entry_image_1)
entry_sku = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_sku.place(x=372.0, y=145.0, width=99.0, height=33.0)

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_image_5 = PhotoImage(file=relative_to_assets("entry_5.png"))
entry_image_10 = PhotoImage(file=relative_to_assets("entry_10.png"))
entry_image_11 = PhotoImage(file=relative_to_assets("entry_11.png"))
entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_4 = canvas.create_image(291.0, 359.5, image=entry_image_4)
entry_bg_5 = canvas.create_image(411.0, 359.5, image=entry_image_5)
entry_bg_10 = canvas.create_image(345.0, 359.5, image=entry_image_10)
entry_bg_11 = canvas.create_image(465.0, 359.5, image=entry_image_11)
entry_bg_2 = canvas.create_image(421.5, 223.5, image=entry_image_2)
entry_bg_3 = canvas.create_image(421.5, 291.5, image=entry_image_3)

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

entry_image_12 = PhotoImage(file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(670.0, 162.5, image=entry_image_12)
entry_calculator = Entry(bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
entry_calculator.place(x=570.0, y=145.0, width=200.0, height=33.0)

# Global variables for Combobox
sessions = ["SO 1", "SO 2"]
default_value = StringVar(value="SO 2")

def on_session_select(event ,combobox):
    selected = default_value.get()
    combobox.configure(values=[selected])
def reset_session(combobox):
    default_value.set("SO 2")
    combobox.configure(values=sessions)

style = Style() 
style.configure( "warnaopsi.TCombobox", background="#f1f2e0", foreground="#000000", borderwidth=2, relief="flat" )
session_combobox = Combobox( canvas, textvariable=default_value, values=sessions, style="warnaopsi.TCombobox", state="readonly" )
session_combobox.place(x=50, y=200, width=80, height=30)
session_combobox.bind("<<ComboboxSelected>>", lambda event: on_session_select(event, session_combobox))
reset_button = Button( canvas, text="Reset Session", command= lambda : reset_session(session_combobox), bg="#D9D9D9", fg="#000716", relief="flat" )
reset_button.place(x=50, y=250, width=70, height=25 , anchor='nw')

def get_fullqty():
    hitungkolian1 = logics.handle_kolian( int(entry_koli1.get()) , int(entry_isi1.get()))
    hitungkolian2 = logics.handle_kolian( int(entry_koli2.get()) , int(entry_isi2.get()))
    fullqty:int = hitungkolian1 + hitungkolian2 + int(entry_qty.get()) + int(entry_qty_tambahan.get())
    return fullqty

def debug():
    data = [entry_sku , entry_qty , entry_qty_tambahan , entry_koli1 , 
            entry_koli2 , entry_upload , entry_keterangan , entry_result , 
            entry_location , entry_isi1 , entry_isi2 , entry_calculator]
    for i , d  in enumerate(data, start=1):
        print(f'{i} - {d.get()}')

canvas.create_text(800.0, 96.0, anchor="nw", text="Maker : Ben", fill="#000000", font=("Inter", -12))
image_image_1 = PhotoImage(file=relative_to_assets("image_1.png"))
canvas.create_image(835.0, 69.0, image=image_image_1)

'''
<Button>: Indicates a mouse button event.
-(number): Specifies the button number:
1 = Left mouse button.
2 = Middle mouse button (if available, e.g., on a three-button mouse).
3 = Right mouse button.
'''

def browse_file():
        filename = filedialog.askopenfilename(
            title="Select Excel File",
            filetypes=(("Excel files", "*.xlsx *.xls"), ("All files", "*.*"))
        )
        if filename:
            entry_upload.delete(0, 'end')
            entry_upload.insert(0, filename)
        try:
            logics.insert_basic
        except:
            return

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_browse = Button(image=button_image_1, borderwidth=0, highlightthickness=0, command=lambda: print("Browse"), relief="flat")
button_browse.place(x=398.0, y=55.0, width=89.0, height=51.0)
button_browse.bind('<Button-1>', lambda x : browse_file())

def add_data():
    
    sku = entry_sku.get()
    session = session_combobox.get()
    location = entry_location.get()
    qty = get_fullqty()
    kets = entry_keterangan.get()

    try:
        logics.inserting_main_data()
    except:
        return


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

button_validloc.bind("<Button-1>", lambda event: messagebox.showinfo("Valid Locations", f"valid locations are :\n{readloc()}"))

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
button_test2 = Button(image=button_image_10,borderwidth=0,highlightthickness=0,command=lambda: print("button_10 clicked"),text='in-test 2!',compound='center',font=('Arial',12 , 'bold') , fg='white',relief="flat")
button_test2.place(x=540.0,y=442.0,width=140.0,height=38.0)

button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
button_test1 = Button(image=button_image_11,borderwidth=0,highlightthickness=0,command=lambda: print('sss'),text='in-test 1!',font=('Arial',12 , 'bold') , fg='white',compound='center',relief="flat")
button_test1.place(x=540.0,y=340.0,width=140.0,height=38.0)

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
canvas.create_text(372.0, 258.0, anchor="nw", text="Qty tambahan :", fill="#000000", font=("Inter Bold", -10))
canvas.create_text(271.0, 329.0, anchor="nw", text="Koli:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(391.0, 329.0, anchor="nw", text="Koli:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(327.0, 329.0, anchor="nw", text="isi:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(447.0, 329.0, anchor="nw", text="isi:", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(570.0, 131.0, anchor="nw", text="tulis perhitungan :", fill="#000000", font=("Inter Bold", -8))
canvas.create_text(23.0, 465.0, anchor="nw", text="Voila :", fill="#000000", font=("Inter Bold", -10))
canvas.create_text(159.0, 276.0, anchor="nw", text="*make sure that u place / write location \nwhere it already set at ( show valid loc )\nto prevent any future error.", fill="#FF0000", font=("Inter", -10))
canvas.create_text(561.0, 191.0, anchor="nw", text="RANDOM QUOTES", fill="#000000", font=("JimNightshade Regular", -24))
canvas.create_text(795.9999718563797, 152.0, anchor="nw", text=":)", fill="#FFFFFF", font=("Inter Bold", -20))    

def create_logs(action)->str:
    ket = action
    if entry_koli1.get() != '0' or entry_koli1.get() != '0' & entry_keterangan.get() != None:
        texts = f'''{datetime.now().strftime('%H:%M "%d/%m')}-{ket} , {entry_sku.get()} - {get_fullqty()} - at {session_combobox.get()}
- {entry_keterangan.get()}'''
    elif  entry_koli1.get() != '0' or entry_koli1.get() != '0':
        texts = f'''{datetime.now().strftime('%H:%M "%d/%m')}-{ket} , {entry_sku.get()} - {get_fullqty()} - at {session_combobox.get()}
- {entry_koli1.get()}@{entry_isi1.get()} & {entry_koli1.get()}@{entry_isi1.get()}'''
    
    return texts


window.resizable(False, False)
'''
entry : 

1 - sku
2 - quant
3 - tambahan
4 - koli 1
5 - koli 2
6 - upload
7 - keterangan
8 - result
9 - location
10 - isi 1
11 - isi 2
12 - calcu


'''
# RECAP_ENTRY : dict[str,Any] = {
#     "sku" : entry_1 , 
#     "qty" : entry_2 , 
#     "additions": entry_3 , 
#     "kolian_1": entry_4 , 
#     "kolian_2": entry_5 , 
#     'upload': entry_6 , 
#     'keterangan': entry_7 , 
#     'output': entry_8 , 
#     'location': entry_9 , 
#     'isian_1': entry_10 , 
#     'isian_2': entry_11 , 
#     'calculator': entry_12 ,
#     'sessions': session_combobox
# }

# '''
# button :

# button 1 = browse
# button 2 = calculate
# button 3 = add
# button 4 = hijau pojok kanan (kiri bawah)
# button 5 = export
# button 6 = kuning
# button 7 = hijau sebelah kuning
# button 8 = hijau pojok kanan (kanan tengah)
# button 9 = hijau pojok kanan (kanan atas)
# button 10 = hijau pojok kanan (kiri tengah)
# button 11 = hijau pojok kanan (kiri atas)
# button 12 = show valid loc
# button 13 = clear
# '''
# RECAP_BUTTON :dict[str,Any] = {
#     'browse':button_1 ,
#     'calculate':button_2,
#     'add':button_3,
#     'export':button_5,
#     'substract':button_6,
#     'valid_loc':button_12

# }


if __name__ == '__main__':
    window.mainloop()


# app = ENTRIES()
# app.mainloop()
#     return window , RECAP_BUTTON, RECAP_ENTRY

# windows , buttons , entrys= main_UI()



# windows.mainloop()
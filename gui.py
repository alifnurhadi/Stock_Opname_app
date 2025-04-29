from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8

from tkinter import FLAT, Tk, Canvas, Entry, PhotoImage ,StringVar 
from tkinter.ttk import OptionMenu, Radiobutton ,Style

from button import ButtonLogic


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alifn\OneDrive\Desktop\urgent\workspace_2025_\WIP Project\kantor\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class Main_UI(ButtonLogic):
    def __init__(self):

        self.root = Tk()
        self.root.geometry("901x582")
        self.root.configure(bg = "#F6F6EF")
        self.root.title("ASTEROS STOCK OPNAME")
        self.root.resizable(False,False)

        self.main = Canvas(self.root, bg = "#F6F6EF", height = 582, width = 901, bd = 0, highlightthickness = 0, relief = "ridge")
        self.main.place(x = 0, y = 0)

        # upload file
        self.main.create_text(40.0, 43.0, anchor="nw", text="Upload File", fill="#000000", font=("Inter Bold", 12 * -1))
        self.upload = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0)
        self.upload.place( x=36.0, y=65.0, width=336.0, height=30.0 )

        # brand
        self.main.create_text( 800.0, 96.0, anchor="nw", text="Maker : Ben", fill="#000000", font=("Inter", 12 * -1))
        logo = PhotoImage(file=relative_to_assets("image_1.png"))
        self.main.create_image( 835.0, 69.0, image=logo )

        self.main.create_text( 65.00000762939453, 145.0, anchor="nw", text="SESSION", fill="#000000", font=("Inter Bold", 12 * -1 ))
        # Input place holder
        self.sku_name = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.main.create_text( 380.0, 145.0, anchor="nw", text="SKU :", fill="#000000", font=("Inter Bold", 12 * -1) )

        # so options
        
        sessions = ["SO 1", "SO 2"]
        default_value = StringVar(value="SO 2")
        style = Style()  # Instantiate Style
        style.configure("warnaopsi.TMenubutton", background="#f1f2e0", foreground="#000000", borderwidth=2, relief="flat")  # Configure the style
        self.session = OptionMenu(self.root, default_value, *sessions, style="warnaopsi.TMenubutton")  # Use the style name
        self.session.place(x=50, y=200, width=80, height=30)

        self.amount = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.main.create_text( 381.0, 205.0, anchor="nw", text="Quantity :", fill="#000000", font=("Inter Bold", 12 * -1) )

        self.another_qty = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.main.create_text( 380.0, 270.0, anchor="nw", text="Add-on QTY ( Ops ) :", fill="#000000", font=("Inter Bold", 8 * -1) )

        self.upload = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.output = Entry( bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0 )
        self.location = Entry( bd=0, bg="#D9D9D9", fg="#000716", highlightthickness=0 )
        self.main.create_text( 217.00001525878906, 145.0, anchor="nw", text="LOCATION", fill="#000000", font=("Inter Bold", 12 * -1) )
        
        self.sku_name.place( x=380.0, y=163.0, width=99.0, height=33.0 )
        self.amount.place( x=381.0, y=223.0, width=99.0, height=33.0 )
        self.another_qty.place( x=381.0, y=283.0, width=99.0, height=33.0 )
        self.upload.place( x=36.0, y=65.0, width=336.0, height=30.0 )
        self.output.place( x=23.0, y=363.0, width=477.0, height=195.0 )
        self.location.place( x=180.0, y=181.0, width=143.0, height=38.0 )

        # divider
        self.main.create_rectangle( 149.00000739073917, 148.0, 150.00001525878906, 329.0, fill="#000000", outline="")
        self.main.create_rectangle( 349.9999921319501, 148.0, 351.0, 329.0, fill="#000000", outline="")
        self.main.create_rectangle( 490.9999921319501, 148.0, 492.0, 329.0, fill="#000000", outline="")
        self.main.create_rectangle( 28.99999976134464, 148.0, 30.00000762939453, 329.0, fill="#000000", outline="")
        self.main.create_rectangle( 560.0, 139.0, 839.0, 320.0, fill="#D9D9D9", outline="")
        
        self.main.create_text( 23.0, 340.0, anchor="nw", text="Voila :", fill="#000000", font=("Inter Bold", 10 * -1) )
        self.main.create_text( 159.0, 294.0, anchor="nw", text="*make sure that u place / write location \nwhere it already set at ( show valid loc )\nto prevent any future error.", fill="#FF0000", font=("Inter", 10 * -1) )
        self.main.create_text( 561.0, 142.0, anchor="nw", text="RANDOM QUOTES", fill="#000000", font=("JimNightshade Regular", 24 * -1) )


        
        
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

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Button, PhotoImage , messagebox

import sys
sys.path.append('../')
from business_logic import SystemMain , DBManager


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alifn\OneDrive\Desktop\urgent\workspace_2025_\WIP Project\kantor\assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

class ButtonLogic(DBManager):
    def __init__(self):
        super().__init__()

        browse_button = PhotoImage( file=relative_to_assets("button_1.png"))
        button_1 = Button( image=browse_button, borderwidth=0, highlightthickness=0, command=lambda: print("Browse"), relief="flat" )
        button_1.place( x=398.0, y=55.0, width=89.0, height=51.0 )

        self.button_1 = Button(  borderwidth=0, highlightthickness=0, command=lambda: print("Browse"), relief="flat" )
        self.button_1.place( x=398.0, y=55.0, width=89.0, height=51.0 )

        self.button_2 = Button(  borderwidth=0, highlightthickness=0, command= lambda: print("add"), relief="flat")
        self.button_2.place( x=541.0, y=381.0, width=140.0, height=38.0 )

        self.button_3 = Button( borderwidth=0, highlightthickness=0, command=lambda: print("check diff clicked"), relief="flat" )
        self.button_3.place( x=540.0, y=503.0, width=140.0, height=38.0 )

        self.button_4 = Button( borderwidth=0, highlightthickness=0, command=lambda: print("export clicked"), relief="flat" )
        self.button_4.place( x=721.0, y=502.0, width=140.0, height=38.0 )

        self.button_5 = Button( borderwidth=0, highlightthickness=0, command=lambda: print("update clicked"), relief="flat" )
        self.button_5.place( x=541.0, y=443.0, width=140.0, height=38.0 )

        self.button_6 = Button( borderwidth=0, highlightthickness=0, command=lambda: print("track diff clicked"), relief="flat" )
        self.button_6.place( x=722.0, y=442.0, width=140.0, height=38.0 )

        self.button_7 = Button( borderwidth=0, highlightthickness=0, command=lambda: print("show all diff clicked"), relief="flat" )
        self.button_7.place( x=722.0, y=381.0, width=140.0, height=38.0 )

        self.button_8 = Button(  borderwidth=0, highlightthickness=0, command=lambda: print("show valid clicked"), relief="flat" )
        self.button_8.place( x=200.0, y=258.0, width=100.0, height=26.0 )

        # self.button_9 = Button(  borderwidth=0, highlightthickness=0, command=lambda: print("so1 clicked"), relief="flat" )
        # self.button_9.place( x=50.00000762939453, y=178.0, width=81.0, height=50.0 )

        # self.button_10 = Button(  borderwidth=0, highlightthickness=0, command=lambda: print("so2 clicked"), relief="flat" )
        # self.button_10.place( x=50.00000762939453, y=250.0, width=81.0, height=50.0 )

    


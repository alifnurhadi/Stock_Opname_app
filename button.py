
# https://github.com/alifnurhadi/Stock_Opname_app.git

import os
from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Button, PhotoImage , messagebox

import sys
from typing import Any
sys.path.append('../')
from business_logic import SystemMain , DBManager
import gui


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\alifn\OneDrive\Desktop\urgent\workspace_2025_\WIP Project\kantor\assets")

def relative_to_assets( filename) -> Path:
        # return ASSETS_PATH / Path(path)
        return os.path.join(os.path.dirname(__file__), "assets", filename)

class ButtonLogic(DBManager):
    def __init__(self):
        pass

    def simple_calc(self, entry:str) -> int:
        add = []
        sub = []
        for txt in entry.split('+'):
            cleantxt = txt.strip()
            if '-' in cleantxt:
                cleantxt2 = cleantxt.split('-')
                add.append(int(cleantxt2[0].strip()))
                sub.append(int(cleantxt2[-1].strip()))
            else:
                add.append(int(cleantxt))
        result = sum(add) - sum(sub)

        return result




RECAP:dict[str,Any] =  {
    'ADD' : ... ,
    'UPDATE' : ... ,
    'MODIFY_ADD' : ... ,
    'SUBTRACT' : ... ,
    'EXPORT' : ... ,
    'CHECK' : ... ,
    'CHECK_ALL' : ... ,
    'TRACK_LOG' : ... ,
    'BROWSE' : ... ,
    'SHOW_LOC' : ... ,
    'CALC' : ... 
}




if __name__ == '__main__':
    print('hello')


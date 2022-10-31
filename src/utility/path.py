import os
import string
import sys

def get_path(filename) -> string:
    
    if getattr(sys, 'frozen', False):
        PATH = filename 
    else:
        PATH = os.path.join(os.path.dirname("src/designer_files/"), filename)

    try:
        os.chdir(sys._MEIPASS)
    except:
        pass
    
    return PATH
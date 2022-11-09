import os
import string
import sys

def is_running_executable() -> bool:
    if getattr(sys, 'frozen', False):
        return True
    
    return False

def change_to_correct_dir() -> bool:
    try:
        if getattr(sys, 'frozen', False):
            PATH = os.path.dirname(sys.executable)
            os.chdir(PATH)
            return True
    except:
        return False

def get_correct_path_of_designer_files(filename) -> string:
    
    if getattr(sys, 'frozen', False):
        PATH = filename 
    else:
        PATH = os.path.join(os.path.dirname("src/designer_files/"), filename)

        try:
            os.chdir(sys._MEIPASS)
        except:
            pass
    
    return PATH

def get_correct_path_of_db(filename) -> string:
    
    if getattr(sys, 'frozen', False):
        PATH = filename 
    else:
        PATH = os.path.join(os.path.dirname("src/database/"), filename)
    
    return PATH

def change_to_child() -> bool:
    try:
        os.chdir(sys._MEIPASS)
        return True
    except:
        return False

def get_correct_path_of_save_file(filename) -> string:
    
    if getattr(sys, 'frozen', False):
        PATH = os.path.dirname(sys.executable)
    elif __file__:
        PATH = filename

    return PATH

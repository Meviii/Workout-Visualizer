import xlsxwriter
import openpyxl
import src.utility.path as util_path
import os
import sys

def get_correct_path_of_save_file(file_name):
    if getattr(sys, 'frozen', False):
        PATH = os.path.dirname(sys.executable)
        os.chdir(PATH)
    elif __file__:
        PATH = file_name

    return PATH


def make_excel(data_workouts, data_exercises, WORKBOOK):
    # create file
    
    DIR = get_correct_path_of_save_file(WORKBOOK)
    
    workbook = xlsxwriter.Workbook(WORKBOOK)
    workbook.close()
    
    # open
    workbook = xlsxwriter.Workbook(WORKBOOK)
    worksheet = workbook.add_worksheet()
    
    # Starting row/col
    row = 4
    col = 2

    sorted_workouts = sort_workout_by_day(data_workouts)
    # store current day for day matching
    current_day_streak = sorted_workouts[0][2]

    worksheet.write(row, col, current_day_streak)
    
    workout_row_incrementer = 2
    row_incrementer_for_workout_change = find_available_row(row, col, WORKBOOK) + 1 # + 1 for spacing next workout
    for w_id, w_name, w_day in (sorted_workouts):
        
        # if day is same        
        if current_day_streak != w_day:
            row = 4
            col += 4
            worksheet.write(row, col, w_day)
            current_day_streak = w_day
        
        # write workout name
        worksheet.write(row + workout_row_incrementer, col, w_name)
        
        # for exercises with workout id 
        row_incre = 4
        for e_id, e_name, e_sets, e_reps, e_workout_id in data_exercises:
            if e_workout_id == w_id:
                worksheet.write(row + row_incre, col, e_name)
                worksheet.write(row + row_incre, col + 1, (e_sets + " sets"))
                worksheet.write(row + row_incre, col + 2, (e_reps + " reps"))
                row_incre += 1

        row += row_incrementer_for_workout_change
        
    workbook.close()

def find_available_row(row, col, WORKBOOK):
    workbook = openpyxl.load_workbook(WORKBOOK)
    worksheet = workbook.active
    SAFE_RANGE = 4
    
    is_safe = False
    while not is_safe:
        if (worksheet.cell(row, col).value) == None:
            for i in range(SAFE_RANGE):
                if (worksheet.cell(row + i, col).value) != None:
                    break
                is_safe = True
                return row
        row += SAFE_RANGE
        
def sort_workout_by_day(workouts_to_sort, sorted_workouts = [], current_day = 0):
    
    MAX_DAY_COUNT = 7
    DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    
    # break
    if current_day == MAX_DAY_COUNT:
        return sorted_workouts
    
    # add to final list for current day
    for workout in workouts_to_sort:
        if str(workout[2]).lower() == DAYS[current_day]:
            sorted_workouts.append(workout)
    
    return sort_workout_by_day(workouts_to_sort, sorted_workouts, current_day + 1)

def excel_string_width(str):
    """
    Calculate the length of the string in Excel character units. This is only
    an example and won't give accurate results. It will need to be replaced
    by something more rigorous.

    """
    string_width = len(str)

    if string_width == 0:
        return 0
    else:
        return string_width * 1.25

def write_value(worksheet,row, col, string):
    min_width = 0

    # Check if it the string is the largest we have seen for this column.
    string_width = excel_string_width(string)
    if string_width > min_width:
        max_width = worksheet.default_col_width
        worksheet.set_column(col, col, width = string_width)
        if string_width > max_width:
            worksheet.set_column(col, col, width = string_width)
    
    worksheet.write(row, col, string)
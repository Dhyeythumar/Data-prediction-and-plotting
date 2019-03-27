"""Converts the excel data into pickle file."""
import pickle

import xlrd

# total_rows = 60 (2-59)
# total_column = 83
# Sap-ID (column no.) = 0
# Name (column no.) = 2
# CGPA (column no.) = 82


def data_extraction(file_name):
    """Extract data form excel file."""
    loc = (file_name)
    rb = xlrd.open_workbook(loc)
    sheet = rb.sheet_by_index(0)

    temp = {}
    for r in range(2, 60):
        temp[int(sheet.cell_value(r, 0))] = [sheet.cell_value(r, 2).lower(), sheet.cell_value(r, 82)]
    return temp


def pickle_io():
    """Dump data in to a pickle file."""
    dict1 = data_extraction("Excel_data/Sem I.xlsx")
    dict2 = data_extraction("Excel_data/Sem II.xlsx")

    with open("Pickle_files/test1_data.pickle", "wb") as data_out:
        pickle.dump(dict1, data_out)
    with open("Pickle_files/test2_data.pickle", "wb") as data_out:
        pickle.dump(dict2, data_out)

    del(dict1)
    del(dict2)

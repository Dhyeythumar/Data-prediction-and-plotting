"""Predict the third sem CGPA."""
import os

import pickle

# import sqlite3

import data_analysis

import data_plotter

import list_formation


# conn = sqlite3.connect("College_data.db")
# c = conn.cursor()
# c.execute("drop table Sem_1")
# c.execute("""CREATE TABLE IF NOT EXISTS Sem_1 (name TEXT, sapid INTEGER UNIQUE, sem INTEGER)""")
# c.execute("drop table Sem_2")
# c.execute("""CREATE TABLE IF NOT EXISTS Sem_2 (name TEXT, sapid INTEGER UNIQUE, sem INTEGER)""")
# c.execute("drop table Sem_3")
# c.execute("""CREATE TABLE IF NOT EXISTS Sem_3 (name TEXT, sapid INTEGER UNIQUE, sem INTEGER)""")


def iterator(t):
    """Iterate through the data_list."""
    temp = {}
    # data_list_updated = {}
    for x in t:

        # c.execute("""INSERT INTO Sem_1 VALUES(?, ?, ?)""", (t[x][0], x, t[x][1]))
        # c.execute("""INSERT INTO Sem_2 VALUES(?, ?, ?)""", (t[x][0], x, t[x][2]))

        value = predict_value(x, t[x])
        value = (int(value * (10**2)) / (10.0**2))
        temp[x] = [t[x][0], value]

        # c.execute("""INSERT INTO Sem_3 VALUES(?, ?, ?)""", (t[x][0], x, value))
        # conn.commit()
        # data_list_updated[x] = t[x]
        # data_list_updated[x].insert(3, value)
        # print(value)
    # conn.close()
    return temp


def predict_value(sap, value_list):
    """Predict the third value."""                     # value_list = [name, sem1, sem2, diff, base]
    # print(sap, value_list)
    e = 2.718281828
    b = round((value_list[4] - 0.1), 2)
    while True:
        try:
            upper_bound = 9.99
            # lower_bound = int({True: value_list[2], False: value_list[1]}[value_list[1] > value_list[2]])
            cal = round((e**b) / (2 * value_list[2]), 4)
            d = abs(int(value_list[1]) - int(value_list[2]))
            cal = ((-1)**d) * cal
            temp = round((value_list[2] + cal), 3)

            if int(value_list[2]) < int(value_list[1]):
                cal = (-1) * cal
                temp = round((value_list[1] + cal), 3)

            if temp <= upper_bound:
                return temp
            else:
                b -= 0.1
                b = round(b, 2)
            # elif temp > upper_bound:
            #     b -= 0.1
            #     b = round(b, 2)
        except Exception as ep:
            print(str(ep))


def print_data(temp):
    """Print the data."""
    e = 2.718281828
    # print(temp)
    # {
    #     sap: [name, sem1, sem2, diff, base]
    # }
    for x in temp:
        # print(temp[x][0])
        print(temp[x][0], x, temp[x][1], temp[x][2], temp[x][3], temp[x][4])
        if temp[x][3] < 0:
            print("*****sem2 ", round((temp[x][1] - (e**temp[x][4]) / (2 * temp[x][1])), 2))
        elif temp[x][3] == 0:
            print("*****sem2 ", temp[x][2])
        else:
            print("*****sem2 ", round((temp[x][1] + (e**temp[x][4]) / (2 * temp[x][1])), 2))


def data_prediction():
    """Main function."""
    print(__name__)
    pickle_file_list = ('data_list.pickle', 'test1_data.pickle', 'test2_data.pickle', 'test3_data.pickle')

    path = "Pickle_files/"
    dir_file_list = tuple(os.listdir(path))

    # comparing pickle_file_list data in dir_file_list list.
    result = all(elements in dir_file_list for elements in pickle_file_list)

    if result is not True:
        data_analysis.pickle_io()
        list_formation.list_creation()

    with open("Pickle_files/data_list.pickle", "rb") as data_in:
        data_list = pickle.load(data_in)                          # dict_list = {sap : [name, sem1, sem2, diff, base] }
    # print_data(data_list)

    dict3 = iterator(data_list)

    with open("Pickle_files/test3_data.pickle", "wb") as data_out:
        pickle.dump(dict3, data_out)
    del(dict3)

    # print(data_list_updated)
    # with open("Pickle_files/data_list.pickle", "wb") as data_out:
    #     pickle.dump(data_list_updated, data_out)
    # del(data_list_updated)
    #
    # c.execute("""SELECT * FROM Sem_2""")
    # print(c.fetchall())
    # conn.close()

    data_plotter.data_plot()


data_prediction()

"""Converts the pickle file data into linked list."""
import pickle


class Node:
    """Node of student's data."""

    def __init__(self, name, sap, sem1, sem2, diff):
        self.name = name
        self.sap = sap
        self.sem1 = sem1
        self.sem2 = sem2
        self.diff = diff
        self.base = None
        self.next = None
        self.prev = None


class Linkedlist:
    """Starting pointer of the list."""

    def __init__(self):
        self.head = None

    def insert(self, sem1, sem2):
        """Create list of student's data."""
        newnode = Node(sem1[1][0], sem1[0], sem1[1][1], sem2[1][1], round(sem2[1][1] - sem1[1][1], 4))
        temp = self.head
        if self.head is None:
            self.head = newnode
        else:
            while temp.next is not None:
                temp = temp.next
            temp.next = newnode

    def list_iterator(self):
        """Iterate through list of student's data."""
        temp = self.head
        # e = 2.718281828
        if temp is None:
            print("!!**The link list is empty**!!")
        else:
            while temp is not None:
                temp.base = cal_base(temp)
                """
                print(temp.name, temp.sap, temp.sem1, temp.sem2, temp.diff)
                if temp.diff < 0:
                    print("Approx. sem2 ", round((temp.sem1 - (e**temp.base) / (2 * temp.sem1)), 2))
                else:
                    print("Approx. sem2 ", round((temp.sem1 + (e**temp.base) / (2 * temp.sem1)), 2))
                """
                temp = temp.next

    def data_dump(self):
        """Dump data in pickle file."""
        temp = self.head
        if temp is None:
            print("!!**The link list is empty**!!")
        else:
            temp_list = {}         
            while temp is not None:
                temp_list[temp.sap] = [temp.name, temp.sem1, temp.sem2, temp.diff, temp.base]
                temp = temp.next
        return temp_list


def cal_base(t):
    """Calculate the base value for each node."""
    if t.diff == 0.0:
        return t.diff

    e = 2.718281828
    b = 2.1
    l1 = 0
    l2 = 0

    # checks for the presicion 0.01
    while (l1 >= 0 and l2 == 0) or (l1 == 0 and l2 <= 0):

        cal = round((e**b) / (2 * t.sem1), 2)
        temp = round((cal - abs(t.diff)), 2)

        if temp < -0.01:
            b += 0.1
            b = round(b, 2)
            l1 += 1
            # print("inc ", b)
        elif temp > 0.01:
            b -= 0.1
            b = round(b, 2)
            l2 -= 1
            # print("dec ", b)
        else:
            # print("true", b)
            return b

    # checks for the presicion other then 0.01
    cal = round((e**b) / (2 * t.sem1), 2)
    temp = round((cal - abs(t.diff)), 2)

    b1 = round((b - 0.1), 2)
    b2 = round((b + 0.1), 2)
    t1 = abs(round((((e**b1) / (2 * t.sem1)) - abs(t.diff)), 2))
    t2 = abs(round((((e**b2) / (2 * t.sem1)) - abs(t.diff)), 2))
    temp = abs(temp)

    # return b2 if temp > t2 else b if t1 > t2 else b1 if temp > t1 else b
    return {True: {True: b, False: b2}[t2 > temp], False: {True: b, False: b1}[t1 > temp]}[t1 > t2]


def create_linkedlist(dict1, dict2):
    """Create the linked list."""
    start = Linkedlist()
    for s1 in dict1.items():
        for s2 in dict2.items():
            if s1[0] == s2[0]:
                start.insert(s1, s2)
    start.list_iterator()
    temp = start.data_dump()
    return temp


def list_creation():
    """Load data from pickle file."""
    with open("Pickle_files/test1_data.pickle", "rb") as data_in:
        dict1 = pickle.load(data_in)
    with open("Pickle_files/test2_data.pickle", "rb") as data_in:
        dict2 = pickle.load(data_in)

    dict_list = create_linkedlist(dict1, dict2)
    del (dict1)
    del(dict2)
    # dict_list = {sap : [name, sem1, sem2, diff, base] }
    with open("Pickle_files/data_list.pickle", "wb") as data_out:
        pickle.dump(dict_list, data_out)
    del(dict_list)

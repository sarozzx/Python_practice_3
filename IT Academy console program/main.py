from time import sleep
import os
import csv
from csv import writer
class main:
    def __init__(self):
        self.list=[]
        self.list1=[]
        # input_file={}
    def options(self, x):

        switcher = {
            0: self.stay,
            1: self.inquirycourse,
            2: self.addstudent,
            3: self.information,
            4: self.exit,


        }
        return switcher.get(x,False)
    def stay(self):
        return 0
    def inquirycourse(self):
        print("IT ACADEMY")
        print("Student Registration fee : Rs. 20000 (deposit). ")
        print("Students are allowed to pay in two installments with Rs. 10000 each.")
        y=int(input("Enter 0 to go back "))
        return y
    def addstudent(self):

        name=input("Enter name : ")
        amt=int(input("Amount deposited : "))
        z=20000-amt
        x=(name,amt,z)
        self.list.append(tuple(x))
        filename = "studentinfo" + ".csv"
        with open(filename, 'a+', newline='') as csvfile:
            csvwriter =writer(csvfile)
            csvwriter.writerow(self.list)
        y=int(input("Enter 0 to go back "))
        return y
    def information(self):
        input_file = csv.DictReader(open("studentinfo.csv"))
        for items in input_file:
            self.list1.append(items)
        for item in self.list1:
            print(item)
        y=int(input("Enter 0 to go back "))
        return y
    def exit(self):
        exit()

    def create_csv(self,list1):
        filename = "studentinfo" + ".csv"

        with open(filename, 'w') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerows(list1)
def start():

    print("IT ACADEMY")

    print("1.Inquiry course          2.New Student")
    print("3.Student's information   4.exit")
    print("0: Stay")

abc=0
while(abc==0):
    os.system('cls')
    start()


    obj=main()

    x=int(input("ENter a key to continue : "))


    y = obj.options(x)
    abc=1
    if y:
        os.system('cls')
        abc=y()

    if abc!=0:
        print("Error")


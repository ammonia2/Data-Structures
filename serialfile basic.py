import pickle
import os

class Product:
    ProductID = int(0)         # Data Type Integer
    Name = ""             # Data Type String
    UnitPrice = float(0.0)           # Data Type Real
    Discontinued = False      # Data Type Boolean

def add_record():
    NewRecord = Product()
    NewRecord.ProductID = int(input("Enter Product ID :"))
    NewRecord.Name = input("Enter Name : ")
    NewRecord.UnitPrice = float(input("Enter Unit Price :"))
    NewRecord.Discontinued = False
    file1 = open("Products.dat", "ab")
    pickle.dump(NewRecord, file1)
    file1.close()


def print_all():
    TempRecord = Product()
    file1 = open("Products.dat", "rb")
    file1.read()
    eof = file1.tell()
    file1.seek(0)
    while file1.tell() != eof:
        TempRecord = pickle.load(file1)
        print("Product ID          :", TempRecord.ProductID)
        print("Product Name        :", TempRecord.Name)
        print("Unit Price          :", TempRecord.UnitPrice)
        print("Discontinued Status :", TempRecord.Discontinued)
    file1.close()
    
def search(search_item):
    TempRecord = Product()
    file1=open("Products.dat","rb")
    file1.read()
    eof=file1.tell()
    file1.seek(0)
    found=False
    while file1.tell()!=eof:
        TempRecord = pickle.load(file1)
        if search_item == TempRecord.ProductID:
            found = True
            print("Product Name:        ",TempRecord.Name)
            print("Unit Price:          ",TempRecord.UnitPrice)
            print("Discontinued Status: ",TempRecord.Discontinued)
    if found==False:
        print("Not found!")
    file1.close()
    
def average():
    TempRecord= None  #only declaring variable to be used ahead
    file1=open("Products.dat","rb")
    file1.read()
    eof=file1.tell()
    file1.seek(0)
    Count=0
    TotalPrice=0.0
    AveragePrice=0.0
    
    while file1.tell()!=eof:
        TempRecord=pickle.load(file1)
        TotalPrice=TempRecord.UnitPrice+TotalPrice
        Count+=1
    AveragePrice=TotalPrice/Count
    print("Average: ",AveragePrice)
    file1.close()

def delete(item):
    TempRecord = Product()
    file1 = open("Products.dat", "rb")
    file2 = open("Temp.dat", "wb")
    file1.read()
    eof = file1.tell()
    file1.seek(0)
    found = False
    while file1.tell() != eof:
        TempRecord = pickle.load(file1)
        if TempRecord.ProductID == item:
            found = True
        else:
            pickle.dump(TempRecord, file2)
    file1.close()
    file2.close()
    if found == False:
        print("Record not Found")
        os.remove("Temp.dat")    
    else:
        os.remove("Products.dat")
        os.rename("Temp.dat", "Products.dat")

#**************************************MAIN MODULE*************************************
Choice = 0
while Choice != 9:
    os.system("cls")
    print("1  Add a Record")
    print("2  Print All Records")
    print("3  Search a Record by ID")
    print("4  Average Price of all Products")
    print("5  Delete a Record")
    print("6  List the discontinued products")
    print("7  List the continued products")
    print("8  List the items above 100.00")
    Choice = int(input("Enter your choice  :"))
    if Choice == 1:
        add_record()
    elif Choice == 2:
        print_all()
    elif Choice == 3:
        search_item = int(input("Enter the Product ID of the item you want to search: "))
        search(search_item)
    elif Choice == 4:
        average()
    elif Choice == 5:
        delete_item = int(input("Enter the Product ID of the item you want to delete: "))
        delete(delete_item)
    elif Choice == 9:
        break
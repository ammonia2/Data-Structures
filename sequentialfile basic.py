import pickle
import os

class Vehicle:
    VehicleID = 0
    Make = ""
    Model = 0
    Airbag = False
    Price = 0.0

def add_record():
    NewRecord = Vehicle()
    NewRecord.VehicleID = int(input("Enter Vehicle ID: "))
    NewRecord.Make = input("Enter Vehicle Make: ")
    NewRecord.Model = int(input("Enter Model(year): "))
    NewRecord.Airbag = bool(input("Does vehicle have airbag? Enter True or False: "))
    NewRecord.Price = float(input("Enter Vehicle Price: "))
    fptr1 = open("Vehicles.dat", "ab")
    fptr1.close()
    fptr1 = open("Vehicles.dat", "rb")
    fptr2 = open("Temp.dat", "wb")
    fptr1.read()
    eof = fptr1.tell()
    fptr1.seek(0)
    CurrentRecord = Vehicle()
    entered = False
    while fptr1.tell() != eof:
        CurrentRecord = pickle.load(fptr1)
        if CurrentRecord.VehicleID > NewRecord.VehicleID and entered == False:
            pickle.dump(NewRecord, fptr2)
            entered = True
        pickle.dump(CurrentRecord, fptr2)
    if entered == False:
        pickle.dump(NewRecord, fptr2)
        entered = True
    fptr1.close()
    fptr2.close()
    os.remove("Vehicles.dat")
    os.rename("Temp.dat", "Vehicles.dat")

def print_all():
    TempRecord = Vehicle()
    fptr = open("Vehicles.dat", "rb")
    fptr.read()
    eof = fptr.tell()
    fptr.seek(0)
    while fptr.tell() != eof:
        TempRecord = pickle.load(fptr)
        print("Vehicle ID : ", TempRecord.VehicleID)
        print("Make       : ", TempRecord.Make)
        print("Model      : ", TempRecord.Model)
        print("Airbag     : ", TempRecord.Airbag)
        print("Price      : ", TempRecord.Price)
        print("\n*****************************************")
    fptr.close()


def search_ByID(searchID):
    TempRecord = Vehicle()
    fptr=open("Vehicles.dat","rb")
    fptr.read()
    eof=fptr.tell()
    fptr.seek(0)
    found=False
    while fptr.tell()!=eof:
        TempRecord = pickle.load(fptr)
        if searchID == TempRecord.VehicleID:
            found = True
            print("Vehicle ID : ", TempRecord.VehicleID)
            print("Make       : ", TempRecord.Make)
            print("Model      : ", TempRecord.Model)
            print("Airbag     : ", TempRecord.Airbag)
            print("Price      : ", TempRecord.Price)
            print("\n*****************************************")
    if found==False:
        print("Not found!")
    fptr.close()


def search_ByMake(searchMake):
    TempRecord = Vehicle()
    fptr=open("Vehicles.dat","rb")
    fptr.read()
    eof=fptr.tell()
    fptr.seek(0)
    found=False
    while fptr.tell()!=eof:
        TempRecord = pickle.load(fptr)
        if searchMake == TempRecord.Make:
            found = True
            print("Vehicle ID : ", TempRecord.VehicleID)
            print("Make       : ", TempRecord.Make)
            print("Model      : ", TempRecord.Model)
            print("Airbag     : ", TempRecord.Airbag)
            print("Price      : ", TempRecord.Price)
            print("\n*****************************************")
    if found==False:
        print("Not found!")
    fptr.close()

def delete(deleteID):
    TempRecord = Vehicle()
    fptr1 = open("Vehicles.dat", "rb")
    fptr2 = open("Temp.dat", "wb")
    fptr1.read()
    eof = fptr1.tell()
    fptr1.seek(0)
    found = False
    while fptr1.tell() != eof:
        TempRecord = pickle.load(fptr1)
        if TempRecord.VehicleID == deleteID:
            found = True
        else:
            pickle.dump(TempRecord, fptr2)
    fptr1.close()
    fptr2.close()
    if found == False:
        print("Record not Found!")
        os.remove("Temp.dat")
    else:
        print("Record deleted!")
        os.remove("Vehicles.dat")
        os.rename("Temp.dat", "Vehicles.dat")

def average():
    TempRecord= Vehicle()
    fptr=open("Vehicles.dat","rb")
    fptr.read()
    eof=fptr.tell()
    fptr.seek(0)
    Count=0
    TotalPrice=0.0
    AveragePrice=0.0
    
    while fptr.tell()!=eof:
        TempRecord=pickle.load(fptr)
        TotalPrice=TempRecord.Price+TotalPrice
        Count+=1
    AveragePrice=TotalPrice/Count
    print("Average Price of all vehicles: ",AveragePrice)
    fptr.close()

def edit_ByID(vehicleID):
    fptr1 = open("Vehicles.dat", "rb")
    fptr2 = open("Temp.dat", "wb")
    fptr1.read()
    eof = fptr1.tell()
    fptr1.seek(0)
    CurrentRecord = Vehicle()
    entered = False 
    while fptr1.tell() != eof:
        CurrentRecord = pickle.load(fptr1)
        if CurrentRecord.VehicleID == vehicleID:
            NewRecord = Vehicle()
            NewRecord.VehicleID = vehicleID
            NewRecord.Make = input("Enter new Vehicle Make: ")
            NewRecord.Model = int(input("Enter new Model(year): "))
            NewRecord.Airbag = bool(input("Does new vehicle have airbag? Enter True or False: "))
            NewRecord.Price = float(input("Enter new Vehicle Price: "))
            pickle.dump(NewRecord, fptr2)
            entered = True
        else:
            pickle.dump(CurrentRecord, fptr2)
    if entered == False:
        print("Couldn't find record to edit!")
    fptr1.close()
    fptr2.close()
    os.remove("Vehicles.dat")
    os.rename("Temp.dat", "Vehicles.dat")

Choice = 0
while Choice != 8:
    os.system("cls")
    print("\n*****************************************")
    print("1  Add a Vehicle")
    print("2  Print All Vehicles")
    print("3  Search Vehicles by ID")
    print("4  Search Vehicles by Make")
    print("5  Delete Vehicles by ID")
    print("6  Calculate Average Price of All Vehicles")
    print("7  Edit Vehicles by ID")
    print("8  Quit")
    Choice = int(input("Enter your choice: "))
    if Choice == 1:
        add_record()
    elif Choice == 2:
        print_all()
    elif Choice == 3:
        search_item = int(input("Enter the Vehicle ID of the Vehicles you want to search: "))
        search_ByID(search_item)
    elif Choice == 4:
        search_item = input("Enter the Make of the Vehicles you want to search: ")
        search_ByMake(search_item)
    elif Choice == 5:
        delete_item = int(input("Enter the Vehicle ID of the vehicles you want to delete: "))
        delete(delete_item)
    elif Choice == 6:
        average()
    elif Choice == 7:
        edit_item = int(input("Enter the Vehicle ID of the vehicles you want to edit: "))
        edit_ByID(edit_item)
    elif Choice == 8:
        print("Quitting......")
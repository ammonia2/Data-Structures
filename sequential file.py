import pickle
import os

class seq_record():
    def __init__(self, index):
        self.productID = 0
        self.index = index
        self.name = "None"
        self.unit_price = 0.0
        self.discontinued = False

def record_creation(name): ## all good
    rec_file = open(name, "wb")
    for x in range(3):
        y = seq_record(x)
        pickle.dump(y, rec_file)
    eof = rec_file.tell()
    rec_file.close()
    return name

def print_record(file):  ## lesson : pickle zindabad!! ++ need to put "try: except:" here
    data = None
    rec_file = open(file, "rb")
    rec_file.seek(0)
    while True:
        try:
            data = pickle.load(rec_file)
            print(data.index, data.name)
            #if data.index == index: <--for single record print
            #    break
        except (EOFError):
            break
    rec_file.close()

def update_record(index, id, name, price, status, file):
    rec_file = open(file, "rb")
    rec_file.seek(0)
    while True:
        data = pickle.load(rec_file)
        if data.index == index:
            data.productID = id
            data.name = name
            data.unit_price = price
            data.discontinued = status
            break
    rec_file.close()

def delete_record(del_index):  #all good
    new_file = record_creation("recordc.DAT")
    #copying the desired
    new_filee, rec_file = open("recordc.DAT", "wb"), open("recordg.DAT", "rb")
    rec_file.seek(0)
    while True:
        try:
            data = pickle.load(rec_file)
            #data2 = pickle.load(new_filee)
            if data.index != del_index:
                pickle.dump(data, new_filee)
                print("transfer:",data.index)
        except (EOFError):
            break
    rec_file.close()
    new_filee.close()
    os.remove("recordg.DAT")
    os.rename("recordc.DAT", "recordg.DAT")
    
print_record(record_creation("recordg.DAT"))
update_record(2, 256, "Honey", 26.2, False, "recordg.DAT")
delete_record(1)
print_record("recordg.DAT")
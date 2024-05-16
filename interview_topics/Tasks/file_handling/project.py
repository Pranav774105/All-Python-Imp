import csv
import pandas as pd
filename = 'customer.csv'

# note: 100 rupay chi --> one time process
##fields = ['room_no', 'name', 'contact', 'bill']
##with open(filename, 'a') as fh:
##   csvwriter = csv.writer(fh)
##   csvwriter.writerow(fields)


total_rooms = [101,102,103,104]
available_rooms = []
allocated_rooms = []


def find_index():
    room_no = input('Enter room no here')
    with open(filename, 'r') as fh:
        csvreader = csv.reader(fh)
        fields = next(csvreader)
        index = 0
        for records in csvreader:
            if records:
                if records[0] == room_no:
                    return index
                index += 1
        


def check_rooms():
    global available_rooms, allocated_rooms
    with open(filename,'r') as fh:
        csvreader = csv.reader(fh)
        fields = next(csvreader)
        allocated_rooms = [int(records[0]) for records in csvreader if records]
        available_rooms = list(set(total_rooms)^set(allocated_rooms))



def new_customer():
    if available_rooms:
        room_no = available_rooms.pop()
        name = input('Enter name here')
        contact = int(input('contact'))
        days = int(input('Enter number of stays'))
        bill = days*800
        fields = [room_no, name, contact, bill]
        with open(filename, 'a') as fh:
           csvwriter = csv.writer(fh)
           csvwriter.writerow(fields)
        print(f'Hi { name } here is your key of room no { room_no }')
    else:
        print('no rooms available')


def show_all_cust():
    with open(filename, 'r') as fh:
        csvreader = csv.reader(fh)
        fields = next(csvreader)
        for records in csvreader:
            if records:
                print(f'{records[1]} rahtoy room no {records[0]} ani tych attapryantch bill zalay {records[3]}')
    

def update():
    index = find_index()      
    ch = int(input('What do you want to update\n'\
                   '1.Name\n'\
                   '2.contact\n'))   
    match ch:
        case 1:
            field = 'name'
            change = input('Enter new name')
        case 2:
            field = 'contact'
            change = int(input('Enter new contact'))
            
    df = pd.read_csv(filename)  
    df.loc[index, field] = change
    df.to_csv(filename, index=False)
    print('Updated')


def delete():
    index1 = find_index()
    df = pd.read_csv(filename)
    df = df.drop(df.index[index1])
    df.to_csv(filename, index=False)
    print('deleted')





while True:
    ch = int(input('1.new Customer\n'\
                   '2.Show All customers\n'\
                   '3.Update Contact\n'\
                   '4.Delete\n'))
    match ch:
        case 1:
            check_rooms()
            new_customer()
        case 2:
            show_all_cust()
        case 3:
            update()
        case 4:
            delete()
        


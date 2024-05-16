## Hotel Management System

class Hotel:
    def __init__(self, name, room_no, mob_no, room_bill=0, resto_bill=0, gaming_bill=0, laundry_bill=0):
        self.name = name
        self.mob_no = mob_no
        self.room_no = room_no
        self.room_bill = room_bill
        self.gaming_bill = gaming_bill
        self.laundry_bill = laundry_bill
        self.resto_bill = resto_bill

    def __str__(self):
        return f'Customer name = {self.name}\n'\
               f'Mobile Number = {self.mob_no}\n'\
               f'Room Number = {self.room_no}\n'\
               f'Room Bill = {self.room_bill}\n'\
               f'Gaming Bill = {self.gaming_bill}\n'\
               f'Laundry Bill = {self.laundry_bill}\n'\
               f'Resto_bill = {self.resto_bill}\n'

available_room = [101, 102, 103]
allocated_rooms = []
customer_list = []

def new_customer():
    print('*********Welcome*********')
    
    if available_room:
        room_no = available_room.pop()
        allocated_rooms.append(room_no)
        name = input('Enter your name here')
        mobile_no = int(input('Enter mobile number here'))
        number_of_days = int(input('Enter no.of days'))     
        customer = Hotel(name, room_no, mobile_no, room_bill=number_of_days*800)
        print(f'Hi {name}, here is your key of room no {room_no}')
        customer_list.append(customer)
    else:
        print('Sorry no rooms are available')
        
    

def existing_customer():
    ch = int(input(('****** SERVICES ********\n'\
                    '1.RESTAURANT\n')))
    customer_room_no = int(input('Plz Enter your room number here'))
    for i in customer_list:
        if i.room_no == customer_room_no:
             break
    cust = i
    
    if ch == 1:
        ch1 = int(input('***Menu***\n'\
                          '1.Tea    --> 10rs\n'\
                          '2.Lunch  --> 120rs\n'\
                          '3.Exit'))
        if ch1 == 1:
             quantity = int(input('How many number of teas'))
             cust.resto_bill += quantity*10
             
        elif ch1 == 2:
             quantity = int(input('How many number of lunch'))
             cust.resto_bill += quantity*120
             
        elif ch1 == 3:
            print('Exit from restro')
          
                    
            
def customer_details():
    for i in customer_list:
        print(i)


def billing_checkout():
    customer_room_no = int(input('Plz Enter your room number here'))
    for i in customer_list:
        if i.room_no == customer_room_no:
             break
    cust = i
    total_bill = cust.room_bill + cust.gaming_bill + cust.laundry_bill + cust.resto_bill
    print(f'Your total bill is {total_bill}')
    allocated_rooms.remove(customer_room_no)
    available_room.append(customer_room_no)
    customer_list.remove(i)
    print('Thanks for visting our Hotel')

while True:
    ch = int(input('Please Enter Your Choice \n'\
          '1. New Customer \n'\
          '2. Existing Customer\n'\
          '3. Customer Details \n'\
          '4. Billing and Checkout'
          ))
    match ch:
        case 1:
            new_customer()
        case 2:
            existing_customer()
        case 3:
            customer_details()
        case 4:
            billing_checkout()
        case _:
            pass





from datetime import date, timedelta


todays_date = date.today()

print ("initial_date", todays_date)
print('*'*30)


future_date_after_2days = todays_date + timedelta(days = 2)

print('future_date_after_2days:', future_date_after_2days)



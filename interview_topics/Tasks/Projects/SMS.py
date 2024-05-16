class Student:
    def __init__(self, r, fn, ln, sub, m):
        self.roll = r
        self.fname = fn
        self.lname = ln
        self.subject = sub
        self.marks = m
    def __str__(self):
        return f'\t  ****Information of Student is:****\n\
               Roll number is : {self.roll}\n\
               First Name is:   {self.fname}\n\
               Last Name is:    {self.lname}\n\
               Subject is:      {self.subject}\n\
               Marks are:       {self.marks}\n\
               {"_"*20}'
l = []
x = 1
#################################   Main Menu  ###########################################
while True:
    print('\t***Main Menu***\n\
          1.Add Student\n\
          2.show Student Info\n\
          3.update Student Info\n\
          4.Delete Info\n\
          5.Exit\n'
          )
    ch = int(input('--Enter Your Choice--\n'))
#################################   Create  ###########################################
    if ch==1:
        ch1 = int(input('How Many Students You wants to add'))
        
        for i in range(1,ch1+1):
            
            rn = x
            x = x + 1 
            fn = input('Enter First Name Here')
            ln = input('Enter last Name Here')
            sub = input('Enter Subject Here')
            marks = float(input('Enter marks Here'))
            print(f'Hi, {fn} Your allocated with roll  {[rn]}')
            s = Student(rn, fn, ln, sub, marks)
            l.append(s)
            

#################################   Retrive  ###########################################
    elif ch==2:
        if bool(l) == False:
            print('No data To display Please Add Students First')
        else:
            while True:
                print('\t***Menu***\n\
                  1.Show all Student Info\n\
                  2.Show Particular Student Info\n\
                  3.Back to Main Menu\n'
                  )
                
                ch2 = int(input('--Enter Your Choice--\n'))
                if ch2 == 1:
                    for i in l:
                        print(i)
                elif ch2 == 2:
                    ch3 = int(input('Enter Roll Number Here'))
                    for i in l:
                        if i.roll == ch3:
                            print(i)
                            break
                    else:
                        print('Please Enter valid Roll Number')
                elif ch2 == 3:
                    break
#################################   Update  ###########################################              
    elif ch==3:
        if bool(l) == False:
            print('No data To update Please Add Students First')
        else:
                
                    ch4 = int(input('Enter Students Roll to update Info\n'))
                    for i in l:
                        if i.roll == ch4:
                            while True:
                                print('**What do you wants To Update**\n\
                                      1.First name\n\
                                      2.Last name\n\
                                      3.Subject Name\n\
                                      4.Marks\n\
                                      5.Back to Main menu')
                                ch5 = int(input('Enter Your Choice'))
                                if ch5 == 1:
                                    fn = input(f'Hi, {i.fname} Enter Your first Name that you wants to Update')
                                    i.fname = fn
                                    print('Updated')
                                elif ch5 == 2:
                                    ln = input(f'Hi, {i.fname} Enter Your Last Name that you wants to Update')
                                    i.lname = ln
                                    print('Updated')
                                elif ch5 == 3:
                                    s = input(f'Hi, {i.fname} Enter Subject Name that you wants to Update')
                                    i.subject = s
                                    print('Updated')
                                elif ch5 == 4:
                                    m = input(f'Hi, {i.fname} Enter Marks that you wants to Update')
                                    i.marks = m
                                    print('Updated')
                                elif ch5 == 5:
                                    break
                                else:
                                    print('Please Enter Valid Input')
                        
                            
                                
                    else:
                        print('Please Enter valid Roll Number')
#################################   Delete  ###########################################
    elif ch==4:
        if bool(l) == False:
            print('No data To Delete')
        else:
            while True:
                print('**What do you wants To Delete**\n\
                      1.All Records\n\
                      2.Single Record\n\
                      3.Back to main Menu')
                ch6 = int(input('Enter Your Choice'))
                if ch6 == 1:
                    l.clear()
                    print('All Records Deleted Successsfully!!!')
                    break
                elif ch6 == 2:
                    if bool(l)== False:
                        print('No data To delete')
                    elif bool(l)== True:
                        ch7 = input('Enter Roll You wants to delete info of')
                        for i in l:
                            if ch7 == i.roll:
                                l.remove(i)
                                print(f'Record of roll{i.roll}deleted')
                                break
                                
                        else:
                            print('Please Enter Valid Roll Number')
                elif ch6 == 3:
                    break
                else :
                    print('Please Enter Valid Number')
                
            
            
    elif ch==5:
        print('Exited')
        break
        
    else:
        print('Please Enter Valid Number')



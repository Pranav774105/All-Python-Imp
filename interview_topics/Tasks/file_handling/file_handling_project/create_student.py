from student import Student
l=[]

def foo():
    num = int(input('Enter number of student u want to add'))
    for i in range(1,num+1):
        
        ch2 = input('Enter name here')
        ch3 = float(input('Enter marks here'))
        s=Student()
        s.roll=i
        s.name=ch2
        s.marks=ch3
        l.append(s)
        

    fh=open('C:/Users/Ajay/Desktop/studentdata.txt','w')
    fh.write('Roll\tName\tmarks\n')
    
    for i in range(num):
        fh.write(f'{l[i].roll}\t{l[i].name}\t{l[i].marks}\n')
        
    fh.close()


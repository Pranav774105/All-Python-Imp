##
##while True:
##    ch=int(input('1.feedback 2.exit 3.checkfeedback'))
##    if ch==1:
##        
##        name=input('Enter your name==')
##        n1=(f'{name}.txt')
##        print(n1)
##        import os
##      
##        slist=os.listdir(r'C:\Users\HP\Desktop\feedback project')
##        print(slist)
##        if n1 in slist:
##            print('this name alrady given feedback ')
##        else:
##
##            wfb=input('Enter your feedback=')
##            with open(n1,'x') as feed:
##                wf=feed.write(wfb)
##        print('thanks for giving feedback')
##    elif ch==2:
##        break
##    elif ch==3:
##        import os
##      
##        slist=os.listdir(r'C:\Users\HP\Desktop\feedback project')
##        print(slist)
##        check=input('Enter name of student=')
##        c1=f'{check}.txt'
##        print(c1)
##        if c1 not in slist:
##            print('this student not given feedback')
##            
##        else:
##        
##            print('Feedback done by',check)
##            with open(f'C:/Users/HP/Desktop/{c1}') as fo:
##                rf=fo.read()
##                print(rf)




##print(len(r'\nemo'))
##fh = open(r'C:\Users\HP\Desktop\python_topics\File Handling\demo1.txt')


##with open(r'C:\Users\HP\Desktop\python_topics\File Handling\demo1.txt') as fh:
##    fh.seek(2)
##    fh.tell()

##    print(type(fh))







##try:
##    print(fh.write('Hello'))
##finally:
##    fh.close()
##    print(fh.closed)















    
##print(fh.write('Hello'))
##print(fh.closed)
##fh.close()
##print(fh.closed)

##if 'a' in di:
##    print('a is present in dict')
##else:
##    print('a is present in dict')


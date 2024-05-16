class Course:

    def __init__(self,cid,cname,cfees,cduration):
        self.cid=cid
        self.cname=cname
        self.cfees=cfees
        self.cduration=cduration        
        

class Batch:

    def __init__(self,bid,bname,batchtiming,objcourse):
        self.bid=bid
        self.bname=bname
        self.batchtiming=batchtiming
        self.objcourse=objcourse        
        

class Student:

    def __init__(self,rollno,name,city,objbatch):
        self.rollno=rollno
        self.name=name
        self.city=city
        self.objbatch=objbatch

        
class ZeroMinusValueError(Exception):
    def __init__(self,msg):
        self.msg=msg
        
clist=[]
blist=[]
slist=[]
cid_list=[]
bid_list=[]
rollno_list=[]


print("--SELECT--\n1)ADD COURSE\t2)ADD BATCH\t3)ADD STUDENT\t4)SHOW ALL\t5)SHOW COURSE\t6)SHOW BATCH\t7)SHOW STUDENT\n8)UPDATE COURSE\t9)UPDATE BATCH\t10)UPDATE STUDENT\t11)DELETE COURSE\t12)DELETE BATCH\t13)DELETE STUDENT\n14)Exit")

while True:
    
    try:
        ch=int(input("Enter your choice:-"))
    
#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>ADD COURSE<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        if ch==1:
            n=int(input("Enter how many course do you want to add:-"))
            if n<=0:
                raise ZeroMinusValueError("Please do not enter minus value or zero value")
            i=0
            while i<n:
                cid=input("Enter Course ID:-")
                if cid in cid_list:
                    print("Course ID already exist")
                else:
                    c1=Course(cid,input("Enter Course Name:-"),input("Enter Course Fees:-"),input("Enter Course Duration:-"))
                    clist.append(c1)
                    cid_list.append(c1.cid)
                    i=i+1  #i+=1
                    
#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>ADD BATCH<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#            

        elif ch==2:
            if clist==[]:
                print("Add Course Information First")
                
            else:
                n=int(input("Enter how many batch do you want to add:-"))
                if n<=0:
                    raise ZeroMinusValueError("Please do not enter minus value or zero value")
                i=0
                while i<n:
                    c_choice=input("Enter Course ID:-")
                    if c_choice in cid_list:
                        bid=input("Enter Batch ID:-")
                        for course in clist:
                            if c_choice==course.cid:
                                if bid in bid_list:
                                    print("Batch ID already exist")
                                else:
                                    b1=Batch(bid,input("Enter Batch Name:-"),input("Enter Batch Timing:-"),course)
                                    blist.append(b1)
                                    bid_list.append(b1.bid)
                                    i=i+1  #i+=1
                    else:
                        print("Enter valid Course ID")
                        
#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>ADD STUDENT<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==3:
            if blist==[]:
                print("Add Batch Information First")
                
            else:
                print("----AVAILABLE BATCH INFORMATION----")
                for batch in blist:
                        print(batch.bid,':',batch.bname,':',batch.objcourse.cname)
                        
                n=int(input("Enter how many student do you want to add:-"))
                if n<=0:
                    raise ZeroMinusValueError("Please do not enter minus value or zero value")
                i=0
                while i<n:
                    c_choice = input("Enter Batch ID:-")
                    if c_choice in bid_list:
                        rollno=int(input("Enter Student Rollno:-"))
                        for batch in blist:
                           if c_choice==batch.bid:
                               if rollno in rollno_list:
                                   print("Student Rollno already exist")
                               else:
                                    s1=Student(rollno,input("Enter Student Name:-"),input("Enter Student City:-"),batch)
                                    slist.append(s1)
                                    rollno_list.append(s1.rollno)
                                    i=i+1  #i+=1
                                    
                    else:
                        print("Enter valid Batch ID")

#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>SHOW ALL<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#                    

        elif ch==4:
            if slist==[]:
                print("Add Student Information First")
                
            else:
                print("\t\t\t----AVAILABLE STUDENT INFORMATION----")
                for student in slist:
                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                        
#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>SHOW COURSE<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#        
                    
        elif ch==5:
            if clist==[]:
                print('Add Course Information First')
                
            else:
                while True:
                    print('1)All Courses\t2)Specified Course Information\t3)Exit')
                    
                    ch=int(input('Enter your choice for show course information:-'))
                    
                    if ch==1:
                        print("\t\t\t----AVAILABLE COURSE INFORMATION----")
                        for course in clist:
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)          
                                   
                    elif ch==2:
                        cid=input("Enter which Course ID details do you want to show:-")
                        if cid in cid_list:
                            print("\t\t\t-----SPECIFIED COURSE INFORMATION-----")
                            for course in clist:
                                if cid==course.cid:
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)           
                        else:
                            print("Enter valid Course ID")

                    elif ch==3:
                        break

                    else:
                        print("Enter valid choice for show course information")
                        
#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>SHOW BATCH<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==6:
            if blist==[]:
                print("Add Batch Information First")
                
            else:
                while True:
                    print("1)All Batches\t2)Specified Batch Information\t3)Exit")
                    ch=int(input("Enter your choice for show batch information:-"))
                        
                    if ch==1:
                        print("\t\t\t----AVAILABLE BATCH INFORMATION----")
                        for batch in blist:
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                    elif ch==2:
                        bid=input("Enter which Batch ID details do you want to show:-")
                        if bid in bid_list:
                            print("\t\t\t-----SPECIFIED BATCH INFORMATION-----")
                            for batch in blist:
                                if bid==batch.bid:
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)

                        else:
                            print("Enter valid Batch ID")

                    elif ch==3:
                        break
                            
                    else:
                        print("Enter valid choice for show batch information")
                    
#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>SHOW STUDENT<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==7:
            if slist==[]:
                print("Add Student Information First")
                
            else:
                while True:
                    print("1)All Students\t2)Specified Student Information\t3)Exit")
                    ch=int(input("Enter your choice for show student information:-"))
                        
                    if ch==1:
                        print("\t\t\t----AVAILABLE STUDENT INFORMATION----")
                        for student in slist:
                            print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                            
                    elif ch==2:
                        rollno=int(input("Enter which Rollno Student details do you want to show:-"))
                        if rollno in rollno_list:
                            print("\t\t\t-----SPECIFIED STUDENT INFORMATION-----")
                            for student in slist:
                                if rollno==student.rollno:
                                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                                              
                        else:
                            print("Enter valid Student Rollno")

                    elif ch==3:
                        break
                            
                    else:
                        print("Enter valid choice for show student information")

#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>UPDATE COURSE<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==8:
            if clist==[]:
                print("Add Course Information First")
                
            else:
                while True:
                    print("1)All Courses\t2)Update Specified Course Name\t3)Update specified Course Fees\n4)Update specified Course Duration\t5)Update All Information For Specified Course\t6)Exit")
                    ch=int(input("Enter your choice for update course information:-"))

                    if ch==1:
                        print("\t\t\t----AVAILABLE COURSE INFORMATION----")
                        for course in clist:
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)

                    elif ch==2:
                        cid=input("Enter which Course ID their Course Name do you want to update:-")
                        if cid in cid_list:
                            print("\t\t\t----SPECIFIED COURSE INFORMATION----")
                            for course in clist:
                                if cid==course.cid:
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    cname=input("Enter New Course Name:-")
                                    course.cname=cname
                                    print("\t\t\t--UPDATED SPECIFIED COURSE INFORMATION--")
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Course ID")

                    elif ch==3:
                        cid=input("Enter which Course ID their Course Fees do you want to update:-")
                        if cid in cid_list:
                            print("\t\t\t----SPECIFIED COURSE INFORMATION----")
                            for course in clist:
                                if cid==course.cid:
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    cfees=input("Enter New Course Fees:-")
                                    course.cfees=cfees
                                    print("\t\t\t--UPDATED SPECIFIED COURSE INFORMATION--")
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Course ID")

                    elif ch==4:
                        cid=input("Enter which Course ID their Course Duration do you want to update:-")
                        if cid in cid_list:
                            print("\t\t\t----SPECIFIED COURSE INFORMATION----")
                            for course in clist:
                                if cid==course.cid:
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    cduration=input("Enter New Course Duration:-")
                                    course.cduration=cduration
                                    print("\t\t\t--UPDATED SPECIFIED COURSE INFORMATION--")
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Course ID")

                    elif ch==5:
                        cid=input("Enter which Course ID all information do you want to update:-")
                        if cid in cid_list:
                            print("\t\t\t----SPECIFIED COURSE INFORMATION----")
                            for course in clist:
                                if cid==course.cid:
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    cname=input("Enter New Course Name:-")
                                    cfees=input("Enter New Course Fees:-")
                                    cduration=input("Enter New Course Duration:-")
                                    course.cname=cname
                                    course.cfees=cfees
                                    course.cduration=cduration
                                    print("\t\t\t--UPDATED SPECIFIED COURSE INFORMATION--")
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Course ID")

                    elif ch==6:
                        break
                            
                    else:
                        print("Enter valid choice for update course information")
                            
#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>UPDATE BATCH<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==9:
            if blist==[]:
                print("Add Batch Information First")
                
            else:
                while True:
                    print("1)All Batches\t2)Update Specified Batch Name\t3)Update Specified Batch Timing\n4)Update All Information For Specified Batch\t5)Exit")
                    ch=int(input("Enter your choice for update batch information:-"))

                    if ch==1:
                        print("\t\t\t----AVAILABLE BATCH INFORMATION----")
                        for batch in blist:
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)

                    elif ch==2:
                        bid=input("Enter which Batch ID their Batch Name do you want to update:-")
                        if bid in bid_list:
                            print("\t\t\t----SPECIFIED BATCH INFORMATION----")    
                            for batch in blist:
                                if bid==batch.bid: 
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    bname=input("Enter New Batch Name:-")
                                    batch.bname=bname
                                    print("\t\t\t--UPDATED SPECIFIED BATCH INFORMATION--")
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Batch ID")

                    elif ch==3:
                        bid=input("Enter which Batch ID their Batch Timing do you want to update:-")
                        if bid in bid_list:
                            print("\t\t\t----SPECIFIED BATCH INFORMATION----")   
                            for batch in blist:
                                if bid==batch.bid:
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    batchtiming=input("Enter New Batch Timing:-")
                                    batch.batchtiming=batchtiming
                                    print("\t\t\t--UPDATED SPECIFIED BATCH INFORMATION--")
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Batch ID")

                    elif ch==4:
                        bid=input("Enter which Batch ID all information do you want to update:-")
                        if bid in bid_list:
                            print("\t\t\t----SPECIFIED BATCH INFORMATION----")
                            for batch in blist:
                                if bid==batch.bid:
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    bname=input("Enter New Batch Name:-")
                                    batchtiming=input("Enter New Batch Timing:-")
                                    batch.bname=bname
                                    batch.batchtiming=batchtiming
                                    print("\t\t--UPDATED SPECIFIED BATCH INFORMATION--")
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Batch ID")

                    elif ch==5:
                        break   
                            
                    else:
                        print("Enter valid choice for update batch information")

#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>UPDATE STUDENT<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==10:
            if slist==[]:
                print("Add Student Information First")
                
            else:
                while True:
                    print("1)All Students\t2)Update Specified Student Name\t3)Update specified Student City\n4)Update All Information For Specified Student\t5)Exit")
                    ch=int(input("Enter your choice for update student information:-"))

                    if ch==1:
                        print("\t\t----AVAILABLE STUDENT INFORMATION----")
                        for student in slist:
                            print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)

                    elif ch==2:
                        rollno=int(input("Enter which Student Rollno their Student Name do you want to update:-"))
                        if rollno in rollno_list:
                            print("\t\t---SPECIFIED STUDENT INFORMATION---")
                            for student in slist:
                                if rollno==student.rollno:
                                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    name=input("Enter New Name:-")
                                    student.name=name
                                    print("\t\t--UPDATED SPECIFIED STUDENT INFORMATION--")
                                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Student Rollno")

                    elif ch==3:
                        rollno=int(input("Enter which Student Rollno their Student City do you want to update:-"))
                        if rollno in rollno_list:
                            print("\t\t---SPECIFIED STUDENT INFORMATION---")  
                            for student in slist:
                                if rollno==student.rollno:   
                                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    city=input("Enter New City:-")
                                    student.city=city
                                    print("\t\t--UPDATED SPECIFIED STUDENT INFORMATION--")
                                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Student Rollno")
                            
                    elif ch==4:
                        rollno=int(input("Enter which Rollno Student all information do you want to update:-"))
                        if rollno in rollno_list:
                            print("\t\t---SPECIFIED STUDENT INFORMATION---")
                            for student in slist:
                                if rollno==student.rollno:
                                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                                    name=input("Enter New Name:-")
                                    city=input("Enter New City:-")
                                    student.name=name
                                    student.city=city
                                    print("\t\t--UPDATED SPECIFIED STUDENT INFORMATION--")
                                    print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                    print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                    print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        else:
                            print("Enter valid Student Rollno")

                    elif ch==5:
                        break
                            
                    else:
                        print("Enter valid choice for update student information")

#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>DELETE COURSE<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#
                    
        elif ch==11:
            if clist==[]:
                print("Add Course Information First")
                
            else:
                while True:
                    print("1)All Courses\t2)Delete Specified Course In List And Course ID In List\t3)Delete All Courses List And Course ID List\n4)Exit")
                    ch=int(input("Enter your choice for delete course information:-"))

                    if ch==1:
                        print("\t\t\t----AVAILABLE COURSE INFORMATION LIST----")
                        for course in clist:
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)

                    elif ch==2:
                        print("\t\t\t----AVAILABLE COURSE INFORMATION LIST----")
                        for course in clist:
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        print("\t\t\t----AVAILABLE COURSE ID INFORMATION LIST----")
                        for cid in cid_list:
                            print(cid) 
                        cid=input("Enter which Course ID information do you want to delete:-")
                        if cid in cid_list:
                            for course in clist:
                                if cid==course.cid:
                                    clist.remove(course)
                                    cid_list.remove(cid)
                            print("\t\t\t-----REST COURSE INFORMATION LIST-----")
                            for course in clist:
                                print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                            print("\t\t\t-----REST COURSE ID INFORMATION LIST-----")
                            for cid in cid_list:
                                print(cid)
                        else:
                            print("Enter valid Course ID")
                            
                    elif ch==3:
                        print("---AFTER DELETE ALL COURSE INFORMATION LIST---")
                        i=0
                        n=len(clist)
                        while i<n:
                            clist.remove(clist[0])
                            i=i+1
                        print(clist)
                        print("---AFTER DELETE ALL COURSE ID INFORMATION LIST---")
                        i=0
                        n=len(cid_list)
                        while i<n:
                            cid_list.remove(cid_list[0])
                            i=i+1
                        print(cid_list)

                    elif ch==4:
                        break

                    else:
                        print("Enter valid choice for delete course information")

#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>DELETE BATCH<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==12:
            if blist==[]:
                print("Add Batch Information First")
                
            else:
                while True:
                    print("1)All Batches\t2)Delete Specified Batch In List And Batch ID In List\t3)Delete All Batches List And Batch ID List\n4)Exit")
                    ch=int(input("Enter your choice for delete batch information:-"))

                    if ch==1:
                        print("\t\t\t----AVAILABLE BATCH INFORMATION LIST----")
                        for batch in blist:
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)

                    elif ch==2:
                        print("\t\t\t----AVAILABLE BATCH INFORMATION LIST----")
                        for batch in blist:
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        print("\t\t\t----AVAILABLE BATCH ID INFORMATION LIST----")
                        for bid in bid_list:
                            print(bid)   
                        bid=input("Enter which Batch ID information do you want to delete:")
                        if bid in bid_list:
                            for batch in blist:
                                if bid==batch.bid:
                                    blist.remove(batch)
                                    bid_list.remove(bid)
                            print("\t\t----REST BATCH INFORMATION LIST----")
                            for batch in blist:
                                print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)   
                            print("\t\t\t-----REST BATCH ID INFORMATION LIST-----")
                            for bid in bid_list:
                                print(bid)    
                        else:
                            print("Enter valid Batch ID")

                    elif ch==3:
                        print("---AFTER DELETE ALL BATCH INFORMATION LIST---")
                        i=0
                        n=len(blist)
                        while i<n:
                            blist.remove(blist[0])
                            i=i+1
                        print(blist)
                        print("---AFTER DELETE ALL BATCH ID INFORMATION LIST---")
                        i=0
                        n=len(bid_list)
                        while i<n:
                            bid_list.remove(bid_list[0])
                            i=i+1
                        print(bid_list)

                    elif ch==4:
                        break
                            
                    else:
                        print("Enter valid choice for delete batch information")

#=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>=>DELETE STUDENT<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=<=#

        elif ch==13:
            if slist==[]:
                print("Add Student Information First")
                
            else:
                while True:
                    print("1)All Students\t2)Delete Specified Student In List And Rollno In List\t3)Delete All Student List And Rollno List\n4)Exit")
                    ch=int(input("Enter your choice for delete student information:-"))

                    if ch==1:
                        print("\t\t\t----AVAILABLE STUDENT INFORMATION LIST----")
                        for student in slist:
                            print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)

                    elif ch==2:
                        print("\t\t\t----AVAILABLE STUDENT INFORMATION LIST----")
                        for student in slist:
                            print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                            print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                            print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)
                        print("\t\t\t----AVAILABLE ROLLNO INFORMATION LIST----")
                        for rollno in rollno_list:
                            print(rollno) 
                        rollno=int(input("Enter which rollno student information do you want to delete:-"))
                        if rollno in rollno_list:
                            for student in slist:
                                if rollno==student.rollno:
                                    slist.remove(student)
                                    rollno_list.remove(rollno)
                            print("\t\t----REST STUDENT INFORMATION LIST----")
                            for student in slist:
                                print("\t\t\t----STUDENT INFORMATION----\nSTUDENT_ROLLNO:-",student.rollno,"\t\tSTUDENT_NAME:-",student.name,"\t\tSTUDENT_CITY:-",student.city)
                                print("\t\t\t-----BATCH INFORMATION-----\nBATCH_ID:-",student.objbatch.bid,"\t\tBATCH_NAME:-",student.objbatch.bname,"\t\tBATCH_TIMING:-",student.objbatch.batchtiming)
                                print("\t\t\t-----COURSE INFORMATION-----\nCOURSE_ID:-",student.objbatch.objcourse.cid,"\t\tCOURSE_NAME:-",student.objbatch.objcourse.cname,"\t\tCOURSE_FEES:-",student.objbatch.objcourse.cfees,"\t\tCOURSE_DURATION:-",student.objbatch.objcourse.cduration)      
                            print("\t\t\t-----REST STUDENT ROLLNO INFORMATION LIST-----")
                            for rollno in rollno_list:
                                print(rollno)  
                        else:
                            print("Enter valid Rollno")

                    elif ch==3:
                        print("---AFTER DELETE ALL STUDENT INFORMATION LIST---")
                        i=0
                        n=len(slist)
                        while i<n:
                            slist.remove(slist[0])
                            i=i+1
                        print(slist)
                        print("---AFTER DELETE ALL ROLLNO INFORMATION LIST---")
                        i=0
                        n=len(rollno_list)
                        while i<n:
                            rollno_list.remove(rollno_list[0])
                            i=i+1
                        print(rollno_list)

                    elif ch==4:
                        break

                    else:
                        print("Enter valid choice for delete student information")


        elif ch==14:
            break
                            
    except ZeroMinusValueError as e:
        print(e)
        
    except:
        print("Please Enter Correct Value")

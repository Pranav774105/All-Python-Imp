##import csv
##filename = "demo.csv"

##fields = ['Name', 'Branch', 'Year', 'CGPA']
##rows = [
##        ['Nikhil', 'COE', '0' , '0'],
##	['Sanchit', 'COE', '2', '9.1'],
##	['Aditya', 'IT', '2', '9.3'],
##	['Sagar', 'SE', '1', '9.5'],
##	['Prateek', 'MCE', '3', '7.8'],
##	['Sahil', 'EP', '2', '9.1']
##]
##
##with open(filename, 'w') as csvfile:
##        print(help(csv.writer))
##        csvwriter = csv.writer(csvfile)
##        csvwriter.writerow(fields)
##        csvwriter.writerows(rows)



# Retrival


##fields = []
##rows = []
##
##with open(filename, 'r') as csvfile:
##	csvreader = csv.reader(csvfile)
##	fields = next(csvreader)
##	for row in csvreader:
##		rows.append(row)
##
##for i in fields:
##	print(i)
##print('rows', '*'*30)
##
##for i in rows:
##    if i:
##        print(i)




#update


##import pandas as pd 
##df = pd.read_csv(filename)  
##df.loc[3, 'Name'] = 'sagar sir bag dya bag dya'
##
##df.to_csv(filename, index=False) 






##delete

##
##import pandas as pd
##df = pd.read_csv(filename)
##df = df.drop(df.index[3])
##df.to_csv(filename, index=False)























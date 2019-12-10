import csv
import pandas as pd
import os
# path=r'case.csv'
def csvdata(path,a,b):    
    with open(path) as csvfile:
        rows=csv.reader(csvfile)
    #     for row in rows:
    #         print(row)
    #     print(type(rows))
#         print(rows)
        return(list(rows)[a][b])
def writeCsv():   
    file = os.getcwd() + '\\1.csv'    
#     data = pd.DataFrame({'a':[1, 2, 3], 'b': [4, 5, 6]})  
#     data=pd.DataFrame(['a'],['b'])
#     data.to_csv(file, index=False) 
# #     
#     data2=pd.DataFrame({'result':[7,8,9]})
#     data2.to_csv(file,index=False,mode='a+',header=False)
    
    out=open(file,'a',newline='')
    csv_writer = csv.writer(out, dialect='excel')
    csv_writer.writerow(['result'])

if __name__=='__main__':
    path=r'case.csv'
#     print(csvdata(path,1,2))
    writeCsv()
      
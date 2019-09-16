import csv

# path=r'case.csv'
def csvdata(path,a,b):    
    with open(path,newline='') as csvfile:
        rows=csv.reader(csvfile)
    #     for row in rows:
    #         print(row)
    #     print(type(rows))
        print(rows)
        return(list(rows)[a][b])

if __name__=='__main__':
    path=r'case.csv'
    print(csvdata(path,2,2))
        
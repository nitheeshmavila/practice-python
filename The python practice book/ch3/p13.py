'''
Problem 13: Write a program csv2xls.py that reads a csv file and exports it as Excel file. The prigram should take two arguments. The name of the csv file to read as first argument and the name of the Excel file to write as the second argument.
'''
import tablib

def csv2xls(csv, excel):
    data = tablib.Dataset()
    for line in open(csv):
        i = 1
        for d in line.split(','):
             data.append([d, i])
             i += 1
   
    f =  open(excel, 'wb') 
    f.write(data.xls)



def main():
    if len(sys.argv) == 3:
        csv2xls(sys.argv[1], sys.argv[2])
    else:
        print('invalid usage')
        print('usage : p13.py <csv file name> <excel file name>')
if __name__ == '__main__':
    main()
 

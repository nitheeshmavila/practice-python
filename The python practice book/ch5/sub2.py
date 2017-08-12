                    count += 1
        else:
            getCount(p)
     return count       

def main():
    print('Total no of lines inside the python files in the directory with excluding comment and blank lines %s : %d'%(sys.argv[1],getCount(sys.argv[1]))) 
    
if __name__ == '__main__':
    main()

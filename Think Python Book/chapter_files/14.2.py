"""Exercise 14.2. Write a function called sed that takes as arguments a pattern string, a replacement
string, and two filenames; it should read the first file and write the contents into the second file
(creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced
with the replacement string.
If an error occurs while opening, reading, writing or closing files, your program should catch the
exception, print an error message, and exit"""


def sed(pattern,replacement,file1,file2):
  try:
    f1=open(file1,'r')
    f2=open(file2,'w')
    for line in f1:
      line=line.replace(pattern,replacement)
      f2.write(line)
    f1.close()
    f2.close()
  except:
    print("something went wrong \n try again")

sed(' programing','python','input.txt','output.txt')

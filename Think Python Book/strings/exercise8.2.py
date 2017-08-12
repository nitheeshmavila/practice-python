'''
Exercise 8.2
-------------
'''

prefixes = 'jklmnopq'
def word():
    for i in prefixes:
        if (i == 'o') or (i == 'q'):
            suffix = "uack"
            
        else:
            suffix = 'ack'
        print(i + suffix)
word()

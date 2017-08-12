'''
please run this in Python3

author : Nitheesh M.N

Question 2 : Palindrome
'''
def palindrome(s):
	''' This function returns True if the string is palindrome 
	    returns Flase otherwise '''	
	return s[::-1] == s

def main():
	s = input('enter a string\n')
	print(palindrome(s))

if __name__ == '__main__':
	main()


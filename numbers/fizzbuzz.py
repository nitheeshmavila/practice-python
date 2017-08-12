'''
Please run this code in Python3


QUESTION 1 : FIZZ BUZZ

author : NIthesh MN

'''


def fizzbuzz(n):
	'''This function takes an integer n ( 0 < n < 2 * 10 ^ 5) 
	   and print FizzBuzz if i (1<=i<=n)
	   print Fizz if i is a multiple of 3 but not 5 
	   print Buzz if i is a mutiple of 5 but not 3 
	   print i otherwise '''

	fiveList = [] # contains multiple of 5
	threeList = [] # contain multiple of 3
	for i in range(1, n+1):	
		if i % 3 == 0:
			threeList.append(i)			
		if i % 5 == 0:
			fiveList.append(i)

		if i in threeList and i in fiveList :
			print('FizzBuzz')
		elif i in threeList and (i not in fiveList):
			print('Fizz')
		elif i in fiveList and (i not in threeList):
			print('Buzz') 
		else:
			print(i)

def main():
	n = input('enter an integer\n')
	if int(n) > 0 and int(n) < 2 * (10**5):
		fizzbuzz(int(n))

if __name__ == '__main__':
	main()

		

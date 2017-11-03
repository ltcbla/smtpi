
while True:
	try:
		n1 	= input('Insert number: ')
		n2	= input('Insert number2: ')
		n3	= n1+n2
		print 'The sum is:',n3

		if n3 > 10:
			print 'so big'
	
		elif n3 <5:
			print 'small'
	
		else :
			print 'average'
		
	except:
		KeyboardInterrupt()
			

	

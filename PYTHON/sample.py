#coding:UTF-8
def skip():

	# input
	#
	name = raw_input('What is your name?\n')
	print 'Hi, %s.' % name


	# iteration
	#
	friends = ['john', 'pat', 'gary', 'michael']
	for i, name in enumerate(friends):
		 print "iteration {iteration} is {name}".format(iteration=i, name=name)


	# fibonacci
	#
	parents, babies = (1, 1)
	print parents,
	while babies < 1000:
		#print 'This generation has {0} babies'.format(babies)
		print babies,
		parents, babies = (babies, parents + babies)


	# regular expression
	#
	import re
	for test_string in ['555-1212', 'ILL-EGAL']:
		 if re.match(r'^\d{3}-\d{4}$', test_string):
			  print test_string, 'is a valid US local phone number'
		 else:
			  print test_string, 'rejected'

	# hash
	#
	prices = {'apple': 0.40, 'banana': 0.50}
	my_purchase = { 'apple': 1, 'banana': 6}

	grocery_bill =  \
		sum(prices[fruit] * my_purchase[fruit] for fruit in my_purchase)

	print 'I owe the grocer $%.2f' % grocery_bill



	#  argv
	#
	import sys
	try:
		 total = sum(int(arg) for arg in sys.argv[1:])  # argv[1]～
		 print 'sum =', total
	except ValueError:
		 print 'Please supply integer arguments'


	#  file
	#
	import glob
	# glob supports Unix style pathname extensions
	python_files = glob.glob('*.py')
	for file_name in sorted(python_files):
		 print '    ------' + file_name

		 with open(file_name) as f:
			  for line in f:
					print '    ' + line.rstrip()

		 print



	# hash
	#
	from time import localtime

	activities = {8: 'Sleeping',
					  9: 'Commuting',
					  17: 'Working',
					  18: 'Commuting',
					  20: 'Eating',
					  22: 'Resting' }

	time_now = localtime()
	hour = time_now.tm_hour

	for activity_time in sorted(activities.keys()):
		 if hour < activity_time:
			  print activities[activity_time]
			  break
	else:
		 print 'Unknown, AFK or sleeping!'


	# class
	#
	class BankAccount(object):
		 def __init__(self, initial_balance=0):
			  self.balance = initial_balance
		 def deposit(self, amount):
			  self.balance += amount
		 def withdraw(self, amount):
			  self.balance -= amount
		 def overdrawn(self):
			  return self.balance < 0
	my_account = BankAccount(15)
	my_account.withdraw(5)
	print my_account.balance


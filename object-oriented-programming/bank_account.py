class bank_account(object):
	def  __init__(self,balance=0):
		self.balance = balance

	def deposit(self,amount):
		self.balance += amount
		return self.balance

	def withdraw(self,amount):
		self.balance -= amount
		return self.balance

	def __str__(self):
		return 'Balance : %d' %self.balance

class minimum_balance(bank_account):
	def __init__(self,min_bal):
		bank_account.__init__(self,min_bal)
		self.min_bal = min_bal

	def withdraw(self,amount):
		if self.balance - amount < self.min_bal:
			print 'sorry minimum balance must be maintained'
			return self.balance
		else:
			return bank_account.withdraw(self,amount)


a = bank_account(100)
b = minimum_balance(50)

print a
print b

print a.deposit(60)
print b.withdraw(40)

import psycopg2
import random
conn = psycopg2.connect("postgresql://banker:password123@localhost/bank")
cur = conn.cursor()

# Register Function (This Function Simply makes a user profile, not bank account is made)
def register():
	print("Please Insert your User Name")
	USER_NAME = input()
	print("Please Insert your email")
	EMAIL = input()
	cur.execute("""
		INSERT INTO clients (user_name,email)
		VALUES (%s,%s);
		""", (USER_NAME, EMAIL,));
	conn.commit()

def login():
	print("Please provide your username")
	USER_NAME = input()
	cur.execute("""
		SELECT client_id FROM clients WHERE user_name = %s
		""", (USER_NAME,));
	client_id = cur.fetchone()
	if not client_id == None:
		print("Client ID was found")
		return client_id[0]
	else:
		print("Account does not exist ,Please Register!")

def create_account():
	client_id = login()
	print(client_id)
	conn.commit()
	AMOUNT = 0
	ACCOUNT_NUMBER = generateAccNumber(6, leading_zeroes=False) # Should check if already exists but ... im lazy.
	while True:
		print("Please select the type of account:\n")
		print("1. Checkings")
		print("2. Savings")
		ACCOUNT_TYPE = input()
		if int(ACCOUNT_TYPE) == 1:
			ACCOUNT_TYPE = "checkings"
			break
		elif int(ACCOUNT_TYPE) == 2:
			ACCOUNT_TYPE = "savings"
			break
		else:
			print("Invalid Option, try again")
			continue
	print("Would you like to make an inital depost?[Y/N]")
	CHOICE = input()
	if CHOICE == "Y" or CHOICE == "y":
		while True:
			print("How much would you like to deposit?")
			user_input = input()
			try:
				AMOUNT = int(user_input)
				print("You entered: " + str(AMOUNT))
				break
			except ValueError:
				print("Not a number, please try again")
				continue
	cur.execute("""
		INSERT INTO accounts (account_id, client_id, balance, type) 
		VALUES (%s, %s, %s, %s)
		""", (ACCOUNT_NUMBER, client_id, AMOUNT, ACCOUNT_TYPE)); # Should the account ID be generated locally or on the DB?
	conn.commit()
	print("Account Created")

def transfer():
	pass
# Create an account (in case a user wants multiple accounts)

def deposit():
	client_id = login()
	while True:
		print("How much would you like to deposit?")
		user_input = input()
		try:
			AMOUNT = int(user_input)
			break
		except ValueError:
			print("Not a number, please try again")
			continue
	cur.execute("""
		SELECT account_id, type, balance FROM accounts WHERE client_id = %s
		""", (client_id,));
	accounts = cur.fetchall()
	numberOfAccounts = len(accounts)
	if numberOfAccounts == 0:
		print("Please make an account")
	elif numberOfAccounts == 1:
		ACCOUNT = accounts[0][0]
	else:
		while True: 
			ACCOUNT_BALANCE_DICT = {}
			print("Please choose an account to deposit too")
			for account in accounts:
				ACCOUNT_BALANCE_DICT[account[0]] = account[2]
				print(account)
			ACCOUNT_CHOICE = input()
			ACCOUNT_NUMS = ACCOUNT_BALANCE_DICT.keys() # need to check if account number is real
			print(ACCOUNT_NUMS)
			if ACCOUNT_CHOICE not in ACCOUNT_NUMS:
				print("Account not found, please try again")
				continue
			else:
				ACCOUNT = ACCOUNT_CHOICE
				BALANCE = ACCOUNT_BALANCE_DICT.get(ACCOUNT_CHOICE)
				print(ACCOUNT + "" + BALANCE)

	
				
		



	
# Credit
#https://stackoverflow.com/questions/13496087/python-how-to-generate-a-12-digit-random-number
def generateAccNumber(x, leading_zeroes=False):
    if x > 6000:
    	return ''.join([str(random.randint(0, 9)) for i in xrange(x)])
    else:
        return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)


def getAccountInfo():
	pass 


def main():
	print("connected")
	while True:
		print("Hello, welcome to my banking system!\n")
		print("What would you like to do today?")
		print("1. Register a profile \n")
		print("2. Create an account \n")
		print("3. Make a deposit \n")
		print("4. Make a transfer \n")
		print("5. Exit")
		CHOICE = int(input())
		match CHOICE:
			case 1:
				 register()
			case 2:
				create_account()
			case 3:
				deposit()
			case 4:
				transfer()
			case 5:
				break
			case _:
				print("Unknown Option Choice: Please proivde an option from 1-5")
				continue
	cur.close()
	conn.close()

main()
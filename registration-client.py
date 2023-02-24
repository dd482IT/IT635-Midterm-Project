import psycopg2

conn = psycopg2.connect("postgresql://banker:password123@localhost/midterm")
cur = conn.cursor()

print("connected")

# Register Function (This Function Simply makes a user profile, not bank account is made)
def register():
	print("Please Insert your User Name")
	USER_NAME = input()
	cur.execute("""
		INSERT INTO clients (user_name)
		VALUES (%s);
		""", (USER_NAME,));
	conn.commit()

def login():
	print("Please provide your username")
	USER_NAME = input()
	cur.execute("""
		SELECT client_id FROM clients WHERE user_name = %s
		""", (USER_NAME,));
	client_id = cur.fetchone()
	if not client_id == None:
		print("Account was found")
		return client_id[0]
	else:
		print("Account does not exist")
# Transfer Function 

def create_account():
	client_id = login()
	print(client_id)
	conn.commit()
	print("Would you like to make an inital depost?[Y/N]")
	CHOICE = input()
	AMOUNT = 0
	if CHOICE == "Y" or CHOICE == "y":
		while True:
			print("How much would you like to depost?")
			try:
				AMOUNT = int(user_input)
				print("You entered: " + AMOUNT)
				break
			except ValueError:
				print("Not a number, please try again")
				continue
	cur.execute("""
		INSERT INTO accounts (acccount_id, client_id, balance) 
		VALUES (%s, %s, %s)
		""", (123456789, client_id, AMOUNT,)); # Should the account ID be generated locally or on the DB?
	conn.commit()
	print("Account Created")

def transfer():
	pass
# Create an account (in case a user wants multiple accounts)

def deposit():
	pass 

def getAccountInfo():
	pass 

# Deposit Function
# cur.execute("""
#	INSERT INTO accounts (acccount_id, client_id, balance, created_at)
#	VALUES (%s, %s, %s)
#   RETURNING acdcount_id;
#	""", (account_id, client_id, balance));

create_account()

cur.close()
conn.close()


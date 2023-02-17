import psycopg2

conn = psycopg2.connect("postgresql://banker:password123@localhost/midterm")
cur = conn.cursor()

print("connected")

# Register Function

def  register():
	print("Please Insert your User Name")
	user_name=input()
	print("Please Insert your First Name")
	first_name=input()
	print("Please Insert your Last Name")
	last_name=input()
cur.execute("""
        INSERT INTO clients (user_name, first_name, last_name, created_at)
   	VALUES (%s, %s, %s,NOW())
        RETURNING client_id; 
""",(user_name, first_name, last_name));
	client_id = cur.fetchone()[0]
cur.execute("""
	INSERT INTO accounts (account_id, client_id, balance, created_at)
	VALUES (%s, %s, %s, NOW())
""",(1111, client_id, 0);

# Transfer Function 

# Deposit Function

cur.close()
conn.close()

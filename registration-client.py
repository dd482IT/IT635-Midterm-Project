import psycopg2

conn = psycopg2.connect("postgresql://banker:password123@localhost/midterm")
cur = conn.cursor()

print("connected")

# Register Function
print("Please Insert your User Name")
user_name = input()
cur.execute("""
        INSERT INTO clients (user_name)
   	    VALUES (%s)
        RETURNING client_id; 
    """,(user_name));
client_id = cur.fetchone()[0]
cur.execute("""
	INSERT INTO accounts (account_id, client_id, balance, created_at)
	VALUES (%s, %s, %s)
    RETURNING account_id;
	""", (account_id, client_id, balance));

# Transfer Function 

# Deposit Function



cur.close()
conn.close()

import psycopg2

conn = psycopg2.connect("postgresql://banker:password123@localhost/midterm")
cur = conn.cursor()

print("connected")
postgreSQL_select_Query = "select * from clients"
cur.execute(postgreSQL_select_Query)
response = cur.fetchone()
print(response)

exit()  
# Register Function 

cur.execute("""
        INSERT INTO rental (rental_date, inventory_id, customer_id, return_date, staff_id)
        VALUES (NOW(), %s, %s, NOW() + INTERVAL '7 DAYS', %s)
        RETURNING rental_id;
    """, (inventory_id, customer_id, staff_id));

# Transfer Function 

# Deposit Function





while True:
    print("Please enter inventory ID")
    inventory_id = int(input())
    print("Please enter customer ID")
    customer_id = int(input())
    print("Please enter staff ID")
    staff_id = int(input())
    rental_id = cur.fetchone()[0]
    print(f"Rental submitted: ID {rental_id}")
    conn.commit()

cur.close()
conn.close()
import psycopg2

def create_db():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='***' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()
    
def insert_val(item,quantity,price):
    '''adds (str,int,float)(item,quantity,price) to DB'''
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='***' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES(%s,%s,%s)",(item,quantity,price))
    conn.commit()
    conn.close()
    
def update(quantity,price,item):
    '''updates quantity, price, item in DB'''
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='***' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s",(quantity,price,item))# %s <=> ? in sqlite
    conn.commit()
    conn.close()

def delete(item):
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='***' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def view():
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='@***' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

#create_db()
insert_val('item_1',0,0)    
update(12,2,'item_1')    
insert_val('item_2',10,3)
insert_val('item_3',14,7)
delete("item_2")
print(view())
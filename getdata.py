import psycopg2
conn=psycopg2.connect(host="35.202.149.46" , user="postgres", database="postgres", password="Rahul")
cur=conn.cursor()
cur.execute("select * from wrsn03 order by datetime desc limit 10")
a= cur.fetchall()
print(a)
 

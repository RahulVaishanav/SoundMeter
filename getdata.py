import psycopg2
conn=psycopg2.connect(host="" , user="", database="", password="")
cur=conn.cursor()
cur.execute("select * from wrsn03 order by datetime desc limit 10")
a= cur.fetchall()
print(a)
 

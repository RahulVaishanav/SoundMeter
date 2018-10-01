import serial
import psycopg2
import datetime
import time
import math

data=serial.Serial('/dev/ttyUSB0',9600)


while (1==1):
	Leq=0
	Lmax=0
	try:
		for i in range(450):
			if data.inWaiting>0:
                                data.flushInput()
			        data.flush()
                                data.flushOutput()
                               
				c=data.read(5)
				try: 
				 a=float(c.replace('\n', '').replace('\r',''))
                                except:
                                 pass

#				print str(a) + "  "+ str(i) + "\n"
				Leq=Leq+ 10**(a/10)
				if a> Lmax:
					Lmax=a
			time.sleep(2)

		Leq= (10*( math.log10(Leq/450)))
		
	
		b= (str (datetime.datetime.now())[:-7])
                try:
			conn=psycopg2.connect(host="",database="", user="s", password="")
                	cur=conn.cursor()
                	cur.execute ("INSERT INTO  WRSN03 (Leq,Lmax , DATETIME) VALUES (%.1f,%.1f,'%s')" % (Leq,Lmax,b))
			conn.commit()
                	conn.close()
                except:	
			print str(Leq) + "  " + str(Lmax) +"This is  Lmax"
#	        print("done")

	except Exception as e:
#                pass
		print(e)



def recordandsend(DATE,LEQ):
        recordvoice.recordaudio()

        send.send_mail("127.0.0.1",["rvaishnav@ascengineering.org", "ascengineer@me.com","fahmad@ascengineering.org","cyang@ascengineering.org"],"WRSN03 Noise Exeedance at  %s current recording  %.1f" %(DATE,LEQ) ,"Team, <br/> The noise station has exceeded the noise levels, please see attached recording . <br/> Thanks, <br/><br/><br/> - Noise Station WRSN-03", "noise.wav")


import send
import recordvoice
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
                for i in range(15):
                        if data.inWaiting>0:
                                
                                
                                
                                c=data.read(5)
                                
                               
                                try:
                                  a=float(c.replace('\n', '').replace('\r',''))
                                except:
                                  pass

#                                print (str(a) + "  "+ str(i) + "\n")
                                Leq=Leq+ 10**(a/10)
					
                        time.sleep(2)

                Leq= (10*( math.log10(Leq/15)))
		b= (str (datetime.datetime.now())[:-7])

                if Leq>76:
			 recordandsend(b,Leq) 
#		 	 print ("emailsent") 	

                             
#                print str(Leq) + "  " +"This is  Lmax"
		time.sleep(600)

        except Exception as e:
               pass
#               print(e)








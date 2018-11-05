import sys
import serial
import time

#function definition to send command and write the serial output in to file
def execute_write_file(target,aLine,ser):
    cleanLine =aLine.replace("\n","") #removing \n from the command  
    ser.write(cleanLine.replace("\r","").encode('ascii')) #writing the command
    time.sleep(1) #delay one second
    t=ser.read(ser.in_waiting) #read number of bytes
    t1=t.replace("\n","") # replacing the \n from the read bytes              
    print t1
    #printing into the files
    target.write(cleanLine.replace("\r","").encode('ascii'))
    target.write("\n")
    target.write(t1.replace("\r","").encode('ascii'))
    target.write("\n")      
    if cleanLine.find("mac tx ") !=-1:
        print "Waiting for tx_ok...".replace("\n\r","")
        time.sleep(4) #delay one second
        t=ser.read(ser.in_waiting) #read number of bytes    
        t1=t.replace("\n","")
        print t1.replace("\r","")
        target.write(t1.replace("\r","").encode('ascii'))
        target.write("\n")
    else:
         target.write("\n")
    
# Main program starts from here...
if len(sys.argv) <3:
    print "usage: serial_acsip <COM_PORT_NUM> <FILEname for COMMSND>"
    exit()
print sys.argv[0] 
print sys.argv[1] #comm port
print sys.argv[2] #file name for the commands

#port = "COM4"
port =  sys.argv[1]
baud = 115200
fileName = "serial_acsip.txt"
fileNameCmds = sys.argv[2]

cmd_get_ch_param = "mac get_ch_para 0"
cmd_get_sys_ver  = "sip get_ver"

ser = serial.Serial(port,baud,timeout=1)
if ser.isOpen():
    print(ser.name+'is open..')
    
with open(fileNameCmds,'r') as inptarget:
    with  open(fileName,'w') as target:
        for aLine in inptarget:
            if ser.in_waiting != 0:
                t=ser.read(ser.in_waiting) #read number of bytes
                t1=t.replace("\n","")
                print t1
                target.write(t1.replace("\r","").encode('ascii'))
                target.write("\n")
                target.write("\n")

            print aLine.replace("\n","")
            if aLine.replace("\n","") == "#end":
                print "End Reached"
                exit()
            if aLine[0] !='#':
                if aLine.find("loop")!=-1:
                    print "found loop"
                    ls=aLine.split()
                    lptimes = int(ls[1])
                    print lptimes
                    x=aLine.replace("loop ","") #remove loop command
                    x = x.replace(ls[1]+" ","") #remove the count
                    count =0
                    while count < lptimes:
                        count = count +1
                        print count
                        execute_write_file(target,x,ser) #this will execute the command
                else:
                     execute_write_file(target,aLine,ser)
                    

        


  
                
               
                
            
        
        
       
        


        
    

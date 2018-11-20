def xor(a, b): 
    result = "" 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result+='0' 
        else: 
            result+='1'   
    return result 
f=open("messagegenerator.txt","r")
if f.mode=='r' :
       inputtext=f.read()
realmessage=inputtext.split()[0]
generator=inputtext.split()[1]
r=len(generator)
m=len(realmessage)
for i in range(r):
    message=realmessage+'0'
counter=r    
buffer=message[0 :counter]
while counter < m: 
   
    if buffer[0] == '1': 
            buffer = xor(generator, buffer) + message[counter] 
   
    else:  
        buffer = xor('0'*counter, buffer) + message[counter] 
   
    counter += 1
    
if buffer[0] == '1': 
    buffer = xor(generator, buffer) 
else: 
    buffer = xor('0'*counter, buffer)
realmessage+=buffer
f=open("transmittedmessage.txt","w")
f.write(realmessage)
f.write("\n")
f.write(generator)
f.close()
print("The transmitted message and the genrator are outputed in transmittedmessage.txt file to be inputted to the verifier and alter")
input("press any button to continue")

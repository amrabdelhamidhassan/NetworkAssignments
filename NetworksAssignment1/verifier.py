def xor(a, b): 
    result = "" 
    for i in range(1, len(b)): 
        if a[i] == b[i]: 
            result+='0' 
        else: 
            result+='1'   
    return result 
f=open("transmittedmessage.txt","r")
if f.mode=='r' :
       inputtext=f.read()
message=inputtext.split()[0]
generator=inputtext.split()[1]
r=len(generator)
m=len(message)
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
verifier=True    
for i in range (len(buffer)):
    if buffer[i]=='1' :
        verifier=False
        break 
if verifier:
       print("message is correct")
else :
       print("message is incorrect")
input('Press any button to exit')

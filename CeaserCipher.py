

def encrypt(text1, s):
    
    result=''

    #transverse the plain text
    
    for i in range(len(text1)):
        char=text1[i]

    #Encrypt uppercase characters in plain text
    
    if(char.isupper()):
        
        result +=chr((ord(char) + s-65)%26+65)
    else:
        result +=chr((ord(char) + s-97)%26+97)

    return result

#check the above function

text='CEASER CIPHER DEMO'

s=4

print("Plain text: "+text)

print("Shift pattern: "+str(s))

print("Cipher: "+encrypt(text, s))
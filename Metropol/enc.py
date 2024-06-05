from Crypto.Cipher import AES
import base64

message ='FirstSoft Technologies Pvt Ltd'.rjust(32)
secret_key = '1234589648789658'

#define AES mode

cipher = AES.new(secret_key,AES.MODE_ECB)
encryption = base64.b64encode(cipher.encrypt(message))
print("The encrypted message is\n",encryption)

#decode the message

decryption = cipher.decrypt

(base64.b64decode(encryption))


#print the decode

print ("Original message after decryptionis\n",decryption)
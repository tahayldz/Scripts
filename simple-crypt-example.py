from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

try:	
	def encode(password, text):
	
		encodeText = encrypt(password,text)
		encodeTextB64 = b64encode(encodeText)
	
		return encodeTextB64
	
	def decode(password,encodeTextB64):
	
		decodeTextB64 = b64decode(encodeTextB64)
		decodeText = decrypt(password,decodeTextB64)
	
		return decodeText
	
	
	text = input("Text yaz: ")
	
	password = input("pass yaz: ")
	
	encoded = encode(password,text)
	decoded = decode(password,encoded)
	
	print(encoded)
	print(decoded)	
except KeyboardInterrupt:
	print("\nBY :)")
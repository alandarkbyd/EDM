import cipherText as CT
# file = open('FindingTheLogic.txt', 'r')
# text = file.read()

try:
	text = input("Enter your secret message: ")
	typeMethod = input("Method will be applied.. (Encode or Decode)? E for encoding and D for decoding: ")

	if typeMethod == "E":
		key_set = False
		while not key_set:
			try:
				differ = int(input("Set a key(2-25): "))
				print(CT.security.encode(text, differ)[0])
				key_set = True
			except:
				print("Please enter a valid key")
				
	elif typeMethod == "D":
		provide_key = False
		while not provide_key:
				try:
					differ = int(input("Enter the key: "))
					print(CT.security.decode(text, differ))
					provide_key = True
				except:
					print("Please enter a valid key")
	else:
		print("Wrong submission!")
except:
	print("Your inputs are not valid!")

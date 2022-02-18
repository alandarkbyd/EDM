import string
from cryptography.fernet import Fernet
from string import ascii_uppercase as au

class ChipherText:
	source = dict()
	decoded = ' '
	encoded = ''
	alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
	converted = ["" for x in range(26)]


	def encode(self, phase, difference):

		text = list(phase.upper())
		for j in range(26):
			
			if (j+difference) > 25:
				
				if (j+difference) == 26:
					s = 0
				elif self.alpha[j] == 'Z':
					s = (0+difference)-1
				else:
					s = ((j+difference) - 25)-1
			
			else:
				s = (j+difference)


			self.converted[j] = self.alpha[s]

		self.source = dict(zip(self.alpha, self.converted))
		self.source.update(dict(zip(string.punctuation, string.punctuation)))
		self.source.update({' ':' '})

		for char in range(len(text)):
			self.encoded += self.source[text[char]]

		return f"Encoded message: {self.encoded.title()}", self.source

	

	def decode(self, phase, difference):	
		# indexs = [x for x in range(len(phase))]
		# index = indexs.__iter__()
		# resource = self.encode(phase, difference)[1]
		
		# try:
		# 	for key, value in resource.items():
		# 		if phase[index.__next__()] == value:
		# 			print(key, end="")
			
		# except:
		# 	print(0)
		
		for i in phase.upper():

		     self.decoded += au[au.index(i)-difference] if i in au else i

		
		return f"Decoded message: {self.decoded.title()}"

key = Fernet.generate_key()
security = ChipherText()

class Dog:

	def __init__(self, name, weight, breed, color, dressirovka):
		self.name = name
		self.weight = weight
		self.breed = breed
		self.color = color
		self.dressirovka = dressirovka

	def feed(self,corm):
		print('Я поела Чаппи')
		self.weight = self.weight + corm
		# pass 
	def bark(self):
		print("wooooow")
		# pass
	def get_tapki(self):
		if self.dressirovka == True:
			print("prines tapki")
		else:
			print("smotrit nedoumenno")

		
	# pass

sharick =  Dog("sharick", 17, "pikiness", " white", False)
bobick =  Dog("Bobick", 20, "vodolaz", "black", True)

sharick.feed(3)
print(sharick.weight)
bobick.get_tapki()
bobick.bark()




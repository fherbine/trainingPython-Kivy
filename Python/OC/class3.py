class UserAccount:
	nAccounts = 0
	lAccounts = dict()
	lAccounts['Usernames'] = list()
	lAccounts['ages'] = list()
	lAccounts['bios'] = dict()

	def __init__(self, usn, age):
		self.username = usn
		self.age = age
		self._bio = ""
		UserAccount.nAccounts += 1
		UserAccount.appendDB(self.username, self.age, self.bio)

	def __repr__(self):			# default behaviour when print(self) is called
		return self.uInfos

	def __str__(self):			# same as repr + str() cast
		return self.uInfos

	def __getattr__(self, atr): # can't get the specified attribute !
		print("Attribute '{}' not found !".format(atr))

	def _get_bio(self):
		return self._bio

	def _set_bio(self, bioBuffer):
		sep = str()
		if self._bio != "":
			sep = "\n"
		bioBuffer = sep + bioBuffer
		self._bio += bioBuffer
		UserAccount.lAccounts['bios'][self.username] += bioBuffer

	def eraseBio(self):
		self._bio = ""
		UserAccount.lAccounts['bios'][self.username] = ""

	def _get_user(self):
		return "The user {} is {} years old and is bio is:\n{}".format(self.username, self.age, self.bio)

	def displayDB(cls):
		print("There's {} users registered".format(cls.nAccounts))
		print(cls.lAccounts)

	displayDB = classmethod(displayDB)

	def appendDB(cls, newUsn, newAge, newBio):
		cls.lAccounts['Usernames'].append(newUsn)
		cls.lAccounts['ages'].append(newAge)
		cls.lAccounts['bios'][newUsn] = newBio

	appendDB = classmethod(appendDB)

	bio = property(_get_bio, _set_bio)
	uInfos = property(_get_user)

if __name__ == "__main__":
	user1 = UserAccount("toto", 35)
	print(user1.uInfos)
	user1.bio = "I'm {} and I'm here to conquest the world !".format(user1.username)
	print(user1.uInfos)
	user1.bio = "AHAHAHHA ! (Weird laugh)"
	print(user1.uInfos)

	usr2 = UserAccount("fherbine", 19)
	usr2.bio = "I created toto, so I can destroy him !"

	UserAccount.displayDB()

	user1.eraseBio()
	print(user1.uInfos)

	UserAccount.displayDB()
	print(user1.__dict__)
	#print(UserAccount.__dict__)
	print(dir(UserAccount))
	#print(dir(user1))
	print(user1)
	str1 = str(user1)
	print(str1)
	print(user1.toto)

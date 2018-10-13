class UserAccount:
	nAccounts = 0
	lAccounts = dict()
	lAccounts['Usernames'] = list()
	lAccounts['ages'] = list()
	lAccounts['bios'] = dict()

	def __init__(self, usn, age):
		self.username = usn
		self.age = age
		self.bio = ""
		UserAccount.nAccounts += 1
		UserAccount.appendDB(self.username, self.age, self.bio)

	def writeBio(self, bioBuffer):
		sep = str()
		if self.bio != "":
			sep = "\n"
		bioBuffer = sep + bioBuffer
		self.bio += bioBuffer
		UserAccount.lAccounts['bios'][self.username] += bioBuffer

	def eraseBio(self):
		self.bio = ""
		UserAccount.lAccounts['bios'][self.username] = ""

	def displayUser(self):
		print("The user {} is {} years old and is bio is:\n{}".format(self.username, self.age, self.bio))

	def displayDB(cls):
		print("There's {} users registered".format(cls.nAccounts))
		print(cls.lAccounts)

	displayDB = classmethod(displayDB)

	def appendDB(cls, newUsn, newAge, newBio):
		cls.lAccounts['Usernames'].append(newUsn)
		cls.lAccounts['ages'].append(newAge)
		cls.lAccounts['bios'][newUsn] = newBio

	appendDB = classmethod(appendDB)
if __name__ == "__main__":
	user1 = UserAccount("toto", 35)
	user1.displayUser()
	user1.writeBio("I'm {} and I'm here to conquest the world !".format(user1.username))
	user1.displayUser()
	user1.writeBio("AHAHAHHA ! (Weird laugh)")
	user1.displayUser()

	usr2 = UserAccount("fherbine", 19)
	usr2.writeBio("I created toto, so I can destroy him !")

	UserAccount.displayDB()

	user1.eraseBio()
	user1.displayUser()

	UserAccount.displayDB()
	print(user1.__dict__)
	#print(UserAccount.__dict__)
	print(dir(UserAccount))
	print(dir(user1))

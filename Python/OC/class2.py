class UserAcc:
	def __init__(self, usn, age):
		self.usn = usn
		self.age = age
		self._livingPlace = "Paris"

	def _get_livingPlace(self):
		print("getting {} living place...".format(self.usn))
		return self._livingPlace

	def _set_livingPlace(self, newPlace):
		print("{} has a new home in {}".format(newPlace))
		self._livingPlace = newPlace

	livingPlace = property(_get_livingPlace, _set_livingPlace)

if __name__ == "__main__":
	usr1 = UserAcc("toto", 32)
	print(usr1.livingPlace)
	usr1.livingPlace = "Tokyo"
	print(usr1.livingPlace)

#A variable in a superior scope is remind in a down scope even if the inicial def or scope is deleted
#Need  nested function


def make_multiplier(x):

	def multipler(n):
		return x * n

	return multipler

times10 = make_multiplier(10)
times4 = make_multiplier (4)

print(times10(3))
print(times4(5))
print(times10(times4(2)))
class A:
	def do_something(self):
		print('Method defined In: A')

class B(A):
	pass
	def do_something(self):
		print('Method defined In: B')
		super().do_something()

class C(A):
	pass
	def do_something(self):
		print('Method defined In: C')

class D(B,C):
	pass
	def do_something(self):
		print('Method defined In: D')
		super().do_something()

# print(D.__mro__)
# print(D.mro())
# help(D)


thing = D()
thing.do_something()
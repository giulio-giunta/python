class Animal:
    cool = True
    
    def make_sound(self, sound):
        print(f'this animal says {sound}')
        
class Cat(Animal):
        pass

blue = Cat()
blue.make_sound('MEOW')
print(blue.cool)
print(Cat.cool)
print(Animal.cool)

print(id(blue.cool))
print(id(Cat.cool))
print(id(Animal.cool))

print(isinstance(blue,Cat))
print(isinstance(blue,Animal))
print(isinstance(blue,object))


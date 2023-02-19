#Import your helpers module here.  Do not use the 'from' or 'as' syntax, just use a plain old 'import'
from helpers import lucky_number as lucky


#Call the lucky_number function from your helpers module, and save the result to a variable called num
num = lucky()
print(num)
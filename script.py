print("Hello")
#print (hello)






import sys
print(sys.version)
#to know version of python







"""
its comment
"""
# its comment




x = 5
y = "asghar"
print(x)
print(y)




x = 4       # x is of type int
x = "ahnmad" # x is now of type str
print(x)



x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0




x = 5
y = "asghar"
print(type(x))
print(type(y))
#to know type of something





x = "mamad"
x = 'mamad'
# is the same as



a = 4
A = "sina"
#A is not eaqual with a





"""2myvar = "John"
my-var = "John"
my var = "John"""
#wrong form




myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
#corect form





x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
#short work





x = y = z = "Orange"
print(x)
print(y)
print(z)
#short work





fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
#short work






"""x = 5
y = "John"
print(x + y)"""
#make eror




x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()

print("Python is " + x)





x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
#to have global var 







x = 5
print(type(x))
#return number





"""
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
"""
#types







x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType
#types






x = 1
y = 2.8
z = 1j

print(type(x))
print(type(y))
print(type(z))




import random
print(random.randrange(1000, 9999))
#to have a random number





x = float(1)
y = int(2.8)
z = int("3")
a = str(1)
print(x)
print(y)
print(z)
print(a)
#to change type




print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')




a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)




a = "Hello, World!"
print(a[1])
#Get the character at position 1 (remember that the first character has the position 0)




a = "Hello, World!"
print(len(a))
#The len() function returns the length of a string:



txt = "The best things in life are free!"
print("free" in txt)
#to know have we somthing in some texts( return true or faluse ) 



txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")



txt = "The best things in life are free!"
print("expensive" not in txt)
#to know havent we somthing in some texts( return true or faluse ) 



txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")





b = "Hello, World!"
print(b[2:5])
#return llo



b = "Hello, World!"
print(b[:5])
#return hello



b = "Hello, World!"
print(b[2:])
#llo, World!






b = "Hello, World!"
print(b[-5:-2])
#return orl







a = "Hello, World!"
print(a.upper())
#The upper() method returns the string in upper case





a = "Hello, World!"
print(a.lower())
#The lower() method returns the string in lower case





print(a.strip()) # returns "Hello, World!"
#The strip() method removes any whitespace from the beginning or the enda = " Hello, World! "




a = "Hello, World!"
print(a.replace("H", "J"))
#The replace() method replaces a string with another string






a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
#The split() method returns a list where the text between the specified separator becomes the list items.






a = "Hello"
b = "World"
c = a + b
print(c)




a = "Hello"
b = "World"
c = a + " " + b
print(c)




"""age = 36
txt = "My name is John, I am " + age
print(txt)
#wrong code cant + int and str"""





age = 36
txt = F"My name is John, I am {age}"
print(txt)
#correct form
#F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.





""""txt = "We are the so-called "Vikings" from the north."""
#wrong form




txt = "We are the so-called \"Vikings\" from the north."
#correct form






"""
capitalize()                         #	Converts the first character to upper case
casefold()                         #	Converts string into lower case
center()	                         #Returns a centered string
count()                         #	Returns the number of times a specified value occurs in a string
encode()                         #	Returns an encoded version of the string
endswith()                         #	Returns true if the string ends with the specified value
expandtabs()                         #	Sets the tab size of the string
find()                         #	Searches the string for a specified value and returns the position of where it was found
format()                         #	Formats specified values in a string
format_map()	                         #Formats specified values in a string
index()	                         #Searches the string for a specified value and returns the position of where it was found
isalnum()                         #	Returns True if all characters in the string are alphanumeric
isalpha()                         #	Returns True if all characters in the string are in the alphabet
isascii()	                         #Returns True if all characters in the string are ascii characters
isdecimal()	                         #Returns True if all characters in the string are decimals
isdigit()	                         #Returns True if all characters in the string are digits
isidentifier()	                         #Returns True if the string is an identifier
islower()	                         #Returns True if all characters in the string are lower case
isnumeric()	                         #Returns True if all characters in the string are numeric
isprintable()	                         #Returns True if all characters in the string are printable
isspace()	                         #Returns True if all characters in the string are whitespaces
istitle()	                         #Returns True if the string follows the rules of a title
isupper()	                         #Returns True if all characters in the string are upper case
join()                         #	Joins the elements of an iterable to the end of the string
ljust()                         #	Returns a left justified version of the string
lower()                         #	Converts a string into lower case
lstrip()	                         #Returns a left trim version of the string
maketrans()                         #	Returns a translation table to be used in translations
partition()	                         #Returns a tuple where the string is parted into three parts
replace()                         #	Returns a string where a specified value is replaced with a specified value
rfind()                         #	Searches the string for a specified value and returns the last position of where it was found
rindex()                         #	Searches the string for a specified value and returns the last position of where it was found
rjust()                         #	Returns a right justified version of the string
rpartition()                         #	Returns a tuple where the string is parted into three parts
rsplit()                         #	Splits the string at the specified separator, and returns a list
rstrip()                         #	Returns a right trim version of the string
split()                         #	Splits the string at the specified separator, and returns a list
splitlines()                         #	Splits the string at line breaks and returns a list
startswith()	                         #Returns true if the string starts with the specified value
strip()                         #	Returns a trimmed version of the string
swapcase()                         #	Swaps cases, lower case becomes upper case and vice versa
title()                         #	Converts the first character of each word to upper case
translate()                         #	Returns a translated string
upper()                         #	Converts a string into upper case
zfill()                         #	Fills the string with a specified number of 0 values at the beginning
"""



#booleans
print(10 > 9)
print(10 == 9)
print(10 < 9)




a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")




print(bool("Hello"))
print(bool(15))





x = "Hello"
y = 15

print(bool(x))
print(bool(y))





bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])




bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})





def myFunction() :
  return True

print(myFunction())







def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")









x = 200
print(isinstance(x, int))
#Check if an object is an integer or not




print(10 + 5)





#oprerators

"""
+	Addition	x + y	
-	Subtraction	x - y	
*	Multiplication	x * y	
/	Division	x / y	
%	Modulus	x % y	
**	Exponentiation	x ** y	
//	Floor division	x // y
"""




"""
=	x = 5	x = 5	
+=	x += 3	x = x + 3	
-=	x -= 3	x = x - 3	
*=	x *= 3	x = x * 3	
/=	x /= 3	x = x / 3	
%=	x %= 3	x = x % 3	
//=	x //= 3	x = x // 3	
**=	x **= 3	x = x ** 3	
&=	x &= 3	x = x & 3	
|=	x |= 3	x = x | 3	
^=	x ^= 3	x = x ^ 3	
>>=	x >>= 3	x = x >> 3	
<<=	x <<= 3	x = x << 3	
:=	print(x := 3)	x = 3
print(x)
"""







"""
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y	
"""






"""
and         Returns True if both statements are true                                	x < 5 and  x < 10	
or	        Returns True if one of the statements is true	                            x < 5 or x < 4	
not	        Reverse the result, returns False if the result is true	                  not(x < 5 and x < 10)
"""




"""
in                   	Returns True if a sequence with the specified value is present in the object                  x in y	
not in                Returns True if a sequence with the specified value is not present in the object	            x not in y
"""





"""
& 	AND	Sets each bit to 1 if both bits are 1	x & y	
|	OR	Sets each bit to 1 if one of two bits is 1	x | y	
^	XOR	Sets each bit to 1 if only one of two bits is 1	x ^ y	
~	NOT	Inverts all the bits	~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2	
>>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2
"""










"""
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
"""








print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)









#lists
mylist = ["apple", "banana", "cherry"]




thislist = ["apple", "banana", "cherry"]
print(thislist)






thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#Print the number of items in the list:




mylist = ["apple", "banana", "cherry"]
print(type(mylist))





thislist = ["apple", "banana", "cherry"]
print(thislist[1])





thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#return cherry






thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])






thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#This will return the items from index 0 to index 4.
#Remember that index 0 is the first item, and index 4 is the fifth item
#Remember that the item in index 4 is NOT included




thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#This will return the items from index 2 to the end.
#Remember that index 0 is the first item, and index 2 is the third







thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")








thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#Negative indexing means starting from the end of the list.
#This example returns the items from index -4 (included) to index -1 (excluded)
#Remember that the last item has the index -1,





thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#change the second item






thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon"






thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#Change the second value by replacing it with two new values






thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist) 
#To insert a new list item, without replacing any of the existing values, we can use the insert() method.The insert() method inserts an item at the specified index:Insert "watermelon" as the third item:




thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#Using the append() method to append an item






thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#TROPICAL WILL add in thislist





thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist) 




thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)





thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)






thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)






thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
#The clear() method empties the list.The list still remains, but it has no content.



thislist = ["apple", "banana", "cherry"]
for a in thislist:
  print(a)
#loop in list






thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])








thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1








thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
#for loop short form







fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# just words with "a" will show
 







fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# just words with "a" will show





#newlist = [expression for item in iterable if condition == True]
#syntax







fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if x != "apple"]

print(newlist)
#it wont print just "apple"







fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits]
print(newlist)







newlist = [x for x in range(10)]
print(newlist)
#print 0 to 10






newlist = [x for x in range(10) if x < 5]
print(newlist)
#return 0 to 4





fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x.upper() for x in fruits]
print(newlist)
#print 'APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO'






fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = ['hello' for x in fruits]
print(newlist)
#replace hello for fruits




fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
#wont print banana





thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)






thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)







list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)






list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)






list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)








"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list
"""







mytuple = ("apple", "banana", "cherry")
#tupel syntax






thistuple = ("apple", "banana", "cherry")
print(thistuple)






thistuple = ("apple", "banana", "cherry")
print(len(thistuple))







#it is tupel
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))







thistuple = ("apple", "banana", "cherry")
print(thistuple[1])





thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])




thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included





thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#print 'apple', 'banana', 'cherry', 'orange'



thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#print 'cherry', 'orange', 'kiwi', 'melon', 'mango'




x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)






thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)








"""thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple)
 #this will raise an error because the tuple no longer exists"""






fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)






fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)







fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)






thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)





thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])





thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1







tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)






fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)







#count()	Returns the number of times a specified value occurs in a tuple
#index()	Searches the tuple for a specified value and returns the position of where it was found






#set
myset = {"apple", "banana", "cherry"}





thisset = {"apple", "banana", "cherry"}
print(thisset)
# Note: the set list is unordered, meaning: the items will appear in a random order.
# Refresh this page to see the change in the result.





thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)




thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)






thisset = {"apple", "banana", "cherry"}
print(len(thisset))





set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

print(set1)
print(set2)
print(set3)






myset = {"apple", "banana", "cherry"}
print(type(myset))






thisset = set(("apple", "banana", "cherry"))
print(thisset)
# Note: the set list is unordered, so the result will display the items in a random order.









thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)







thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
#return  true




thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)
#return  faluse







thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)





thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
#add tropical to thisset






thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)






thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)




thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)





thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal
#return   cherry       and       {'banana', 'apple'}





thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)






"""thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset) 
#this will raise an error because the set no longer exists"""







thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)








set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)







set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"mohse,", "sina"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)







x = {"a", "b", "c"}
y = (1, 2, 3)
z = x.union(y)
print(z)






set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)





set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)






set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)





set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)






set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", "microsoft", "apple", True}

set3 = set1.intersection(set2)
print(set3)





set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)





set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)
print(set1)






set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)
print(set3)






set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2

print(set3)






set1 = {"apple", "banana" , "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)
print(set1)







"""
add()	 	Adds an element to the set
clear()	 	Removes all the elements from the set
copy()	 	Returns a copy of the set
difference()	-	Returns a set containing the difference between two or more sets
difference_update()	-=	Removes the items in this set that are also included in another, specified set
discard()	 	Remove the specified item
intersection()	&	Returns a set, that is the intersection of two other sets
intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	 	Returns whether two sets have a intersection or not
issubset()	<=	Returns whether another set contains this set or not
 	<	Returns whether all items in this set is present in other, specified set(s)
issuperset()	>=	Returns whether this set contains another set or not
 	>	Returns whether all items in other, specified set(s) is present in this set
pop()	 	Removes an element from the set
remove()	 	Removes the specified element
symmetric_difference()	^	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
union()	|	Return a set containing the union of sets
update()	|=	Update the set with the union of this set and others

"""









#Dictionaries
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}








thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])







thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(len(thisdict))








thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}
print(thisdict)








thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))








thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict) 








thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.get("model")
print(x)
#return Mustang









thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.keys()

print(x)
# return       dict_keys(['brand', 'model', 'year'])









car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}

x = car.keys()

print(x) #before the change

car["color"] = "white"

print(x) #after the change










thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.values()

print(x)
#return        dict_values(['Ford', 'Mustang', 1964])







thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = thisdict.items()

print(x)
#return        dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])









thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")










thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict["year"] = 2018

print(thisdict)







thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)








thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)








thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)









thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)









"""thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) 
#this will cause an error because "thisdict" no longer exists."""







thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)










thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)







thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)








thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)







thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)






thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)







thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)











myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)










child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)









myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])









myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])






"""
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
"""







"""
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
"""






a = 33
b = 200

if b > a:
  print("b is greater than a")






"""a = 33
b = 200

if b > a:
print("b is greater than a")
#dont forget space behind print"""






a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")






a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")






a = 200
b = 33
if a > b: print("a is greater than b")





a = 2
b = 330
print("A") if a > b else print("B")









a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")








a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")





a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")







a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")








x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")







a = 33
b = 200
if b > a:
  pass
# having an empty if statement like this, would raise an error without the pass statement









#while loops
#for loops





i = 1
while i < 6:
  print(i)
  i += 1








i = 1
while i < 6:
  print(i)
  if (i == 3):
    break
  i += 1






i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
# Note that number 3 is missing in the result







i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")








fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 







for x in "banana":
  print(x) 
#return "b" "a" "n" "a" "a"






fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break
# return "apple" "banana"





fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 
# return "apple" 





fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 
#banana wont print





for x in range(6):
  print(x) 
#return 0 1 2 3 4 5 







for x in range(2, 6):
  print(x) 
#return 2 3 4 5 









for x in range(2, 30, 3):
  print(x) 
#return  2 5 8 11 14 17 20 23 26 29
#سه تا ستا میره جلو تا 30









for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")
#If the loop breaks, the else block is not executed.









adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)







for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement






#function



def my_function():
  print("Hello from a function")

my_function()







def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")








def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")






def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")
#it make err because lname







def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")







def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")







def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
#retrn                    I am from Sweden                  I am from India                  I am from Norway                  I am from Brazil








def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)











def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
#return     15             25             45










def myfunction():
  pass

# having an empty function definition like this, would raise an error without the pass statement











def my_function(x, /):
  print(x)

my_function(3)







def my_function(x):
  print(x)

my_function(x = 3)











def my_function(x, /):
  print(x)

my_function(x = 3)
#make err






def my_function(*, x):
  print(x)

my_function(x = 3)







def my_function(*, x):
  print(x)

my_function(x = 3)






def my_function(*, x):
  print(x)

my_function(3)
#make err







def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)










#lambda arguments : expression
#syntax








x = lambda a: a + 10
print(x(5))





x = lambda a, b: a * b
print(x(5, 6))
#return 30




x = lambda a, b, c: a + b + c
print(x(5, 6, 2))
#return 13








def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
print(mydoubler(11))
#return 22







def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)
print(mytripler(11))
#return 33







def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))
#return 22 and 33









#array 




cars = ["Ford", "Volvo", "BMW"]
print(cars)







cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)






cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)







cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)







cars = ["Ford", "Volvo", "BMW"]

for x in cars:
  print(x)






cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)





cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
#remove volvo





cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)







#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#sort()	Sorts the list










#Classes/Objects





class MyClass:
  x = 5
print(MyClass)










class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)
#return 5












class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)
#return  ​      John      36








class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)
#return       <__main__.Person object at 0x15039e602100>









class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"    
  
p1 = Person("John", 36)
print(p1)
#John(36)






class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#return        hello my name is john










class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
#return        hello my name is john







class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40
print(p1.age)
#return      40











class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age
print(p1.age)
# make err








class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1
print(p1)
# make err









class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement










#iterators



mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))










mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))









mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)









mystr = "banana"

for x in mystr:
  print(x)

















class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
#return 1 2 3 4 5








class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)
#return 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20








#Polymorphism



x = "Hello World!"
print(len(x))




mytuple = ("apple", "banana", "cherry")
print(len(mytuple))







thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))









class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car class
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat class
plane1 = Plane("Boeing", "747")     #Create a Plane class

for x in (car1, boat1, plane1):
  x.move()
#return      Drive!     Sail!     Fly!















class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!")

class Plane(Vehicle):
  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()
#return           Ford          Mustang          Move!          Ibiza          Touring 20          Sail!          Boeing          747          Fly!








#scope
def myfunc():
  x = 300
  print(x)

myfunc()






def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()










x = 300

def myfunc():
  print(x)

myfunc()
print(x)
# print 300 and 300








x = 300

def myfunc():
  x = 200
  print(x)

myfunc()
print(x)
# print 200 and 300







def myfunc():
  global x
  x = 300

myfunc()
print(x)







x = 300

def myfunc():
  global x
  x = 200

myfunc()
print(x)







def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())











#Modules
def greeting(name):
  print("Hello, " + name)




import mymodule
mymodule.greeting("Jonathan")




import mymodule as mx
a = mx.person1["age"]
print(a)






import platform
x = platform.system()
print(x)





import platform

x = dir(platform)
print(x)






 
from mymodule import person1
print(person1["age"])








#Dates
import datetime
x = datetime.datetime.now()
print(x)




x = datetime.datetime.now()
print(x.year)
print(x.strftime("%A"))




x = datetime.datetime(2020, 5, 17)
print(x)






x = datetime.datetime(2018, 6, 1)
print(x.strftime("%B"))






"""%a	Weekday, short version	Wed	
%A	Weekday, full version	Wednesday	
%w	Weekday as a number 0-6, 0 is Sunday	3	
%d	Day of month 01-31	31	
%b	Month name, short version	Dec	
%B	Month name, full version	December	
%m	Month as a number 01-12	12	
%y	Year, short version, without century	18	
%Y	Year, full version	2018	
%H	Hour 00-23	17	
%I	Hour 00-12	05	
%p	AM/PM	PM	
%M	Minute 00-59	41	
%S	Second 00-59	08	
%f	Microsecond 000000-999999	548513	
%z	UTC offset	+0100	
%Z	Timezone	CST	
%j	Day number of year 001-366	365	
%U	Week number of year, Sunday as the first day of week, 00-53	52	
%W	Week number of year, Monday as the first day of week, 00-53	52	
%c	Local version of date and time	Mon Dec 31 17:41:00 2018	
%C	Century	20	
%x	Local version of date	12/31/18	
%X	Local version of time	17:41:00	
%%	A % character	%	
%G	ISO 8601 year	2018	
%u	ISO 8601 weekday (1-7)	1	
%V	ISO 8601 weeknumber (01-53)	01"""








#math

x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)
#return 5 , 25





x = abs(-7.25)
print(x)
#return 7.25





x = pow(4, 3)
print(x)
#retrn 64




import math




x = math.sqrt(64)
print(x)
#return 8.0





#Import math library
import math

#Round a number upward to its nearest integer
x = math.ceil(1.4)

#Round a number downward to its nearest integer
y = math.floor(1.4)

print(x)
print(y)
#return 2  , 1





import math
x = math.pi
print(x)
#3.141592653589793
















#JSON
import json




import json

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])
#return 30 









import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
#return    {"name": "John", "age": 30, "city": "New York"}b










#You can convert Python objects of the following types, into JSON strings:
#dict
#list
#tuple
#string
#int
#float
#True
#False
#None










import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
#return               #{"name": "John", "age": 30}            #["apple", "bananas"]            #["apple", "bananas"]            #"hello"            #42            #31.76            #true            #false            #null











#dict	Object
#list	Array
#tuple	Array
#str	String
#int	Number
#float	Number
#True	true
#False	false
#None	null








import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)
#return    {"name": "John", "age": 30, "married": true, "divorced": false, "children": ["Ann","Billy"], "pets": null, "cars": [{"model": "BMW 230", "mpg": 27.5}, {"model": "Ford Edge", "mpg": 24.1}]}








import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))












import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))















import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))










#regEX
import re




"""
findall            Returns a list containing all matches
search             Returns a Match object if there is a match anywhere in the string
split              Returns a list where the string has been split at each match
sub	               Replaces one or many matches with a string
"""





"""
[]	A set of characters	"[a-m]"	
\	Signals a special sequence (can also be used to escape special characters)	"\d"	
.	Any character (except newline character)	"he..o"	
^	Starts with	"^hello"	
$	Ends with	"planet$"	
*	Zero or more occurrences	"he.*o"	
+	One or more occurrences	"he.+o"	
?	Zero or one occurrences	"he.?o"	
{}	Exactly the specified number of occurrences	"he.{2}o"	
|	Either or	"falls|stays"	
()	Capture and group	 
"""





"""
\A	Returns a match if the specified characters are at the beginning of the string	"\AThe"	
\b	Returns a match where the specified characters are at the beginning or at the end of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\bain"

r"ain\b"	

\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
(the "r" in the beginning is making sure that the string is being treated as a "raw string")	r"\Bain"

r"ain\B"	

\d	Returns a match where the string contains digits (numbers from 0-9)	"\d"	
\D	Returns a match where the string DOES NOT contain digits	"\D"	
\s	Returns a match where the string contains a white space character	"\s"	
\S	Returns a match where the string DOES NOT contain a white space character	"\S"	
\w	Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)	"\w"	
\W	Returns a match where the string DOES NOT contain any word characters	"\W"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"
"""




"""
[arn]	Returns a match where one of the specified characters (a, r, or n) is present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 and 59	
[a-zA-Z]	Returns a match for any character alphabetically between a and z, lower case OR upper case	
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
"""




import re
#Check if the string starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")







import re
#Return a list containing every occurrence of "ai":
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)
#return    ['ai', 'ai']




import re
txt = "The rain in Spain"
#Check if "Portugal" is in the string:
x = re.findall("Portugal", txt)
print(x)

if (x):
  print("Yes, there is at least one match!")
else:
  print("No match")









import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start()) 










import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)
#return "None"






import re

#Split the string at every white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)
#return          ['The', 'rain', 'in', 'Spain']








import re

#Split the string at the first white-space character:

txt = "The rain in Spain"
x = re.split("\s", txt, 1)
print(x)
#return ['The', 'rain in Spain']








import re

#Replace the first two occurrences of a white-space character with the digit 9:

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)
print(x)
#return      The9rain9in Spain






"""
The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match
"""








import re

#The search() function returns a Match object:

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)
#return     <_sre.SRE_Match object; span=(5, 7), match='ai'>










import re

#Search for an upper case "S" character in the beginning of a word, and print its position:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())
#return   (12, 17)









import re

#The string property returns the search string:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)
#return       The rain in Spain








import re

#Search for an upper case "S" character in the beginning of a word, and print the word:

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
#return   spain








#try ... except

#The try block lets you test a block of code for errors.

#The except block lets you handle the error.

#The else block lets you execute code when there is no error.

#The finally block lets you execute code, regardless of the result of the try- and except blocks.





#The try block will generate an error, because x is not defined:
try:
  print(x)
except:
  print("An exception occurred")
#return     An exception occurred







#This will raise an exception, because x is not defined:
print(x)








#The try block will generate a NameError, because x is not defined:
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
#return       Variable x is not defined









#The try block does not raise any errors, so the else block is executed:

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
#  return  Hello    Nothing went wrong











#The finally block gets executed no matter if the try block raises any errors or not:

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
#Something went wrong       The 'try except' is finished












#The try block will raise an error when trying to write to a read-only file:
try:
  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")  
# return   Something went wrong when writing to the file










x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")
"""
return  
Traceback (most recent call last):
  File "demo_ref_keyword_raise.py", line 4, in <module>
    raise Exception("Sorry, no numbers below zero")
Exception: Sorry, no numbers below zero
"""








x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")
"""
return

Traceback (most recent call last):
  File "demo_ref_keyword_raise2.py", line 4, in <module>
    raise TypeError("Only integers are allowed")
TypeError: Only integers are allowed
"""







#f-string
txt = f"The price is 49 dollars"
print(txt)




price = 59
txt = f"The price is {price} dollars"
print(txt)





price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)






txt = f"The price is {95:.2f} dollars"
print(txt)








txt = f"The price is {20 * 59} dollars"
print(txt)






price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars"
print(txt)
#return    The price is 73.75 dollars






price = 49
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"
print(txt)






fruit = "apples"
txt = f"I love {fruit.upper()}"
print(txt)







def myconverter(x):
  return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000)} meter altitude"
print(txt)






price = 59000
txt = f"The price is {price:,} dollars"
print(txt)









"""
:<		Left aligns the result (within the available space)
:>		Right aligns the result (within the available space)
:^		Center aligns the result (within the available space)
:=		Places the sign to the left most position
:+		Use a plus sign to indicate if the result is positive or negative
:-		Use a minus sign for negative values only
: 		Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
:,		Use a comma as a thousand separator
:_		Use a underscore as a thousand separator
:b		Binary format
:c		Converts the value into the corresponding Unicode character
:d		Decimal format
:e		Scientific format, with a lower case e
:E		Scientific format, with an upper case E
:f		Fix point number format
:F		Fix point number format, in uppercase format (show inf and nan as INF and NAN)
:g		General format
:G		General format (using a upper case E for scientific notations)
:o		Octal format
:x		Hex format, lower case
:X		Hex format, upper case
:n		Number format
:%		Percentage format

"""




price = 49
txt = "The price is {} dollars"
print(txt.format(price))





price = 49
txt = "The price is {:.2f} dollars"
print(txt.format(price))





quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))
#retu    I want 3 pieces of item number 567 for 49.00 dollars.rn






age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))
#return      His name is John. John is 36 years old.





myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))
# return          I have a Ford, it is a Mustang.











input("press enter to exit")

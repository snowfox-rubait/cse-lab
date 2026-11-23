# Online Python compiler (interpreter)
# Write and run Python online using this editor.

print("Also try Visualize to understand code.")# list
print("list examples start here.")
list = ['abd', 79823, 2.22, 'maw', 'a', 'a', 'bruh', 'items'] # you can change it on the fly
print (list)
print (list[0])
print (list[1:3])
print (list[4:5])
list[0] = 'changed'
print(list[0])
print(list)
list.append('haw') # adding from last
print(list)
print(list.pop()) # by default it pops the last vaule, pop means print and delete the list value. btw "list.remove()" does the same thing
print (list.pop(2)) # pops the 2nd item to the list. index number of that item is 1 btw. index start from 0.
list.insert(2,"inserted 2nd value")
print(list)
list.reverse() # reverses the list
print(list)
number=[1,4,7,2,3,6]
print(number)
number.sort()
print(number)
del(number) # deletes this list
# print(number) # if you uncomment this, it will throw error cause "number" list has been deleted.
print(list.count('a')) # counts how many times this item is there.
# tuple
print("tuple starts from here.")
tuple = ('haw', 234, 2.22, 'meh', 'talapuka') # read only list
print (tuple)
print (tuple[0])
# tuple[0] = 'tried to change' # this is an invalid operation
print (tuple[0])
print(tuple)

#dictonary
print("dictonary examples starts here.")
dict = {} # empty dictionary declaration is required
lista = {}
dict['one'] = "This is one"
dict[2] = "two i guess?"
dict['haw'] = "dict is equal to haw"
lista ['waw'] = {'name': 'john', 'haw':'wah','code':6723} 
print (dict['one'], dict[2], dict['haw'])
print(dict)
print (lista)
print(lista.keys())
print (lista.values())
print(len(dict), len(lista), len(tuple), len(list))

print ("print key vaule pairs")
for i in dict.items(): #print key vaule pairs
  print(i)
print()
print("print value")
for i in dict.values(): #print vaules
  print(i)
print()
print("print keys")
for i in dict.keys(): #print keys
  print(i)
print()
del(list)
print(dict.clear())

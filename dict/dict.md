***Dictionary in python***

Dictionaries and lists share the following characteristics:

- Both are mutable.
- Both are dynamic. They can grow and shrink as needed.
- Both can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.

Dictionaries differ from lists primarily in how elements are accessed:

- List elements are accessed by their position in the list, via indexing.
- Dictionary elements are accessed via keys.

---



**Dictionary: dict()** A dictionary stores **key-value** pairs, where each unique key is an **index** which holds the values associated with it. Dictionaries are **unordered** because the entries are not stored in a linear structure. k**ey:value** The **keys** and **values** can have any of the basic data types or structures. Two keys can have the same value. However, it is crucial that all keys are unique.

using the { } curly brackets

```python
 empty_dict={}
 print(empty_dict)              #output:{}
 phone_book={“Batman”:468426,”Cersei”:237734,”Ghostbusters”:44678}
 print(phone_book)             #output: {‘Batman’:468426}
```

using the dict() constructor

```python
empty_dict=dict()
print(empty_dict)              #output:{}
phone_book=dict(Batman:468426,Cersei:237734,Ghostbusters:44678)
print(phone_book)             #output: {‘Batman’:468426}
```

directly give the elements

```python
mydict[1]=22
mydict[2]=33
mydict[3]=44
mydict
#prints {1: 22, 2: 33, 3: 44}
```

**get()** - method

```python
a_dictionary.get(key)
phone_book={“Batman”:468426,”Cersei”:237734,”Ghostbusters”:44678}
print(phone_book[“Cersei”])
#output: 237734
print(phone_book.get(“Ghostbusters”))
#output: 44678
```

**Dictionary Operations:**

 Updating Elements

```python
phone_book[“Batman”]=9211  
#output: Batman’s value is updated

phone_book[“Godzilla”]=420   
#output: Godzilla:420 key:value pair is added
```

**Removing Entries** using **del**() function

```python
 del(phone_book[“Batman”])
 print(phone_book)
```

**pop() or popitem()**

```python
phone_book={“Batman”:468426,”Cersei”:237734,”Ghostbusters”:44678}
print(phone_book)
cersei=phone_book.pop(“Cersei”)
print(phone_book)    
#output:{‘Batman’:468426,’Ghostbusters’:44678}

print(cersei)                            
#output: 237734

lastAdded=phone_book.popitem()
print(lastAdded) 
#output: (‘Batman’,468426)

print(len(phone_book))        
#output:3
```

**Checking elements**

```python
print(“Batman” in phone_book)     
#output: True
print(“Godzilla” in phone_book)   
#output: False
```

**update()**

```python
phone_book={"Batman":4646}
second_phone_book={"Catwoman":9999}
phone_book.update(second_phone_book)

phone_book
#prints {'Batman': 4646, 'Catwoman': 9999}
second_phone_book
#prints {'Catwoman': 9999}
```

**clear()** - method that empties the dictionary

```python
mydict={"Batman":4646}
mydict.clear()
```

**items()** - method that lists all the items in the dictionary

```python
phone_book.items()
dict_items([('Batman', 4646), ('Catwoman', 9999)])
#prints dict_items([('Batman', 4646), ('Catwoman', 9999)])
```

**keys()** - method that lists all the keys in the dictionary

```python
phone_book.keys()
#prints dict_keys(['Batman', 'Catwoman'])
```

**values()** - method that lists all the values in the dictionary

```python
phone_book.values()
#prints dict_values([4646, 9999])
```

**update()** - method that updates the dictionary

```python
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}

d1.update(d2)
#d1 contains {'a': 10, 'b': 200, 'c': 30, 'd': 400}
```



**Dictionary Comprehension:** To iterate the dictionary use **dict.items()** operation which turns a dictionary into a list of **(key,value) tuples**

```python
houses={1:”Gryffindor”,2:”Slytherin”,3:”Hufflepuff”,4:”Ravenclaw”}
new_houses={n**2: house + “!” for (n,house) in houses.items()}
print(houses)   
#ouput: {1:”Gryffindor!”,4:”Slytherin!”,9:”Hufflepuff!”,16:”Ravenclaw!”}
```


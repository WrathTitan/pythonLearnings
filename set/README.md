#**Sets**

- Sets are unordered.
- Set elements are unique. Duplicate elements are not allowed.
- A set itself may be modified, but the elements contained in the set must be of an immutable type.

**Mutable objects**:

list, dict, set, byte array

**Immutable objects:**

int, float, complex, string, tuple, frozen set [note: immutable version of set], bytes

**Overall:**

- Python handles mutable and immutable objects differently.
- Immutable are quicker to access than mutable objects.
- Mutable objects are great to use when you need to change the size of the object, example list, dict etc.. Immutables are used when you need to ensure that the object you made will always stay the same.
- Immutable objects are fundamentally expensive to “change”, because doing so involves creating a copy. Changing mutable objects is cheap.

**Creating a set**

\######1. Directly assigning values to a set

```python
myset={11,12,13,14,14,14,14,15,15,16}
print(myset)
type(myset)
```

\######2. Using the set() constructor

Can be used to create an empty set. The set constructor requires an <iter> iterator.

```python
myset=set()
print(myset)
type(myset)
```

######3. We can also create a set from a list or a string

```python
myset=set(['1','2','3','4'])
print(myset)

s="Great"
myset1=set(s)

mylist=[11,12,13,22,33,22,22,-1,0,3,-33]
myset2=set(mylist)
```

- The argument to `set()` is an iterable. It generates a list of elements to be placed into the set.
- The objects in curly braces are placed into the set intact, even if they are iterable.

```python
myset3={"wow"} #stores wow as one element of the set
myset4=set("wow") # stores w and o as 2 elements of the set
```

* Python takes { } curly brackets as a dictionary so we have to define a set by using the set constructor

```python
myset1=set()
type(myset1) #<class 'set'>

myset2={}
type(myset2) #<class 'dict'>
```

* An empty set is false in boolean

```python
x=set() # Empty Set
bool(x) # prints False
```

---

**Modifying contents of a set**

Using the *add()* function:

```python
myset.add('a')
myset.add('b')
myset.add((4,3))
#myset contains {'a', 'b', (4, 3)}
```

---


 Using the *update()* function:

```python
myset={11,12,13}
myset.update((1,2,3))# update() only works for iterable objects
#Now the set contains {1, 2, 3, 11, 12, 13}

myset.update({'a','b','c','hello'},['a','e','f'])
#myset contains {1, 2, 3, 'f', 11, 12, 13, 'b', 'hello', 'c', 'e', 'a'}

myset.update({1, 6}, [5, 13],(45,56)) #list items, set items, and tuple items added individually
#myset contains {'a', 1, 'c', 'b', 4, 5, 6, 7, 8, 2, (5, 4), 13, 3}
```


 **REMOVING ITEMS**

Both the *discard()* and *remove()* functions take a single value as an argument and removes that value from the set. If that value is not present, *discard()* does nothing, but *remove()* will raise a KeyError exception.

```python
myset.discard(10)
#myset contains {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 13, 11, 3}
myset.remove(13)
#prints {'a', 1, 'c', 'b', 4, 5, 7, 8, 2, 12, (5, 4), 11, 3}
```

**pop()** method

```python
myset={1,2,3}
myset.pop() #print 1
#myset contains {2,3}
```

`x.pop()` removes and returns an arbitrarily chosen element from `x`. If `x` is empty, `x.pop()` raises an exception:

**clear()** method

```python
myset={1,2,3}
myset.clear() 
#myset contains nothing
```



 **Set size and Membership**

```python
myset={'a','b','c'}
len(myset) #prints 3

'a' in myset #returns True
```

**COMMON SET OPERATIONS** Using *union()*, *intersection()* and *difference()* functions.

```python
a = {2, 4, 5, 9}
b = {2, 4, 11, 12}

a.union(b) # Values which exist in a or b
a | b
#prints {2, 4, 5, 9, 11, 12}

a.intersection(b) # Values which exist in a and b 
a & b
#prints {2, 4}

a.difference(b) # Values which exist in a but not in b
a - b
#prints {9, 5}
```


 The *union()* and *intersection()* functions are symmetric methods:

```python
>> a.union(b) == b.union(a)
True
>> a.intersection(b) == b.intersection(a)
True
>> a.difference(b) == b.difference(a)
False
```

*symmetric_difference()*  The elements that are in set a or set b but not in both

```python
a=set([11,12,13,14,15])
b=set([11,12,23,24,25])

a ^ b
a.symmetric_difference(b)
#prints {23, 24, 25, 13, 14, 15}
```

*isdisjoint()*  returns true if there are no elements in common in sets a and b

```python
a=set([11,12,13,14,15])
b=set([11,12,23,24,25])
a.disjoint(b)
# prints False
```

*issubset()*  returns true if every element on set a is a subset of set b

```python
a=set([11,12,13,14,15])
b=set([11,12,23,24,25])
c=set(11,12,13)

c.issubset(a)
c<=a	#prints True
c<=b	#prints False
```

A proper subset is the same as a subset, except that the sets can’t be identical. A set `x1` is considered a proper subset of another set `x2` if every element of `x1` is in `x2`, and `x1` and `x2` are not equal.

```python
c<a
c<b

c<=c	#True
c<c		#False
```

*issuperset()*  A superset is the reverse of a subset. A set `x1` is considered a superset of another set `x2` if `x1` contains every element of `x2`.

```python
a=set([11,12,13,14,15])
b=set([11,12,23,24,25])
c=set(11,12,13)

a.issuperset(c)
a>=c	#prints True
b>c	#prints False
```

A proper superset is the same as a superset, except that the sets can’t be identical. A set `x1` is considered a proper superset of another set `x2` if `x1` contains every element of `x2`, and `x1` and `x2` are not equal.

*intersection_update()* - Modify a set by intersection

`x1.intersection_update(x2)` and `x1 &= x2` update `x1`, retaining only elements found in both `x1` and `x2`:

```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 &= x2
#prints {'foo', 'baz'}

x1.intersection_update(['baz', 'qux'])
#prints {'baz'}
```

*difference_update()*

`x1.difference_update(x2)` and `x1 -= x2` update `x1`, removing elements found in `x2`:

```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 -= x2
#prints {'bar'}

x1.difference_update(['foo', 'bar', 'qux'])
#prints set()
```

*symmetric_difference_update()*

`x1.symmetric_difference_update(x2)` and `x1 ^= x2` update `x1`, retaining elements found in either `x1` or `x2`, but not both:

```python
x1 = {'foo', 'bar', 'baz'}
x2 = {'foo', 'baz', 'qux'}

x1 ^= x2
#prints {'bar', 'qux'}

x1.symmetric_difference_update(['qux', 'corge'])
#prints {'bar', 'corge'}
```

## Frozen Sets

Python provides another built-in type called a **frozenset**, which is in all respects exactly like a set, except that a frozenset is immutable. You can perform non-modifying operations on a frozenset:

```python
x = frozenset(['foo', 'bar', 'baz'])
#Now if we type x it prints frozenset({'foo', 'baz', 'bar'})
len(x)
#prints 3

x & {'baz', 'qux', 'quux'}
#prints frozenset({'baz'})
```

special case

```python
x1 = set(['foo'])
x2 = set(['bar'])
x3 = set(['baz'])
x = {x1, x2, x3}
#doesn't work
```

but this works

```python
x1 = frozenset(['foo'])
x2 = frozenset(['bar'])
x3 = frozenset(['baz'])
x = {x1, x2, x3}
```


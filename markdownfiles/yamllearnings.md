## YAML

* Yet another markup language / YAML ain't markup language
* Serialisation language - *Serialization* or *marshaling* is the process of converting object state into a format that can be transmitted or stored. The serialization changes the object state into series of bits. The object state could be reconstructed later in the opposite process, called *deserialization* or *unmarshalling*. The reconstructed object is a semantically identical clone to the original object. The object after serialization is called *archive*. Serialization is a low-level technique that violates encapsulation and breaks the opacity of an abstract data type.
* The file starts with three dashes. These dashes indicate the start of a new YAML document.
* Indentation is how YAML denotes nesting. The number of spaces can vary from file to file, but tabs are not allowed. 

```yaml
---
 doe: "a deer, a female deer"
 ray: "a drop of golden sun"
 pi: 3.14159
 xmas: true
 french-hens: 3
 calling-birds:
   - huey
   - dewey
   - louie
   - fred
 xmas-fifth-day:
   calling-birds: four
   french-hens: 3
   golden-rings: 5
   partridges:
     count: 1
     location: "a pear tree"
   turtle-doves: two
```

* yaml can have multiple data types like int, float, strings, arrays, booleans.
* Below is how a yaml file is when it is converted in json format

```json
{
  "doe": "a deer, a female deer",
  "ray": "a drop of golden sun",
  "pi": 3.14159,
  "xmas": true,
  "french-hens": 3,
  "calling-birds": [
     "huey",
     "dewey",
     "louie",
     "fred"
  ],
  "xmas-fifth-day": {
  "calling-birds": "four",
  "french-hens": 3,
  "golden-rings": 5,
  "partridges": {
    "count": 1,
    "location": "a pear tree"
  },
  "turtle-doves": "two"
  }
}
```

* Comments in yaml use a # symbol

```yaml
___
# This is a full line comment
foo: bar # this is a comment, too
```

### Numeric types

YAML recognizes numeric types, floating point and integers above. An integer can be decimal, hexidecimal, or octal.

```yaml
---
 foo: 12345
 bar: 0x12d4
 plop: 023332
```

Python script on this document gives the following

```
foo : 12345
 bar : 4820
 plop : 9946
```

**Ox** indicates a value is hex, and a leading zero denotes an octal value. YAML supports both fixed and exponential floating point numbers.

```yaml
---
 foo: 1230.15
 bar:  12.3015e+05
```

When we evaluate these entries we see:

```
foo : 1230.15
 bar : 1230150.0
```

We can also represent not-a-number (NAN) or infinity.

```yaml
---
foo: .inf
bar: -.Inf
plop: .NAN
```

**Foo** is infinity. **Bar** is negative infinity, and **plop** is NAN.

---

### Strings

YAML strings are Unicode. In most situations, you don't have to specify them in quotes.

```yaml
---
foo: this is a normal string
```

Our test program processes this as:

```
foo: this is a normal string
```

But if we want escape sequences handled, we need to use double quotes.

```yaml
---
foo: "this is not a normal string\n"
bar: this is not a normal string\n
```

YAML processes the first value as ending with a carriage return and linefeed. Since the second value is not quoted, YAML treats the \n as two characters.

```
foo: this is not a normal string
bar : this is not a normal string\n
```

YAML will not escape strings with single quotes, but the single quotes do avoid having string contents interpreted as document formatting. String values can span more than one line. With the fold (greater than) character, you can specify a string in a block.

```yaml
bar: >
  this is not a normal string it
  spans more than
  one line
  see?
```

But it's interpreted without the newlines.

```
bar : this is not a normal string it spans more than one line see?
```

The block (pipe) character has a similar function, but YAML interprets the field exactly as is.

```yaml
bar: |
  this is not a normal string it
  spans more than
  one line
  see?
```

So, we see the newlines where they are in the document.

```
bar : this is not a normal string it
spans more than
one line
see?
```

### Nulls

You enter nulls with a tilde or the unquoted null string literal.

```yaml
---
foo: ~
bar: null
```

Our program prints:

```
foo : None
bar : None
```

Python's representation for null is None.

### Booleans

YAML indicates boolean values with the keywords True, On and Yes for true. False is indicated with False, Off, or No.

```yaml
---
foo: True
bar: False
light: On
TV: Off
```

### Arrays

You can specify arrays or lists on a single line.

```yaml
---
items: [ 1, 2, 3, 4, 5 ]
names: [ "one", "two", "three", "four" ]
```

Or, you can put them on multiple lines.

```yaml
---
items:
  - 1
  - 2
  - 3
  - 4
  - 5
names:
  - "one"
  - "two"
  - "three"
  - "four"
```

The multiple line format is useful for lists that contain complex objects instead of scalars.

```yaml
___
items:
  - things:
      thing1: huey
      things2: dewey
      thing3: louie
  - other things:
      key: value
```

An array can contain any valid YAML value. The values in a list do not have to be the same type.

### Dictionaries

We covered dictionaries above, but there's more to them. Like arrays, you can put dictionaries inline. We saw this format above. It's how python prints dictionaries.

```yaml
---
foo: { thing1: huey, thing2: louie, thing3: dewey }
```

We've seen them span lines before.

```yaml
---
foo: bar
bar: foo
```

And, of course, they can be nested and hold any value.

```yaml
---
foo:
  bar:
    - bar
    - rab
    - plop
```

## Advanced Options

### Chomp Modifiers

Multiline values may end with whitespace, and depending on how you want the document to be processed you might not want to preserve it. YAML has the **strip** chomp and **preserve** chomp operators. To save the last character, add a plus to the fold or block operators.

```yaml
bar: >+
  this is not a normal string it
  spans more than
  one line
  see?
```

So, if the value ends with whitespace, like a newline, YAML will preserve it. To strip the character, use the strip operator.

```yaml
bar: |-
  this is not a normal string it
  spans more than
  one line
  see?
```

### Multiple documents

A document starts with three dashes and ends with three periods. Some YAML processors require the document start operator. The end operator is usually optional. For example, Java's Jackson will not process a YAML document without the start, but Python's PyYAML will. You'll usually use the end document operator when a file contains multiple documents. Let's modify our python code.

```python
import yaml

if __name__ == '__main__':
    stream = open("foo.yaml", 'r')
    dictionary = yaml.load_all(stream)

    for doc in dictionary:
        print("New document:")
        for key, value in doc.items():
            print(key + " : " + str(value))
            if type(value) is list:
                print(str(len(value)))
```

PyYAML's **load****_****all** will process all of the documents in a stream. Now, let's process a compound document with it.

```
---
bar: foo
foo: bar
...
---
one: two
three: four
```

The script finds two YAML documents.

```
New document:
bar : foo
foo : bar
New document:
one : two
three : four
```
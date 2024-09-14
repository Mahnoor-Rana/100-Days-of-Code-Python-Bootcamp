# Python Type Handling

This README covers TypeError, type checking, and type conversion in Python.

## TypeError

These errors occur when you are using the wrong data type. For example:

```python
len(12345)
```

Because you can only give the `len()` function Strings, it will refuse to work and give you a TypeError if you give it a number (Integer).

### Exercise 1
Fix the `len()` function so it has no more warnings or errors.

## Type Checking

You can check the data type of any value or variable in Python using the `type()` function.

```python
print(type("abc"))  # will give you 
```

### Exercise 2
Write out 4 type checks to print all 4 data types. Use the `type()` and `print()` functions to print out 4 lines into the output area so we get the full collection of data types that we learned about:
- `<class 'str'>`
- `<class 'int'>`
- `<class 'float'>`
- `<class 'bool'>`

## Type Conversion

You can convert data into different data types using special functions. For example:
- `float()`
- `int()`
- `str()`

### Exercise 3
Make this line of code run without errors:

```python
print("Number of letters in your name: " + len(input("Enter your name")))
```

Hint: You'll need to use type conversion to make this work correctly.
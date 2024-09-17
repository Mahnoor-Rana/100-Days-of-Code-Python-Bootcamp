## Random Module
### Pseudorandom Number Generators

Computers are not random, because they are built with circuits and switches. But randomness is very important when building software, especially games. It would be really boring if every move in a video game was pre-determined.

So, some computer scientists invented pseudorandom number generators. e.g. https://en.wikipedia.org/wiki/Mersenne_Twister

If you want to learn more about pseudorandom number generators, I recommend watching this video by Khan Academy: https://www.youtube.com/watch?v=GtOt7EBNEwQ&ab_channel=KhanAcademyLabs

### The Random module in Python

Read the docs here: https://docs.python.org/3/library/random.html

To use it you need to first import it:

```python
import random
rand_num = random.randint(1, 10)
```
### Modules in Python
Python allows us to put code into different files and import that code if needed. This means that we can better organise and modularise our code.
You can create a new module simply by creating a new .py file and then you can import variables or functions from that file just by using the import keyword.
### Random Floats
You can generate a random number between 0 (not inclusive) and 1 (inclusive) using the following code from the random module:
```python
import random
rand_num_0_to_1 = random.random()
```
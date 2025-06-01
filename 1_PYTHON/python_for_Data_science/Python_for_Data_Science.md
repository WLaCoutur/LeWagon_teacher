Python for Data Science
Python
Multi-platform
Interpreted / Dynamic Typing
Garbage Collected
Object-Oriented & Procedural
Large Standard Library
Created by Guido van Rossum, first released in 1991
REPL
Read, Eval, Print, Loop.
Open your terminal and launch:
ipython
Documentation
👉 The Python 3.12 Standard Library
Built-in Types
Let's look at the important sections of the documentation and explore the simple built-in types.
Numeric Types 🔗
type(42)
int
type(3.14)
float
4 + 9.5
13.5
abs(-5)
5
Booleans 🔗
type(True) # or type(False)
bool
True and False
False
True or False
True
not True
False
What are falsy values in Python?
Constants defined to be false: None and False
Zero of any numeric type: 0, 0.0, etc.
Empty sequences and collections: '', (), [], {}, set(), range(0)
Comparisons
5 < 3 # Strictly less than
False
4 <= 4 # Less than or equal
True
"boris" == "seb" # equal, note the `double` =
False
"boris" != "seb" # not equal
True
Text Sequence Type (Strings, str)
"boris"
'boris'
"boris".capitalize()
'Boris'
"   boris ".strip()
'boris'
type(int("42"))
int
Check out the documentation for more str methods.
Advanced built-in types
Sequence Types
list
tuple
range
An example of list
["apple", "cherries", "banana"]
['apple', 'cherries', 'banana']
len(["apple", "cherries", "banana"])
3
"banana" in ["apple", "cherries", "banana"]
True
Mapping Type
There is just one in Python, dict (read "dictionary").
{'city': 'Paris', 'population': 2_141_000}
{'city': 'Paris', 'population': 2141000}
len({'city': 'Paris', 'population': 2_141_000})
2
'city' in {'city': 'Paris', 'population': 2_141_000}
True
Variables
name = 'John' # Assignment
print(name)
John
name = 'Paul' # Re-assignment
print(name)
Paul
first_name = 'John'
last_name = 'Lennon'
full_name = first_name + last_name
print(full_name)
JohnLennon
String Formatting - Interpolation
sentence = f'Hi, my name is {first_name} {last_name}'
print(sentence)
Hi, my name is John Lennon
list operations
# Indexes:    0       1       2
beatles = ['john', 'paul', 'ringo']
beatles[0] # Read
'john'
beatles.append('george') # Create (in place)
print(beatles)
['john', 'paul', 'ringo', 'george']
beatles[1] = 'Paul' # Update (in place)
print(beatles)
['john', 'Paul', 'ringo', 'george']
Other list operations
beatles
['john', 'Paul', 'ringo', 'george']
beatles[1:3] # Slice of 1 to 3 (excluded)
['Paul', 'ringo']
del beatles[1] # Delete (in place)
print(beatles)
['john', 'ringo', 'george']
dict operations
instruments = {'john': 'guitar', 'paul': 'bass'} # Keys are `str`, Values too
instruments['john'] # Read
'guitar'
instruments['ringo'] = 'drums' # Create / Update
print(instruments)
{'john': 'guitar', 'paul': 'bass', 'ringo': 'drums'}
del instruments['john']
instruments
{'paul': 'bass', 'ringo': 'drums'}
Other dict operation
instruments
{'paul': 'bass', 'ringo': 'drums'}
What will happen if we run instruments['john']?
instruments['john']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-40-4f6ae9ee253b> in <module>
----> 1 instruments['john']

KeyError: 'john'
instruments.get('john', 'Default instrument')
'Default instrument'
Control Flow
Once again, the documentation is very thorough.
if statement
age = int(input("How old are you?"))

if age >= 21:
    print("You can become president")
elif age >= 18:
    print("You can vote")
else:
    print("Be patient!")
for statement (on a list)
words = ['cat', 'wolf', 'beetle']
for word in words:
    print(word.upper())
CAT
WOLF
BEETLE
List comprehension
You can achieve the same result in just one line:
[print(word.upper()) for word in words]
... or store it in a new variable:
uppercase_words = [word.upper() for word in words]
print(uppercase_words)
['CAT', 'WOLF', 'BEETLE']
What if you need the index inside the for loop?
for index, word in enumerate(words):
    print(index, word)
0 cat
1 wolf
2 beetle
for statement (on a dict)
instruments
{'paul': 'bass', 'ringo': 'drums'}
for beatle, instrument in instruments.items():
    print(f'{beatle.capitalize()} plays the {instrument}')
Paul plays the bass
Ringo plays the drums
while loop
i = 1
while i <= 4:
    print(i)
    i = i + 1
1
2
3
4
Functions
Let's see how we can define and use our own functions.
def is_even(number):
    return number % 2 == 0
The function is named is_even
The function takes 1 parameter: number
The function returns a bool
result = is_even(42)
print(result)
True
We called the function with the argument 42.
The returned value is stored in a result variable.
Keyword Arguments
Let's have a look at pandas.DataFrame.from_dict (Source). Some arguments are passed with the syntax parameter=value.
def is_odd(number=0):
    return number % 2 == 1
result = is_odd(number=1)
print(result)
True
Mixing positional and keyword arguments
def full_name(first_name, last_name, capitalize=False):
    if capitalize:
        return f"{first_name.capitalize()} {last_name.capitalize()}"
    else:
        return f"{first_name} {last_name}"
print(full_name("john", "lennon"))
print(full_name("ringo", "starr", capitalize=True))
john lennon
Ringo Starr
Modules 🔗
As our programs grow longer, we'll want to split the code into multiple files and folders.
Here is a very simple example to illustrate this technique:
mkdir project && cd project
touch app.py
mkdir helpers && touch helpers/__init__.py
# helpers/__init__.py
import random
import string

def generate_password(size):
    """Generate a random lowercase ASCII password of given size"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))
# app.py
from helpers import generate_password # Module import here

print(generate_password(16))
python app.py
Before you go, one more thing!
Debugging 🐛
print(your_variable)
ipython
python <file_name>
When running your code with python <file_name> you can use the IPython debugger (ipdb) thanks to the built-in breakpoint() function.
It will let you investigate the current state of your code.
Let's try with our generate_password function!
Add the debugger in the function definition and run python app.py file from the Terminal.
# helpers/__init__.py
import random
import string

def generate_password(size, upper=False):
    """Generate a random lowercase ASCII password of given size"""
    letters = string.ascii_uppercase if upper else string.ascii_lowercase
    breakpoint() # <- That's a BREAKPOINT!
    return ''.join(random.choice(letters) for i in range(size))
You can access the args, variables defined within the function (letters) and much more: just type the name of the variable and hit ENTER.
To see the part of the code you're at, type list (or just l).
To continue the execution try:
next (or just n) - execute the current line and go to the next line
step (or just s) - step into the next function that will be called
continue (or just c) - continue until the next breakpoint(), or the end
If you want to see all available commands type help (or just h).
Tips from TAs ❤️
Read the instructions!
It's OK not to finish all challenges
Pseudocode first!
Programming is all about going step by step, decomposing hard problems into small ones.
✒️ Write down the steps you'll need to code in plain English.
Separate 🤔 thinking about the ⚙️ logic from getting the ["syntax')} exactly right.
Run your code!
‼️ Don't try to make directly.
# example.py
def my_function(param1, param2):
    # BODY
    # BODY
    # BODY
    return # SOMETHING

print(my_function(arg1, arg2)) # <- Temp code to test! Remove before final commit/push

and then run the code in your terminal:
python example.py
Debug your code!
Poor man's way: print() all the things! What's the type of this variable? What does it contain at this point of the program?

Better: debug your code using breakpoint()!


💪 Debugging is one of the most important skills to master in your career!
Advanced Language Topics
To master Python, here are some additional topics to dive into during the Bootcamp:
List Comprehensions
Iterators & Generators
Object Oriented Programming
*args & **kwargs
Memory Management / Garbage Collection
Your turn!
Head to Kitt, find your buddy and start your first challenge!
Remember:
Read the assignment carefully
Run your code with python <file.py> before running make
Talk with your buddy
Raise a ticket 🙋‍♀️
Have fun! 🚀
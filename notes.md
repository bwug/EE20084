<h1> Week 1 </h1>

> for(let i=1;i<=100;i++){s="";if(i%3==0){s+="fizz"}if(i%5==0){s+="buzz"}if(s==""){s=i}console.log(s)}

<h2> Course overview: </h2>

- Introduction to python, data structures (arrays, lists and dictionaries)
- Expressions and flow control (sequence, selection and iteration)
- Functions, objects and classes

- Advanced IO
- Libraries
- Modules
- Code optimisation and acceleration

<h2> Assessment: </h2>

- Design Report: 10%
- Code Review: 20%
- Full Report: 20%

- Exam: 50%
    - Two questions, 20 marks per question
    - One question from each lecturer

Python is an interpreted, high level language. Interpreted means that the source code is processed into machine code at the point of operation. The alternative is compiled languages, where the source code must be compiled / converted into a processor specfic machine code executable before it may be used.

High-level means that there is a strong abstraction between the programming syntax or language used, and that of the underlying processor operation itself. It is usually more reader friendly at the cost of potential optimisations.

<h2> Lecture 2 - Variables and Operators </h2>

- Variables: In essence, is a name used to refer to some piece of data, these variables are assigned different **data types**

- Data Types: The way we are representing the data, such as a string or integer

- Operators: Tools that manipulate variables and data

<details>
<summary>
Examples using C
</summary>

```C
int main ()
{
    int age = 6; // The variable name is "age", the data type is "int" and the value is "6"
    char initial = "H";
    char name = "John"; // Throws an error!
    return 0; // Notice that we are returning an int in an int function
}
```

</details>

As seen in the code block above, we can assign data to variables using the assignment operator _=_

Data typing can be either strong or weak, this is how the programming language enforces data typing rules

- For example, in python `5 + "5"` would throw an error, whereas in JavaScript, `1 + "11"` will output _111_ as a string

Data typing is also either static or dynamic, this is how the language inteprets changes to data types

- For example, in python, `age = 6` is valid code, whereas in C, C++, Java, C# etc. you have to declare the data type beforehand using the _int_ keyword

The four primary data types are:
- Integers
- Characters
- Booleans
- Floating point number

> strings are fundamentally an array of characters, more on this later

You can also change a data type, this is referred to as casting and is seen more in dynamic languages than static languages. For example, in python, `str(6)` will convert the integer 6 into the character `"6"`

Operators, as previously mentioned, are used to manipulate or compare data, python has the following operator groups:
- Arithmetic
- Assignment
- Comparison
- Logical
- Identity
- Membership
- Bitwise

Examples for all of these can be seen in [the example code area](/extra_code/example_codes.py)

<h2> Lecture 3 - Introduction to abstract data types </h2>

Last lecture, single data points were introduced and how they can be typed, in this lecture abstract data types will be introduced, these are: **lists**, **arrays**, **tuples**, **sets** and **dictionaries**

- Lists
    - A list is a collection of data points of any type that is mutable and ordered.
- Arrays
    - An array is a mutable, ordered set of data points of the *same type*. The size of an array is unchanged during runtime and is seen mostly in static typing languages
- Tuples
    - A tuple is an immutable, ordered set of data points of any type that cannot be modified in any way during runtime
- Sets
    - A set is an abstract data type that is unordered and unindexed
    - There is no meaning by the position of items in the set
    - You can cast from another data structure to a set to remove all duplicates
- Dictionaries
    - A dictionary is a collection of key-value pairs, where the key is a unique value that points to the value
    <details><summary>Example code in python:</summary>

    ```python
    dict = { "value1": "Hello",
    "value2": "world",
    "name": "Harry"
    }
    ```
    </details>

### Iterables and the iter function

All of these abstract data types are also known as "iterables", which means we can iterate over each individual index

Demos of iterables are found in the [the example code area](/extra_code/example_codes.py)

### Accessing lists and arrays

Lists and arrays can be accessed using square brackets `[]`, in most languages, data structures are indexed from "0".

<details><summary> Example Code </summary>

```py
data = [2, 3, 5, 7, 9] # Creates a LIST of 5 points
data.append(11) # Changes the size of the LIST during runtime
print(data[0], data[2:1000])
```
</details>

<br>

<details><summary>List vs. Array</summary>The notes say lists are analogous to arrays in other languages, though most high level languages support both lists and arrays.
Lists are technically arrays with dynamic memory management and are more like a kind of array, so the use of the word analogous is correct, albeit a tad misleading. Ignore this section if you do not care about dynamic memory management in abstract data types

An [interesting stackoverflow page](stackoverflow.com/questions/3917574/how-is-pythons-list-implemented) goes over how python converts arrays into lists</details>

## Lecture 4 - Introduction to sequence, selection and iteration

> Known as "Program Control Flow", though the computer science terms have been used

<details><summary> Sequence </summary>

```py
print("hello", end = " ")
print("world")
print("My age is", end = " ")
print(3)
print("I think?")
```

</details>
<details><summary> Selection </summary>

```py
a, b = True, False
if a and b: print(True) # Will not print
if a or b: print(True) # Will not print
```

</details>
<details><summary> Iteration </summary>

```py
for x in range(0, 10):
    print(x)

while 1:
    print("Hello world")
```

</details>

Python includes a number of keywords and structures that are used to control the flow of a program, it also uses white space instead of the common curly brackets { } to dictate depth in a program

This indentation is used to help control the flow of a program, as each new layer of control needs a new layer of indentation

### if, elif and else

Almost all programming languages use if, else if (elif) and else statements. These will execute code conditionally, i.e if the input statement meets certain criteria

For example: `if a > b: print("A is bigger than B!")` is valid code for a single operation, but we can expand this to:<br>`print("a > b!") if a > b else print("a <= b")` <- which is also referred to as a ternary statement, something seen in the C programming module

### for and while

While loops allow programs to repeat a section of code, this repitition will only work if the given condition is True, for example: `while a < b: a += 1` will continue looping until _a_ is greater than or equal to _b_

### pass, break and continue

```py
if a >= b:
    if a == b:
        pass
    elif a > b:
        # Code
        return 0

for x in range(0, 10):
    if x == 4:
        break
    print(x)

# 0, 1, 2, 3

for name in names:
    if name == "harry": continue
    print(name)
    # Prints everything but harry
```

### Error handling

```py
try:
    print(x)
except:
    print("Error!")
# Assuming x doesn't exist, the "except" code will occur

try:
    x = "5"
    print(x + 3)
except TypeError, ValueError:
    print("Type or Value error occured")
```

## Lecture 5 - Introduction to python functions

In this section lambda functions _(anonymous functions)_ and standard functions and procedures

A function or procedure are reusable blocks of code that can take inputs and outputs, though functions are different in that they return an output whereas procedures simply act on data without returning code

Both will be referred to as _functions_ for the rest of this module

Functions will allow users to develop modular code, this helps with:
- Testing - Individual functions can be tested
- Development - Reusable code blocks make development easier
- Transferability - Code can be shared between developers for separate files more easily

**Syntax:**
```py
def func(input1, input2) -> int:
    return input1 + input2
```

The name of the function is func, the arguments - or _args_ - are the input variables given to the function. We then see the "-> int" keyword, which specfies the function returns an integer value

Finally, we reach the "return" statement, which returns anything on that line of code, using abstract data types for returning multiple data values

We can also structure functions using `def f(*args):` or `def f(**kwargs)` to input many arguments without using many argument names

<details><summary>Example code</summary>

```py
def f(*args):
    for arg in args: print(arg)

def b(**kwargs):
    for key, value in kwargs:
        print(key, value)
```
</details>

We can also use _default arguments_ or _optional arguments_ which will have a default value

<details><summary>Example code</summary>

```py
def foo(a, b="hello"):
    print(a)
    print(b)

foo("world", "hiya")
# prints "hiya" instead of "hello"
```
</details>

Nested functions are functions that contain functions

<details><summary>Nested code example</summary>

```py
def head_function(foo, bar):
    def find_sum(num_list, sum = 0) -> int:
        for num in num_list: sum += num
        return sum
    
    if foo = "find_sum": return find_sum(bar)
    else: return 0

def return_larger(num1, num2):
    if num1 > num2: return num1
    elif num1 < num2: return num2
    else: return -1

print(return_larger(5, 6))
# Passing the function return_larger as an argument for print
```
</details>

Recursive functions are functions that call themselves, they do this by implementing a portion of memory called the "stack"

<details><summary>Simple recursive function</summary>

```py
def count_down(n):
    print(n)
    if n >= 0:
        n -= 1
        count_down(n)
    if n < 0: return
```
</details>

Anonymous functions, known as _lambda functions_ in python, are functions that cannot be called but instead run in the line of code that is being executed

<details><summary>Simple anonymous function</summary>

```py
def my_func(a):
    return lambda x: x * a

doubler = my_func(2)
print(doubler(4)) # prints 8
```
</details>

## Lecture 6 - Introduction to python object-oriented programming

Object Oriented Programming, _OOP_ is a programming paradigm that separates code into objects, classes, methods and attributes

It revolves around the concepts of _objects_

_Objects_ can contain data in the form of properties, or attributes or functions in the form of methods, furthermore, a _class_ is a template for an _object_ and most languages support both classes and objects and an object is an instantiation of a class if classes do exist

There are a few notable oddities, such as JSON - "JavaScript object notation", created to use with JavaScript but supported by most high level languages

I will provide extra information in the [example code](/extra_code/object_code.js) area

Classes in python are created using the _class_ keyword, and a general template can be seen below:

```py
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
    def get_name(self): return self.name

    def get_age(self): return self.age

person_a = Person("Harry", 19)

print(person_a.get_age()) # prints 19

del person_a.age()
```

Let's break this down

`class Person` creates a new class template called "Person" (note the capital P)

`def __init__` is a **private** function called initialise that has the parameter `self` which is a keyword that refers to everything about the class while inside the clas

`self.name = name` sets the objects name to the name passed when calling the class instantiate function `Person(name, age)`

`def get_name(self): return self.name` returns the name by using a "getter" function, which is used in high level languages to keep classes private, so data inside of them cannot be manipulated or changed by external sources, such as subroutines in the main code

Classes can also inherit other classes, meaning they inherit new methods and attributes:

```py
class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self, name="", age=0, grade):
        super().__init__(name, age)
        self.grade = grade
```

#### Important note

A fascinating piece of code was shown earlier and quickly brushed over, **get**

The getter function, and similarly, the setter function are both methods inside a class which are used to access data inside a class.

##### Note this is for computer science only

A class can have two kinds of attributes, private and public, a public piece of information can be accessed and changed by anything inside of the code

```py
class Person:
    def __init__(self):
        __name = "harry"
        # Attribute cannot be changed
        age = 7
        # Code can be changed
```

```C++
class Rectangle {
        int width, height;
    public:
        void set_values(int,int);
        int area(void);
} rectangle;
```

In C++, the private (implied) and public keywords are used to instantiate attributes in classes whereas in python we use a number of underscores however they don't enforce privacy rules and are instead implications to the developer, whereas C++ private keyword enforces privacy

In python, classes have inbuilt `__get__` and `__set__` methods

```py
class Rectangle:
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height
   
rect = Rectangle(10, 11)
rect.width = 20 # => Changes width to 20
print(rect.height) # => Prints rectangle height
```

The `.width = 20` and `rect.height` here are setters and getters, respectively

We can however write our own get and set methods inside the class, using this code:

```py
def set_value(self, value):
    self.value = value

def get_value(self, value):
    return self.value
```
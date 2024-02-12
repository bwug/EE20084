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

    ```py
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

An [interesting stackoverflow page](stackoverflow.com/questions/3917574/how-is-pythons-list-implemented) goes over how python converts arrays into lists</details>

<h2> Lecture 4 - Introduction to sequence, selection and iteration </h2>
<h2> Lecture 5 - Introduction to python functions </h2>
<h2> Lecture 6 - Introduction to python object-oriented programming </h2>
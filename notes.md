<h1> Week 1 </h1>

<br>

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

<br>

<h2> Lecture 2 - Variables and Operators </h2>

<br>

- Variables: In essence, is a name used to refer to some piece of data, these variables are assigned different **data types**

- Data Types: The way we are representing the data, such as a string or integer

- Operators: Tools that manipulate variables and data

<display>
<spoiler> Examples using C </spoiler>

```C
int main ()
{
    int age = 6; // The variable name is "age", the data type is "int" and the value is "6"
    char initial = "H";
    char name = "John"; // Throws an error!
    return 0; // Notice that we are returning an int in an int function
}
```

<display>

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
<h2> Lecture 4 - Introduction to sequence, selection and iteration </h2>
<h2> Lecture 5 - Introduction to python functions </h2>
<h2> Lecture 6 - Introduction to python object-oriented programming </h2>

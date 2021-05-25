# Liner
~~A mistake, probably~~

## What is Liner?
*Liner* is a functional language, designed to solve no problems currently facing us.

In *Liner* each statement is limited to a single line of code. With the *Lineeeee*
number based system. This means that Liner does have a slew of.... features.....

This includes, but is not limited to!

Long files for simple tasks!
No floating point numbers!
No pesky Strings!
Really not a lot of anything!
Recursion.....? Kinda?
Mistakes!
And ***more!***

The included *Liner* Interpreter is made using Python, a programming language worth
learning instead of this one.

## How does one program in Liner?

Programming in *Liner* is simple! Just look in the repo for the `"Hello World"`
example!

---
### Namespace
Namespaces are critical to *Liner* code, without them, nothing can work. For *Liner*
the statement's Namespace is the *unique set of characters at the start of the line.*
These are allowed to be any letter, case-sensitive, as long as it's not a keyword.

*Liner* namespaces are declared with no leading whitespace, and are *immediately*
followed with a semi-colon. Whitespace is considered a unique character, so although
it can be placed inside the namespace, this is frowned on because I'm making the language,
and I say so.

```
C;Examples
Name;
 IllegalName;
Bad Name;
CantUseThisOne;
GoodName;
A;
```

`C` is both considered to be a keyword, and not. Interpreter will skip lines beginning
with `C`, ***this includes any word beginning with C***. This is given to the developer
for the sake of comments. However this practice can be highly debated, and leads
perfectly into the next segment.

### Properties
All namespaces have a numeric property, and is where *Liner* takes it's name from!
In any function, by putting *only* the namespace in a location, you can use the number
line the namespace was declared on. Hence to add the numbers 2 and 3 together, you
could write the following.
```
C; assume this is line 1 of the file
A;
B;
D; A add B
E; prin D()
E()
```
As number line can't go negative, to get a negative number, you'd have to subtract
two numbers. The following would print a negative one.
```
C; assume this is line 1 of the file
A;
B;
D; A sub B
E; prin D()
E()
```

### Functions and Variables

The difference in *Liner* is that there isn't one, kinda.

As the only "real" variable type is the numeric property of the namespace, we have
to get creative. This means a proper *Liner* programmer should be able to understand
how to number good.

Anything after the namespace on the same line is considered to be a function. If
there is nothing there, that namespace can be used to end the program. A function
is anything on the same line, and should only include one keyword. If a function
calls another function, that is assumed to be the return value, which is important
for the `prin` keyword.

### Keywords

* `prin` Prints the results of all the following function, and the numeric value
of any namespace.
* `let` converts an integer into its Unicode character.
* `if` returns the highest number of two different namespaces/function
* `set` override the numeric value of a namespace, and replaces the original in duplicate cases.
* `run` Run the function at the given numeric property, if no function is there, crashes.
* `add` add two numeric properties
* `sub` subtracts two numeric properties
* `split` allows for two function calls on one line.

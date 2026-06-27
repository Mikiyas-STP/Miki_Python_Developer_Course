Java has strict syntax rules and reserved keywords that define its structure. Understanding these early will prevent common errors.

Compilation is the process of converting the Java code you write into a format that your computer can execute. Compile time is when Java checks your code for errors before running your program, which is different from languages like Python or JavaScript that check for errors while the program is actually running. This provides us with the significant benefit of being able to spot (some!) errors without running the code. It also means Java IDEs come with a set of powerful tools to aid development.

Java has two types of data type: primitive and reference. Without going into too much detail right now, primitive types are usually much faster for the computer to deal with and should be used in situations where performance is important. Moreover, the primitive types are the basic ‘building blocks’ of Java and all reference types are ultimately made up of primitive types. You can identify primitive types because they are always in lowercase, unlike reference types which are in UpperCamelCase. The primitive types are defined by the Java language itself and we cannot create any new ones ourselves or change any existing ones. We’ll focus on the following primitive types for now:

int
long
double
boolean
char
Java is a statically typed language, which means that variable types are known at compile time. As such, the type must be provided by the programmer when writing the code. For example, if you are to define a string, you must explicitly state that the variable is of type string:

String myVariable = "hello world";
Self Study
As you read through the resources below try to answer the following questions:

What is a keyword in java?
Choose 3 keywords and explain what they represent
What is meant by the term ‘primitive type’? 
Dynamic typing vs. static typing
This topic is provided for reverence only as it explains the differences between dynamic and static typing. Understanding the differences between dynamic and static typing is key to understanding the way in which transformation script errors are handled, and how it is different from the way Groovy handles errors. This will also help you interpret errors created by your transformation script.

Note: It is important to know that the Groovy implementation within Big Data Discovery enforces static typing. For information on exception handling in Transform, which uses a static parser overriding Groovy's dynamic typing behavior, see Exception handling and troubleshooting your scripts.
There are two main differences between dynamic typing and static typing that you should be aware of when writing transformation scripts.

First, dynamically-typed languages perform type checking at runtime, while statically typed languages perform type checking at compile time. This means that scripts written in dynamically-typed languages (like Groovy) can compile even if they contain errors that will prevent the script from running properly (if at all). If a script written in a statically-typed language (such as Java) contains errors, it will fail to compile until the errors have been fixed.

Second, statically-typed languages require you to declare the data types of your variables before you use them, while dynamically-typed languages do not. Consider the two following code examples:
// Java example
int num;
num = 5;
// Groovy example
num = 5
Both examples do the same thing: create a variable called num and assign it the value 5. The difference lies in the first line of the Java example, int num;, which defines num's data type as int. Java is statically-typed, so it expects its variables to be declared before they can be assigned values. Groovy is dynamically-typed and determines its variables' data types based on their values, so this line is not required.

Dynamically-typed languages are more flexible and can save you time and space when writing scripts. However, this can lead to issues at runtime. For example:
// Groovy example
number = 5
numbr = (number + 15) / 2  // note the typo
The code above should create the variable number with a value of 5, then change its value to 10 by adding 15 to it and dividing it by 2. However, number is misspelled at the beginning of the second line. Because Groovy does not require you to declare your variables, it creates a new variable called numbr and assigns it the value number should have. This code will compile just fine, but may produce an error later on when the script tries to do something with number assuming its value is 10.

Extensions Guide · Version 1.0.0 Revision A · March 2015

Copyright © 2015 Oracle and/or its affiliates. All rights reserved. | Cookie Preferences | Ad Choices.
Java Keywords
Java Reserved Keywords
Java has a set of keywords that are reserved words that cannot be used as variables, methods, classes, or any other identifiers:

Keyword	Description
abstract	A non-access modifier. Used for classes and methods: An abstract class cannot be used to create objects (to access it, it must be inherited from another class). An abstract method can only be used in an abstract class, and it does not have a body. The body is provided by the subclass (inherited from)
assert	For debugging
boolean	A data type that can only store true or false values
break	Breaks out of a loop or a switch block
byte	A data type that can store whole numbers from -128 and 127
case	Marks a block of code in switch statements
catch	Catches exceptions generated by try statements
char	A data type that is used to store a single character
class	Defines a class
continue	Continues to the next iteration of a loop
const	Defines a constant. Not in use - use final instead
default	Specifies the default block of code in a switch statement
do	Used together with while to create a do-while loop
double	A data type that can store fractional numbers from 1.7e−308 to 1.7e+308
else	Used in conditional statements
enum	Declares an enumerated (unchangeable) type
exports	Exports a package with a module. New in Java 9
extends	Extends a class (indicates that a class is inherited from another class)
final	A non-access modifier used for classes, attributes and methods, which makes them non-changeable (impossible to inherit or override)
finally	Used with exceptions, a block of code that will be executed no matter if there is an exception or not
float	A data type that can store fractional numbers from 3.4e−038 to 3.4e+038
for	Create a for loop
goto	Not in use, and has no function
if	Makes a conditional statement
implements	Implements an interface
import	Used to import a package, class or interface
instanceof	Checks whether an object is an instance of a specific class or an interface
int	A data type that can store whole numbers from -2147483648 to 2147483647
interface	Used to declare a special type of class that only contains abstract methods
long	A data type that can store whole numbers from -9223372036854775808 to 9223372036854775808
module	Declares a module. New in Java 9
native	Specifies that a method is not implemented in the same Java source file (but in another language)
new	Creates new objects
package	Declares a package
private	An access modifier used for attributes, methods and constructors, making them only accessible within the declared class
protected	An access modifier used for attributes, methods and constructors, making them accessible in the same package and subclasses
public	An access modifier used for classes, attributes, methods and constructors, making them accessible by any other class
requires	Specifies required libraries inside a module. New in Java 9
return	Finished the execution of a method, and can be used to return a value from a method
short	A data type that can store whole numbers from -32768 to 32767
static	A non-access modifier used for methods and attributes. Static methods/attributes can be accessed without creating an object of a class
strictfp	Obsolete. Restrict the precision and rounding of floating point calculations
super	Refers to superclass (parent) objects
switch	Selects one of many code blocks to be executed
synchronized	A non-access modifier, which specifies that methods can only be accessed by one thread at a time
this	Refers to the current object in a method or constructor
throw	Creates a custom error
throws	Indicates what exceptions may be thrown by a method
transient	Used to ignore an attribute when serializing an object
try	Creates a try...catch statement
var	Declares a variable. New in Java 10
void	Specifies that a method should not have a return value
volatile	Indicates that an attribute is not cached thread-locally, and is always read from the "main memory"
while	Creates a while loop
Note: true, false, and null are not keywords, but they are literals and reserved words that cannot be used as identifiers.
1. Overview
The Java Programming Language features eight primitive data types.

In this tutorial, we’ll look at what these primitives are and go over each type.

2. Primitive Data Types
The eight primitives defined in Java are int, byte, short, long, float, double, boolean and char. These aren’t considered objects and represent raw values.

They’re stored directly on the stack (check out this article for more information about memory management in Java).

We’ll take a look at storage size, default values and examples of how to use each type.

Let’s start with a quick reference:

Type	Size (bits)	Minimum	Maximum	Example
byte	8	-27	27– 1	byte b = 100;
short	16	-215	215– 1	short s = 30_000;
int	32	-231	231– 1	int i = 100_000_000;
long	64	-263	263– 1	long l = 100_000_000_000_000;
float	32	-2-149	(2-2-23)·2127	float f = 1.456f;
double	64	-2-1074	(2-2-52)·21023	double f = 1.456789012345678;
char	16	0	216– 1	char c = ‘c’;
boolean	1	–	–	boolean b = true;
2.1. int
The first primitive data type we’re going to cover is int. Also known as an integer, int type holds a wide range of non-fractional number values.

Specifically, Java stores it using 32 bits of memory. In other words, it can represent values from -2,147,483,648 (-231) to 2,147,483,647 (231-1).

In Java 8, it’s possible to store an unsigned integer value up to 4,294,967,295 (232-1) by using new special helper functions.

We can simply declare an int:

int x = 424_242;

int y;
Copy
The default value of an int declared without an assignment is 0.

If the variable is defined in a method, we must assign a value before we can use it.

We can perform all standard arithmetic operations on ints. Just be aware that decimal values will be chopped off when performing these on integers.

2.2. byte
byte is a primitive data type similar to int, except it only takes up 8 bits of memory. This is why we call it a byte. Because the memory size is so small, byte can only hold the values from -128 (-27) to 127 (27 – 1).

Here’s how we can create byte:

byte b = 100;

byte empty;
Copy
The default value of byte is also 0.

2.3. short
The next stop on our list of primitive data types in Java is short.

If we want to save memory and byte is too small, we can use the type halfway between byte and int: short.

At 16 bits of memory, it’s half the size of int and twice the size of byte. Its range of possible values is -32,768(-215) to 32,767(215 – 1).

short is declared like this:

short s = 20_020;

short s;
Copy
Also similar to the other types, the default value is 0. We can use all standard arithmetic on it as well.

2.4. long
Our last primitive data type related to integers is long.

long is the big brother of int. It’s stored in 64 bits of memory, so it can hold a significantly larger set of possible values.

The possible values of a long are between -9,223,372,036,854,775,808 (-263) to 9,223,372,036,854,775,807 (263 – 1).

We can simply declare one:

long l = 1_234_567_890;

long l;
Copy
As with other integer types, the default is also 0. We can use all arithmetic on long that works on int.

2.5. float
We represent basic fractional numbers in Java using the float type. This is a single-precision decimal number. This means that if we get past six decimal points, the number becomes less precise and more of an estimate.

In most cases, we don’t care about the precision loss. But if our calculation requires absolute precision (e.g., financial operations, landing on the moon, etc.), we need to use specific types designed for this work. For more information, check out the Java class Big Decimal.

This type is stored in 32 bits of memory just like int. However, because of the floating decimal point, its range is much different. It can represent both positive and negative numbers. The smallest decimal is 1.40239846 x 10-45, and the largest value is 3.40282347 x 1038.

We declare floats the same as any other type:

float f = 3.145f;

float f;
Copy
And the default value is 0.0 instead of 0. Also, notice we add the f designation to the end of the literal number to define a float. Otherwise, Java will throw an error because the default type of a decimal value is double.

We can also perform all standard arithmetic operations on floats. However, it’s important to note that we perform floating point arithmetic very differently than integer arithmetic.

2.6. double
Next, we look at double. Its name comes from the fact that it’s a double-precision decimal number.

It’s stored in 64 bits of memory. This means it represents a much larger range of possible numbers than float.

Although, it does suffer from the same precision limitation as float does. The range is 4.9406564584124654 x 10-324 to 1.7976931348623157 x 10308. That range can also be positive or negative.

Declaring double is the same as other numeric types:

double d = 3.13457599923384753929348D;

double d;
Copy
The default value is also 0.0 as it is with float. Similar to float, we attach the letter D to designate the literal as a double.

2.7. boolean
The simplest primitive data type is boolean. It can contain only two values: true or false. It stores its value in a single bit.

However, for convenience, Java pads the value and stores it in a single byte.

Here’s how we declare boolean:

boolean b = true;

boolean b;
Copy
Declaring it without a value defaults to false. boolean is the cornerstone of controlling our programs flow. We can use boolean operators on them (e.g., and, or, etc.).

2.8. char
The final primitive data type to look at is char.

Also called a character, char is a 16-bit integer representing a Unicode-encoded character. Its range is from 0 to 65,535. In Unicode, this represents ‘\u0000’ to ‘\uffff’.

For a list of all possible Unicode values, check out sites such as Unicode Table.

Let’s now declare a char:

char c = 'a';

char c = 65;

char c;
Copy
When defining our variables, we can use any character literal, and they will get automatically transformed into their Unicode encoding for us. A character’s default value is ‘/u0000’.

2.9. Overflow
The primitive data types have size limits. But what happens if we try to store a value that’s larger than the maximum value?

We run into a situation called overflow.

When an integer overflows, it rolls over to the minimum value and begins counting up from there.

Floating point numbers overflow by returning Infinity:

int i = Integer.MAX_VALUE;
int j = i + 1;
// j will roll over to -2_147_483_648

double d = Double.MAX_VALUE;
double o = d + 1;
// o will be Infinity
Copy
Underflow is the same issue except it involves storing a value smaller than the minimum value. When the numbers underflow, they return 0.0.

2.10. Autoboxing
Each primitive data type also has a full Java class implementation that can wrap it. For instance, the Integer class can wrap an int. There is sometimes a need to convert from the primitive type to its object wrapper (e.g., using them with generics).

Luckily, Java can perform this conversion for us automatically, a process called Autoboxing:

Character c = 'c';

Integer i = 1;
Copy
3. Conclusion
In this article, we’ve covered the eight primitive data types supported in Java.

These are the building blocks used by most, if not all, Java programs out there, so it’s well worth understanding how they work.
ava For Loop

Last updated: April 8, 2026


Written by:baeldung

Reviewed by:Grzegorz Piwowarek
Core JavaJava Loops
1. Overview
In this article, we’ll look at a core aspect of the Java language – executing a statement or a group of statements repeatedly using a for loop.

2. Simple for Loop
A for loop is a control structure that allows us to repeat certain operations by incrementing and evaluating a loop counter.

Before the first iteration, the loop counter gets initialized, then the condition evaluation is performed followed by the step definition (usually a simple incrementation).

The syntax of the for loop is:

for (initialization; Boolean-expression; step) 
  statement;
Copy
Let’s see it in a simple example:


for (int i = 0; i < 5; i++) {
    System.out.println("Simple for loop: i = " + i);
}
Copy
The initialization, Boolean-expression, and step used in for statements are optional. Here’s an example of an infinite for loop:

for ( ; ; ) {
    // Infinite for loop
}
Copy
2.1. Labeled for Loops
We can also have labeled for loops. It’s useful if we’ve got nested for loops so that we can break/continue from aspecific for loop:

aa: for (int i = 1; i <= 3; i++) {
    if (i == 1)
      continue;
    bb: for (int j = 1; j <= 3; j++) {
        if (i == 2 && j == 2) {
            break aa;
        }
        System.out.println(i + " " + j);
    }
}
Copy
3. Enhanced for Loop
Since Java 5, we have a second kind of for loop called the enhanced for which makes it easier to iterate over all elements in an array or a collection.

The syntax of the enhanced for loop is:

for(Type item : items)
  statement;
Copy
Since this loop is simplified in comparison to the standard for loop, we need to declare only two things when initializing a loop:


The handle for an element we’re currently iterating over
The source array/collection we’re iterating
Therefore, we can say that: For each element in items, assign the element to the item variable and run the body of the loop.

Let’s have a look at the simple example:

int[] intArr = { 0,1,2,3,4 }; 
for (int num : intArr) {
    System.out.println("Enhanced for-each loop: i = " + num);
}
Copy
We can use it to iterate over various Java data structures:

Given a List<String> list object – we can iterate it:

for (String item : list) {
    System.out.println(item);
}
Copy
We can similarly iterate over a Set<String> set:


for (String item : set) {
    System.out.println(item);
}
Copy
And, given a Map<String,Integer> map we can iterate over it as well:

for (Entry<String, Integer> entry : map.entrySet()) {
    System.out.println(
      "Key: " + entry.getKey() + 
      " - " + 
      "Value: " + entry.getValue());
}
Copy
3.1. Iterable.forEach()
Since Java 8, we can leverage for-each loops in a slightly different way. We now have a dedicated forEach() method in the Iterable interface that accepts a lambda expression representing an action we want to perform.

Internally, it simply delegates the job to the standard loop:

default void forEach(Consumer<? super T> action) {
    Objects.requireNonNull(action);
    for (T t : this) {
        action.accept(t);
    }
}
Copy
Let’s have a look at the example:

List<String> names = new ArrayList<>();
names.add("Larry");
names.add("Steve");
names.add("James");
names.add("Conan");
names.add("Ellen");

names.forEach(name -> System.out.println(name));
Copy
4. Conclusion
In this quick tutorial, we explored Java’s for loop.

The code backing this article is available on GitHub. Once you're logged in as a Baeldung Pro Member, start learning and coding on the project.
✍️Exercise 2.1
Goal: Practice basic syntax and keywords.

Create a program that:

Declares variables of different primitive types (int, double, boolean, char).
Prints their values to the console.
Add comments explaining what each keyword does (e.g., public, static, void).
✍️Exercise 2.2
Goal: Identify and fix compilation errors.

Remove a semicolon or misspell a keyword in your code.
Observe the compilation error in IntelliJ.
Fix the error and re-run the program
✍️Exercise 2.3
Goal: Compare Java control flow with JavaScript.

Write a program that:

Uses a for loop to print numbers 1 to 10.
Uses an if-else statement to check if a number is even or odd.
Bonus: Rewrite the same logic in JavaScript and note the differences in syntax.

✍️Exercise 2.4
Write a program that uses a switch statement to print the name of the day based on an integer (1 = Monday, etc.).
Explain why switch in Java differs from JavaScript (e.g. type safety).
Reflections
Think about the following questions, make notes and be prepared to talk through your thoughts in the workshop.

List the primitive types you’ve seen and explain what they represent
What is an enhanced for loop in Java? Would an enhanced for loop be useful for this exercise? Why? When would an enhanced for loop be useful?
Did you encounter any compilation errors when writing your code? How did you fix them? Did the IDE help?
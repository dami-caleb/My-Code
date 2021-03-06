/*
Now, let me tell you a little more 
about constants in C++. Constants are 
identifiers with values that will not 
change during execution. They are useful as parameters in your 
code. For example, to set the size of a screen, or the length of a 
memory buffer. Constants may be implemented with defined directives, 
or as regular variables. On the one hand, we may create constants with pre-processor directives. 
The #defined directive schedules a find-and-replace operation, so that the code that is sent to the compiler 
has all the instances of the #define symbol replaced by its value. These #define symbols are known as macros. 
An example would be to #define the number of rooms in the house as four. Now, you should be aware that the use of #define is sometimes discouraged, and considered a bad practice. 
That's because macros don't have a context, and there's no compiler enforcement for basic features like types and syntax correctness for macros. Besides, there's a better alternative. 
You can #define regular variables as constants using the const qualifier. This is used in a regular variable declaration. Remember that declarations specify a type, so the compiler will notice any 
irregularities in the code related to the type. Also, scoping capsulation is enforced so you have the order embedded in the language. Lastly, let me give you a warning. 
The const qualifier is not exactly the same in C and C++. The C version only means that a variable cannot change, 
but it lacks most of the features implemented in C++. That's one of the reasons why more common in C than C++
*/

#define age 4; //is is a macro decleration
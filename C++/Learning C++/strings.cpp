//strings are not a native datatype in the c++ language
/*Just like in the C programming language you can represent STRINGS
as an array of characters*/

/*You can also use the C++ string class
The std::string class comes with the C++ standard library
*/

#include <iostream>
#include <string>  //this string header contains the string class
#include <cstring> //this contains functions to handle the charcter array strings (the c infornt means it is part of the c standard library)
using namespace std;

const int MAX = 40;

int main(){

char name[MAX] = "Hey Jenifer! ";
char reply[] = "Hello :) ! "; //Notice we did not specify length


return 0;
}

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

char greeting[MAX] = "Hey Jenifer! ";
char reply[] = "Hello :) ! "; //Notice we did not specify length

string conversation1 = "How was your day?";
string reply1 = "It was great.";


int main(){
    //strcat(greeting,MAX,reply); //This function takes in 3 arguments. Firat "greeting" the destination argument. Second "MAX" the size of the destination string (we are ware the size of greeting is 40). Third "reply" the second array to concatenate
    //not that using "strcat" modifies the first string "greeting" 

    //As for the string class, you can concatenate strings insode the printing line of code
    cout<<conversation1 + " " + reply1<<endl;
return 0;
}

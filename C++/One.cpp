/*
____________________________________________
#include <iostream>
int main(){                              //the main function must return an interger
    std::cout << "Hello, I love pizza" << std::endl;
    return 0;
}
____________________________________________

*/


/*
____________________________________________

#include <iostream>
#include <string>
using namespace std;    //we use this to stop including "std::" everytime we want to "print something out" or recieve input from user 
int main(){
    string str;
    cin >> str;        //"cin" only works for single words
    cout<< str;
    return 0;                  //this code recieves input from a user and prints it out
}
____________________________________________

*/

/*
____________________________________________
//Homework
//Ask a user for his/her name and send a response message 

#include <iostream>
#include <string>
using namespace std;
int main(){
    string user_name;

    cout<< "Hello! My name is Alvin. What is your name?"<<endl;
    cin>>user_name;
    cout<<"Hello " + user_name + "!" +" Welcome to our system!"<<endl;
    
    return 0;
}
____________________________________________
*/

/*
____________________________________________

//solution to homework
#include <iostream>
#include <string>
using namespace std;
int main(){
    string user_name;

    cout<< "Enter your name ";
    cin >> user_name;
    cout<<"Nice to meet you, "<< user_name<<"!"<<endl;   // "<<" are sequences of insertion operations to cout
    return 0;
}

____________________________________________
*/


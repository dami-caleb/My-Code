#include <iostream>
#include <typeinfo>

using namespace std;

int number= 8;
char letter= 'A';

int main(){
 cout<<typeid(number).name()<<endl;
 cout<<typeid(letter).name()<<endl;
 
 return 0;
}

// i= int
//c =char
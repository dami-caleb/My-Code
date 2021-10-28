#include <iostream>

using namespace std;

int a, b=5; //we declared a Global variable //Global variables are accessible to all parts of the code, because of this the meory of a global variable is managed statically by the compiler, so they are allocated in the data segment of memory.//Once the program ends that memory is free

int main(){
    
    bool my_flag;
    
    a =3;
    my_flag = true;

    cout <<"Hello! my anme is Caleb."<<endl;
    cout<<"The value of b-a is "<<b-a<<endl;
    cout<<"The value of b is "<<b<<endl;
    cout<<"The value of my_flag is "<<my_flag<<endl;
    
    return 0;
}

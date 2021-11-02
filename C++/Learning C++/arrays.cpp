//Arrays are collection of data

#include <iostream>
using namespace std;

int four[4];
float temp[] = {2.3,43.4,45.4}; //note that the data type of the array is specified, auto can not be used for arrays
int main(){
    four[0]=4;
    four[1]=8;
    four[2]=16;
    four[3]=420;

    cout <<"4*1 = "<<four[0]<<endl;
    cout <<"4*2 = "<< four[1]<<endl;
    cout <<"4*3 = "<<four[2] <<endl;
    cout <<"4*4 = "<<four[3] <<endl;
    cout<<endl; //this prints an empty line

    cout <<"4*1 = "<<four[0]<<endl;
    cout <<"4*2 = "<< four[1]<<endl;
    cout <<"4*3 = "<<four[2] <<endl;
    cout <<"4*4 = "<<four[3] <<endl;


}
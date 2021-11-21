/*Every time you decleare a variable, the computer creates space for 
it somewhere in memeory. If you decleare a variable inside a function
like main(), the computer will store it in a section of meomry called
the stack. If a variable is decleared outside any function,  it will be
stored in the globals section of memory*/

//If you want to find out the memory address of the variable, you can use the & operator

#include <stdio.h>

int y =1; //the variable y will live in the global section in memory

int  main(){
    int x=3; //the variable x will live in the stack section in memory
    printf("The memory address of the variable x is %p\n", &x);

    return 0;

}
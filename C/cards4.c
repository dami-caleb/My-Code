#include <stdio.h>
#include <stdlib.h>

int main(){

    char card_name[3];
    int count = 0;

    do{
        puts("Enter the card_name: ");
        scanf("%2s", card_name);
        int val = 0;
        switch (card_name[0]){
            case 'K':
            case 'Q':
            case 'J':
                val =10;
                break;
            case 'A':
                val = 11;
                break;
            case 'X':
                continue;
            default:
            val = atoi(card_name);
            if (val<1 || val>10){
                puts("Wrong value.");
                continue;
            }
        }
        if ((val>1) &&(val<7 )) {
            count++;
        }
        else if(val==10){
            count--;
        }
        printf("Current count: %i\n",count);
    }while 
    (card_name[0]!='X');
    

    return 0;
}


/*
1. Switch statements efficently check for multiple values
of a variable
2. Every program needs a main() function
3.You need to complie your C program before you run it
4.You can use the && operator on the command line to run
your program only if it complies
5. -o specifies the output file

1.Si

*/
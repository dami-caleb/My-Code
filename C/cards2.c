#include <stdio.h>
#include <stdlib.h>

int main(){
    char card_name[3];
    puts("Enter the card_name: ");
    scanf("%2s", card_name);

    int val=0;

    switch(card_name[0]){
        case 'K':
        val =10;
        break;

        case 'Q':
        val =10;
        break;

        case 'J':
        val =10;
        break;

        case 'A':
        val =11;
        break;

        default:
        val = atoi(card_name);
    }

    printf("The card value is: %i\n", val);

    if ((val>=3)&&(val<=6)){
        puts("Count has gone up");
    }
    else if (val==10){
        puts("Count has gone down.");
    }

}
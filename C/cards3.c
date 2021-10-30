#include <stdio.h>
#include <stdlib.h>
/*
int main(){
    
    char card_name[3];
    puts("Enter the card_name: ");
    scanf("%2s", card_name);

    int val=0;

    switch(card_name[0]){
        case 'K':
        case 'Q':
        case 'J':
        val =10;
        break;

        case 'A':
        val = 11;
        break;

        default:
        val = atoi(card_name);
    }

return 0;
}
*/

int main(){
    int njh;
     for (njh=1; njh<12;njh++){
         printf("%i is the number of teams currently playing\n",njh);
         
     }
return 0;
}
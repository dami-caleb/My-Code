#include <stdio.h>
#include <signal.h>  //we include this header file to be able to handle signals in C
#include <stdlib.h>
#include <unistd.h>  //By including the <unistd.h> header file we are able to use the sleep function

#define taken 0
#define weakly_taken 1
#define  weakly_not_taken  2
#define  not_taken  3

void signal_handler1(int);
void signal_handler2(int);

int value;



int main(){
    value = 0;
    while(1){
        value = 0; 
        //printf("%d\n",value); //main process (background operation)
        //sleep(5);
        
        signal(SIGINT,signal_handler1);  //when Cmd +c (a signal interupt that kills the terminal)is entered it interupts the main/backgrounnd process
        //signal(SIGALARM,signal_handler1);
    }
    return 0;
}

void signal_handler1(int sig){
     signal(sig,SIG_IGN);//this is to ignore if the command is pressed again
     printf("Hey! Are you sure about this? [Y/N]");
     char user_input;
     user_input = getchar();
     if (user_input == 'y' || user_input == 'Y'){
        int event; 
        int state = weakly_taken; //we assume we are in the weakly_taken state
        int i;
        for(i=0;i<5;i++){     //the for loop is seen as a branch
            //the condition is true for i<0
            //therefore the event is taken
            event = taken;
          
          switch(state){
            
            case taken:
            if(event==0){
                state = taken;
    	        printf("TAKEN\n");
    	        sleep(2); //I have included this function, so we can see the code run in a way we can see it. (we wait for 2 seconds)
            }
            else if(event==3){
                state = weakly_taken;
        	    printf("WEAKLY_TAKEN\n");
        	    sleep(2); 
            }
            break;
            
            
            case weakly_taken:
            if(event==0){
                state = taken;
            	printf("TAKEN\n"); //the state moves from a weakly_taken state to a taken state.
            	sleep(2);
            }
            else if(event==3){
                state = weakly_not_taken;
    	        printf("WEAKLY_NOT_TAKEN\n");
    	       sleep(2);
            }
            break;
            
            
            case weakly_not_taken:
            if(event==0){
                state=weakly_taken;
    	        printf("WEAKLY_TAKEN\n");
    	        sleep(2);
            }
            else if(event==3){
                state=not_taken;
    	        printf("NOT_TAKEN\n");
    	        sleep(2);
            }
            break;
            
            
            case not_taken:
            if(event ==0){
                state = weakly_not_taken;
    	        printf("WEAKLY_NOT_TAKEN\n");
    	        sleep(2);
            }
            else if(event==3){
                state = not_taken;
    	        printf("NOT_TAKEN\n");
    	        sleep(2);
            }
            break;
        }
        
        }
        //we are out of the for loop which means
        //the condition for the loop is no longer true (i.e. i>5)
        //therefore the event moves from "taken" to not_taken
        event = not_taken; //the two bit predictor still predicts we are in the taken state (which is wrong).
        printf("WEAKLY_NOT_TAKEN\n");
    	sleep(2);
        
     }
}
    
 
 
    
   
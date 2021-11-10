int red_LED = 11;
int yellow_LED =9;
int green_LED =5;

int counter =0;

void setup(){

	pinMode(red_LED,OUTPUT);
  	pinMode(yellow_LED,OUTPUT);
  	pinMode(green_LED,OUTPUT);
  
    //it is good practise that all LED's are off before we start using them
  	digitalWrite(red_LED,HIGH);   
    digitalWrite(yellow_LED,LOW);
    digitalWrite(green_LED,LOW);

  	Serial.begin(9600);
  
}

void loop(){

  digitalWrite(red_LED,HIGH);
  digitalWrite(yellow_LED,LOW);
  digitalWrite(green_LED,LOW);
  delay(2000);
  
  digitalWrite(red_LED,LOW);
  digitalWrite(yellow_LED,HIGH);
  digitalWrite(green_LED,LOW);
  delay(500);
  
  digitalWrite(red_LED,LOW);
  digitalWrite(yellow_LED,LOW);
  digitalWrite(green_LED,HIGH);
  delay(1000);
  
  counter++;
  Serial.print("Done with iteration: ");
  Serial.print(counter);
  Serial.print('\n');
  
  
}
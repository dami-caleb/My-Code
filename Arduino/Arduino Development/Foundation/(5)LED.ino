int red_LED = 8;
int counter = 0;

void setup(){
	pinMode(red_LED,OUTPUT);
  	Serial.begin(9600);
}

void loop(){
 	counter = counter+ 100;
 	
  
  	digitalWrite(red_LED,HIGH);
  	delay(1000 -counter);
  	digitalWrite(red_LED,LOW);
  	delay(1000 -counter);
  
  	
    
	String message = "We have blinked: ";
    String message1 = " time(s).";
  	String final_message = message + counter + message1;
    Serial.println(final_message);
  
  	
  	
}
int built_in_LED = 13;
int counter = 0;

void setup(){
	pinMode(built_in_LED, OUTPUT);
  	
  	Serial.begin(9600);
}

void loop(){
	digitalWrite(built_in_LED,HIGH);
  	delay(500);
  	digitalWrite(built_in_LED,LOW);
  	delay(5000);
  
 	counter++;
    
    String message = "We have blinked: ";
    String message1 = " time(s).";
 	String full_message = message + counter + message1;
 	Serial.println(full_message);
}
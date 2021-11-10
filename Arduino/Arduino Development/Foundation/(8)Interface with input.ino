int red_LED = 5;
int push_button = 12;

void setup(){

  	pinMode(red_LED,OUTPUT);	
  
  	pinMode(push_button,INPUT);
  	Serial.begin(96000);
  
}

void loop(){
	
  int push_button_value = digitalRead(push_button);
  
  if(push_button_value==1){
    
    digitalWrite(red_LED,HIGH);
    
  	Serial.print("The button has been pressed and the value is: ");
    Serial.println(push_button_value);
    delay(1); //delay in between reads for stability
  }else{
  	
    digitalWrite(red_LED,LOW);
    
    Serial.print("The button value is: ");
    Serial.println(push_button_value);
    
  }
}
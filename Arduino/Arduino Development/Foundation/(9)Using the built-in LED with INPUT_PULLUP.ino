void setup(){
	pinMode(2,INPUT_PULLUP);
  	pinMode(13,OUTPUT);
  
  	Serial.begin(9600);
}


void loop(){
	int button_value = digitalRead(2);
  	Serial.println(button_value);
  
  if (button_value == HIGH){
  	digitalWrite(13,LOW);
  }else{
  digitalWrite(13,HIGH);
  }


}
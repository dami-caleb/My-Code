int built_in_LED = 13;  //look at the part labelled "L"

void setup(){

  pinMode(built_in_LED,OUTPUT);

}

void loop(){
  digitalWrite(built_in_LED,HIGH);
  delay(500);
  digitalWrite(built_in_LED,LOW);
  delay(500);
}
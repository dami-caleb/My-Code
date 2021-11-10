int red_LED = 5;

void setup(){

  pinMode(red_LED, OUTPUT);
}

void loop(){

  digitalWrite(red_LED,HIGH);
  digitalWrite(red_LED,LOW);
}
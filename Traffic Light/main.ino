#define led1 11
#define led2 12
#define led3 13

void setup() {
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
  Serial.begin(9600);
}

void loop() {
 digitalWrite(led1, HIGH);
 delay(2000);
 digitalWrite(led1, LOW);
  
 digitalWrite(led2, HIGH);
 delay(2000);
 digitalWrite(led2, LOW);
  
 digitalWrite(led3, HIGH);
 delay(2000);
 digitalWrite(led3, LOW);
  
 digitalWrite(led2, HIGH);
 delay(2000);
 digitalWrite(led2, LOW);
  
  
}
/*sketch description: 
Devloper: Santiago Torres
Get temperature and humidity from DHT11 sensor
*/
 #include "DHT.h"
 #define DHTTYPE DHT11
 #define DHTPIN 5

 float temp = 0;
 float hum = 0;


DHT dht(DHTTYPE,DHTPIN );
void setup() {
  // put your setup code here, to run once:
  dht.begin();
  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

temp=dht.readTemperature();
hum=dht.readHumidity();

Serial.print(temp);
Serial.print(",")
Serial.print(hum);
}
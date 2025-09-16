#include <SoftwareSerial.h>
#include <ArduinoJson.h>

#define LED_PIN 13

const char* myName = "uno";  // Replace with the actual device name
const int min_temp = 600;    // For randomly generating test temp value
const int temp_range = 100;

SoftwareSerial mySerial(10, 11); // RX, TX

void blink()
{
  digitalWrite(LED_PIN, HIGH);
  delay(200);
  digitalWrite(LED_PIN, LOW);
  delay(200);
}

void setup() {
  pinMode(LED_PIN, OUTPUT);

  blink();
  blink();
  blink();

  Serial.begin(9600);
  Serial.print("Starting up ");
  Serial.println(myName);
  mySerial.begin(9600);
}

void loop() {
  if (mySerial.available() > 0) {
    String input = mySerial.readStringUntil('\n');
    Serial.println(input);
    blink();

    if (input.length() > 0) {
      StaticJsonDocument<256> doc;  // Adjust size if needed for larger JSON
      DeserializationError error = deserializeJson(doc, input);
      
      blink();

      if (error) {
          digitalWrite(LED_PIN, HIGH);
          delay(1000);
          digitalWrite(LED_PIN, LOW);
        return;
      }
      
      const char* destination = doc["destination"];
      if (destination && strcmp(destination, myName) == 0) {

        blink();
        Serial.println("  Destination is me");

        float fake_value = (min_temp + random(0, temp_range)) * 0.1;

        StaticJsonDocument<256> response;
        response["source"] = myName;
        response["destination"] = "hub";
        response["temperature"] = fake_value;
        
        char response_buffer[256];

        serializeJson(response, response_buffer, 256);

        Serial.print(response_buffer);
        Serial.print("\r\n");

        mySerial.print(response_buffer);
        mySerial.print("\r\n");
      } 
      else
      {
          digitalWrite(LED_PIN, HIGH);
          delay(4000);
          digitalWrite(LED_PIN, LOW);
      }
    }
  }
}
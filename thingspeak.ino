#include <ThingSpeak.h>

#include <WiFi.h>
const char *apiKey = "BPHSL7MQU3FR9GMD";                  //  Enter your Write API key from ThingSpeak
const char *ssid =  "HP Trizon";                                    // replace with your wifi ssid and wpa2 key
const char *pass =  "isit@pass";
const char* server = "api.thingspeak.com";
unsigned long channelNum = 874548;

WiFiClient client;
void setup() 
{
    Serial.begin(115200);
    delay(10);
    Serial.println("Connecting to ");
    Serial.println(ssid);
    WiFi.begin(ssid, pass);
    while (WiFi.status() != WL_CONNECTED) 
    {
        delay(500);
        Serial.print(".");
    }
    Serial.println("");
    Serial.println("WiFi connected");
    ThingSpeak.begin(client);
 
}
void loop() 
{
  
int h = 0;
float t =0;

h = random(0,69);
t = random(0,100);

    ThingSpeak.setField(1, h);
    ThingSpeak.setField(2, t);
    ThingSpeak.writeFields(channelNum, apiKey);

    Serial.print("Sensed: ");
    Serial.println(h);
    Serial.print("Temperature:");
    Serial.print(t);
    Serial.println(" C");
    delay(5000);
}
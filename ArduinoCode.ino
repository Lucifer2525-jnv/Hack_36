#include <SoftwareSerial.h> 
#include <TinyGPS.h>      //Needs to be imported if required

TinyGPS gps;  

float lat = -1.6848579,lon = 37.1690756; 



SoftwareSerial mySerial(9, 10); //TX & RX

void setup()
{
  mySerial.begin(9600);   // Setting the baud rate of GSM Module  
  Serial.begin(9600);    // Setting the baud rate of Serial Monitor (Arduino)
  Serial.println("Welcome.");
  Serial.println("......................");
  Serial.println();
  delay(100);
}


void loop()
{
  
  
  if (Serial.available()>0)
   switch(Serial.read())
  {
    case 's':
    case 'S':
      mySerial.println("AT+CMGF=1");    
     delay(1000);  // Delay of 1 second
     mySerial.println("AT+CMGS=\"+9173********\"\r"); //Receiver Number
     delay(1000);
     Serial.println();
     Serial.println("Name: Harshit Chaudhary");
     Serial.println("......................");
     Serial.println("Your location....");
     Serial.println(gps_connect());
     Serial.println("......................");
     Serial.println("Area");
     Serial.println("75m2");
     Serial.println("......................");
     Serial.println("I am in Trouble and Urgently need your help at sended location");// sended message
     Serial.println("......................");
     Serial.println("Total People around");
     Serial.println("5 or depends");
     Serial.println();
     delay(100);
     mySerial.println((char)26);// Termination Code of sms to  the module 
      delay(1000);
      break;



      
    case 'r':
    case 'R':
      mySerial.println("AT+CNMI=2,2,0,0,0"); // AT Command to receive a live SMS
      delay(1000);
      break;
  }

 if (mySerial.available()>0)
   Serial.write(mySerial.read());
}


float gps_connect() {
  while (Serial.available()) { // check for gps data
    if (gps.encode(Serial.read())) // encode gps data
    {
      gps.f_get_position(&lat, &lon); // get latitude and longitude
      // display position

    }
  }

  String latitude = String(lat, 6);
  String longitude = String(lon, 6);
  Serial.println("Latitude: " + latitude + "," "Longitude: " + longitude);
  delay(1000);
}

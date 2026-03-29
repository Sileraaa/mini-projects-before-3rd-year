/*
 * PROJECT: ESP32 DHT11 + SSD1306 OLED Monitor
 * HARDWARE: ESP32 Dev Module, DHT11 (GPIO 4), OLED (SDA: 21, SCL: 18)
 * LIBRARIES: Adafruit_SSD1306, Adafruit_GFX, DHT_Sensor_Library
 */

#include <Wire.h>             // Handles I2C communication (Master/Slave protocol)
#include <Adafruit_GFX.h>      // Core graphics library for drawing shapes/text
#include <Adafruit_SSD1306.h>   // Hardware-specific driver for the SSD1306 OLED
#include "DHT.h"              // Logic to decode the DHT11's pulse-width signal

// --- OLED HARDWARE CONSTANTS ---
#define SCREEN_WIDTH 128      // OLED display width, in pixels
#define SCREEN_HEIGHT 64      // OLED display height, in pixels
#define OLED_RESET    -1      // Reset pin (Set to -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C   // Standard I2C address for 0.96" OLEDs

// Create the 'display' object using the parameters defined above
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// --- DHT11 HARDWARE CONSTANTS ---
#define DHTPIN 4              // The Digital Pin connected to the DHT11 Data pin
#define DHTTYPE DHT11         // Defining the sensor type for the library
DHT dht(DHTPIN, DHTTYPE);     // Initialize DHT object

void setup() {
  // Initialize Serial communication for debugging at 115200 baud
  Serial.begin(115200);

  // 1. Start the DHT11 Sensor
  dht.begin();

  // 2. Custom I2C Initialization
  // This tells the ESP32 to ignore default SCL (22) and use Pin 18 instead.
  // Wire.begin(SDA_PIN, SCL_PIN);
  Wire.begin(21, 18);

  // 3. Initialize the OLED Display
  // SSD1306_SWITCHCAPVCC = uses internal 3.3V to generate high voltage for LEDs
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed. Check D21/D18 wiring!"));
    for(;;); // Don't proceed, loop forever (Safety "Kernel Panic")
  }

  // Clear the buffer and show a blank screen to start
  display.clearDisplay();
  display.display();
  
  Serial.println(F("System Online..."));
}

void loop() {
  // DHT11 is slow; it needs ~2 seconds between readings to stabilize
  delay(2000);

  // --- DATA ACQUISITION ---
  // readTemperature() and readHumidity() return 'float' (decimal) values
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // --- ERROR HANDLING ---
  // isnan = "Is Not A Number". Validates if the sensor data is corrupted.
  if (isnan(h) || isnan(t)) {
    Serial.println(F("Critical Error: DHT11 Sensor Disconnected!"));
    return; // Exit loop early and try again in 2 seconds
  }

  // --- RENDERING (The "Painting" Process) ---
  
  // A. Clear the "Canvas" (Internal RAM buffer)
  display.clearDisplay(); 

  // B. Draw Header Line
  display.setTextSize(1);      // Scale 1 = 8 pixels high
  display.setTextColor(SSD1306_WHITE); 
  display.setCursor(25, 0);    // (x, y) placement
  display.println("MAPUA MONITOR");
  display.drawLine(0, 10, 128, 10, SSD1306_WHITE); // Horizontal separator

  // C. Display Temperature using snprintf (Formatted String)
  // We create a character array (buffer) to hold our formatted text
  char tempStr[20];
  // %.1f means "Float with 1 decimal place"
  snprintf(tempStr, sizeof(tempStr), "TEMP: %.1f C", t);
  
  display.setTextSize(1);
  display.setCursor(0, 25);
  display.print(tempStr);

  // D. Display Humidity
  char humStr[20];
  // %.0f means "Float rounded to nearest whole number"
  snprintf(humStr, sizeof(humStr), "HUMID: %.0f %%", h);
  
  display.setCursor(0, 45);
  display.print(humStr);

  // E. Commit to Hardware
  // This pushes everything from the ESP32 RAM to the OLED glass via I2C.
  display.display(); 
}
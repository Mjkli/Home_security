#include <BLEDevice.h>
#include <BLEServer.h>
#include <BLEUtils.h>
#include <BLE2902.h>

BLEServer* pServer = NULL;
BLECharacteristic* pCharacteristic = NULL;
bool deviceConnected = false;
bool oldDeviceConnected = false;
bool val = true;
const int REED_PIN = 2;
const int LED_PIN = 13;



class serverCallbacks: public BLEServerCallbacks {
    void onConnect(BLEServer* pServer){
        deviceConnected = true;
    }

    void onDisconnect(BLEServer* pServer){
        deviceConnected = false;
    }
};


void setup() {
  Serial.begin(115200);

  // Create the BLE Server
  BLEDevice::init("ESP32_Server");
  pServer = BLEDevice::createServer();

  // Create the BLE Service
  BLEService *pService = pServer->createService(BLEUUID("4fafc201-1fb5-459e-8fcc-c5c9c331914b"));

  // Create a BLE Characteristic
  pCharacteristic = pService->createCharacteristic(
                     BLEUUID("beb5483e-36e1-4688-b7f5-ea07361b26a8"),
                     BLECharacteristic::PROPERTY_NOTIFY |
                     BLECharacteristic::PROPERTY_READ |
                     BLECharacteristic::PROPERTY_WRITE |
                     BLECharacteristic::PROPERTY_INDICATE
                   );

  // Create a BLE Descriptor
  pCharacteristic->addDescriptor(new BLE2902());

  // Start the service
  pService->start();

  // Start advertising
  pServer->getAdvertising()->start();

  pinMode(REED_PIN, INPUT_PULLUP);
  pinMode(LED_PIN, OUTPUT);

}

void loop() {
  int proximity = digitalRead(REED_PIN);
  sleep(1);
  if(proximity == LOW){
    Serial.println("Switch closed");
    digitalWrite(LED_PIN, HIGH);
    pCharacteristic->setValue((uint8_t*)&val, 0);
  }
  else{
    Serial.println("Switch Open");
    digitalWrite(LED_PIN, LOW);
    pCharacteristic->setValue((uint8_t*)&val, 1);
  }

  Serial.println(val);
  pCharacteristic->notify();
  delay(5000); // Adjust delay as needed
}

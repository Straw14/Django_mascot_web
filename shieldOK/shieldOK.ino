#include <SoftwareSerial.h>
#include <SPI.h>
#include <WiFi.h>
SoftwareSerial BT(8, 9);
int rss1,rss2,rss3;

void setup() {                      //初始化串口並等待端口打開：初始化串口並等待端口打開：
  
  Serial.begin(9600);
  BT.begin(9600);
  while (!Serial) { ; }              // 等待串口連接。只需要本地USB端口等待串口連接。只需要本地USB端口
    
  
  if (WiFi.status() == WL_NO_SHIELD) {      // 檢查屏蔽的存在：檢查屏蔽的存在：
    Serial.println("WiFi shield not present");
    // don't continue:
    while (true);
  }


  String fv = WiFi.firmwareVersion();
  Serial.println("your Version : "+fv);
  
  if (fv != "1.1.0") {
    Serial.println("Please upgrade the firmware");
  }
  printMacAddress();                // 打印WiFi MAC地址：
  
}

  ////////////////////////////////////////////////////////////////////////////////////////

void loop() {
  //掃描現有網絡：掃描現有網絡：
  Serial.println("\nScanning available networks...");
  listNetworks();
  delay(5000);
byte Data[4];
Data[0]=97;
Data[1]=rss1;
Data[2]=rss2;
Data[3]=rss3;

 if(BT.available() > 0) //check BT is succeed
    if(BT.read() == 97) //check recieve key from phone
    {
      BT.write(Data[0]);
      BT.write(Data[1]);
      BT.write(Data[2]);
      BT.write(Data[3]);
    }
   
 }



void printMacAddress() {    //你的Wifi擴充版的MAC地址
  byte mac[6];              // 打印您的MAC地址： 
  WiFi.macAddress(mac);       //mac 是一個大小為 6 位元組的陣列，macAddress() 執行完後，
                                             
  Serial.print("MAC: ");     //會把 WiFi Shield 的 MAC 位址放到 mac 裡
  Serial.print(mac[5], HEX);
  Serial.print(":");
  Serial.print(mac[4], HEX);
  Serial.print(":");
  Serial.print(mac[3], HEX);
  Serial.print(":");
  Serial.print(mac[2], HEX);
  Serial.print(":");
  Serial.print(mac[1], HEX);
  Serial.print(":");
  Serial.println(mac[0], HEX);
}



void listNetworks() {             // 搜尋附近的訊號源
  Serial.println("** Scan Networks **");
  int numSsid = WiFi.scanNetworks();
  String ssum;
  if (numSsid == -1) {
    Serial.println("Couldn't get a wifi connection");  //沒有搜尋到ＷＩＦＩ
    while (true);
  }

  
  Serial.print("number of available networks:");  //打印看到的網絡列表：
  Serial.println(numSsid);

  // 打印找到的每個網絡的網絡號和名稱
for (int thisNet = 0; thisNet < numSsid; thisNet++) {
    String ssi=WiFi.SSID(thisNet);
    
    
    if (ssi == "STRAW" ){
    rss1=WiFi.RSSI(thisNet);
    Serial.print("(");
    Serial.print(thisNet);               //搜尋到的第 x 個
    Serial.print(") ");
    Serial.print(WiFi.SSID(thisNet));  //搜尋到的第 x 個ap的名稱（ＳＳＩＤ
    Serial.print("\t訊息: ");
    Serial.print(WiFi.RSSI(thisNet));  //搜尋到的第 x 個ap的距離
    Serial.print(" dBm");
    Serial.print("\t加密方式: ");       //搜尋到的第 x 個ap的加密類型
    printEncryptionType(WiFi.encryptionType(thisNet)); 
    Serial.println(rss1);
    }


    if (ssi == "STRAW2" ){
    rss2=WiFi.RSSI(thisNet);
    Serial.print("(");
    Serial.print(thisNet);     
    Serial.print(") ");
    Serial.print(WiFi.SSID(thisNet));  
    Serial.print("\t訊息: ");
    Serial.print(WiFi.RSSI(thisNet)); 
    Serial.print(" dBm");
    Serial.print("\t加密方式: ");    
    printEncryptionType(WiFi.encryptionType(thisNet));
    Serial.println(rss2);
    } 


    if (ssi == "STRAW3" ){
    rss3=WiFi.RSSI(thisNet);
    Serial.print("(");
    Serial.print(thisNet);     
    Serial.print(") ");
    Serial.print(WiFi.SSID(thisNet));  
    Serial.print("\t訊息: ");    
    Serial.print(WiFi.RSSI(thisNet)); 
    Serial.print(" dBm");
    Serial.print("\t加密方式: ");    
    printEncryptionType(WiFi.encryptionType(thisNet));
    Serial.println(rss3);
    }  

    
  }   
}

void printEncryptionType(int thisType) {
  //讀取加密類型並打印出名稱：
  switch (thisType) {
    case ENC_TYPE_WEP:
      Serial.println("WEP");
      break;
    case ENC_TYPE_TKIP:
      Serial.println("WPA");
      break;
    case ENC_TYPE_CCMP:
      Serial.println("WPA2");
      break;
    case ENC_TYPE_NONE:
      Serial.println("None");
      break;
    case ENC_TYPE_AUTO:
      Serial.println("Auto");
      break;
  }
}




void setup() {
  //  copyright 

  Serial.begin(9600);
  Serial.println("1Started Arduino");

}

void loop() {

  if (Serial.readString() == "print-done") {
   // Exeute motors etc 

   delay(1000);

   Serial.println("1select-print");

   delay (2000);
   Serial.println("1start-print");

   
   

    
  }


}

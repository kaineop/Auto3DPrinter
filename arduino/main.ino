void setup() {
  //  copyright 

  Serial.begin(9600);
  
  Serial.println("1Started Arduino");

}

void loop() {


 while(Serial.available() > 0 ){
    String str = Serial.readString();
    if(str.indexOf("printdone") > -1){
      Serial.println("G1 Y5 F250");
   // Exeute motors etc 
       
   delay(1000);

   Serial.println("1select-print");

   delay (2000);
   Serial.println("1start-print");

    } else {
      Serial.println("unknown");
    }
  }


    
   

   
   

    
  }



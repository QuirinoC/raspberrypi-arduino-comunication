int pin = 8;
int flagPin = 10;
void setup() {
  // put your setup code here, to run once:
  pinMode(pin, INPUT);
  pinMode(flagPin, INPUT_PULLUP);
   
  Serial.begin(9600);
}

int read(int a, int b, int c, int d) {
  return d * 1 +
         c * 2 +
         b * 4 +
         a * 8;
}
int readBin(int d) {
  
}
char hex(int val) {
  switch (val) {
    case 0: return '0'; case 1: return '1'; case 2: return '2'; case 3: return '3';
    case 4: return '4'; case 5: return '5'; case 6: return '6'; case 7: return '7';
    case 8: return '8'; case 9: return '9'; case 10: return 'a'; case 11: return 'b';
    case 12: return 'c'; case 13: return 'd'; case 14: return 'e'; case 15: return 'f';

  }
}

int val;
char hexVal;
boolean flag;
int binHex[] = {0,0,0,0};
int counter = 0;
String string;
int charcounter = 0;
char text(char c) {
  int offset = 4;
}


void loop() {
  // put your main code here, to run repeatedly:
   flag = digitalRead(flagPin);
  if (flag) {//flag) {
    binHex[counter++] = digitalRead(pin);
    if(counter == 4) {
      Serial.print(hex(read(binHex[0],binHex[1],binHex[2],binHex[3])));
      Serial.print(" ");
      //charcounter++;
      //if(charcounter == 4) { Serial.println(); charcounter = 0;}
      counter = 0;
    }
    delay(8);
  }
}


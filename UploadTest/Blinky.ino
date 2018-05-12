void setup(){
    pinMode(13, OUTPUT);
    Serial.begin(9600);
}

void loop(){
    digitalWrite(13, HIGH);
    delay(1000);
    degitalWrite(13, LOW);
    delay(1000);
}
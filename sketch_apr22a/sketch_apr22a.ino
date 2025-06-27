const int redLed = 9;     // Frontal Lobe (Speech) - Red
const int greenLed = 10;  // Occipital Lobe (Vision) - Green
const int blueLed = 11;   // Temporal Lobe (Hearing) - Blue
const int whiteLed = 12;  // Motor Cortex (Movement) and Olfactory Bulb (Smell) - White (Can be tested with pin 7: const int whiteLed = 7;)
const int yellowLed = 8;  // Thalamus - Yellow

void setup() {
  Serial.begin(9600);
  Serial.setTimeout(100);
  pinMode(redLed, OUTPUT);
  pinMode(greenLed, OUTPUT);
  pinMode(blueLed, OUTPUT);
  pinMode(whiteLed, OUTPUT);
  pinMode(yellowLed, OUTPUT);

  digitalWrite(redLed, LOW);
  digitalWrite(greenLed, LOW);
  digitalWrite(blueLed, LOW);
  digitalWrite(whiteLed, LOW);
  digitalWrite(yellowLed, LOW);

  // Initial test: Turn on each LED for 0.5 seconds
  Serial.println("LED Test Starting...");
  Serial.println("Yellow LED (Thalamus) test...");
  digitalWrite(yellowLed, HIGH); delay(500); digitalWrite(yellowLed, LOW); delay(100);
  Serial.println("Red LED (Speech) test...");
  digitalWrite(redLed, HIGH); delay(500); digitalWrite(redLed, LOW); delay(100);
  Serial.println("Green LED (Vision) test...");
  digitalWrite(greenLed, HIGH); delay(500); digitalWrite(greenLed, LOW); delay(100);
  Serial.println("Blue LED (Hearing) test...");
  digitalWrite(blueLed, HIGH); delay(500); digitalWrite(blueLed, LOW); delay(100);
  Serial.println("White LED (Movement/Smell) test...");
  digitalWrite(whiteLed, HIGH); delay(500); digitalWrite(whiteLed, LOW); delay(100);
  Serial.println("Test Completed. Waiting for command (S, V, H, M, O)");
}

void turnOffAllLeds() {
  digitalWrite(redLed, LOW);
  digitalWrite(greenLed, LOW);
  digitalWrite(blueLed, LOW);
  digitalWrite(whiteLed, LOW);
  digitalWrite(yellowLed, LOW);
}

void blinkThalamus() {
  for (int i = 0; i < 10; i++) {
    digitalWrite(yellowLed, HIGH);
    delay(50);
    digitalWrite(yellowLed, LOW);
    delay(50);
  }
}

void blinkLed(int ledPin) {
  for (int i = 0; i < 5; i++) {
    digitalWrite(ledPin, HIGH);
    delay(100);
    digitalWrite(ledPin, LOW);
    delay(100);
  }
}

void processCommand(String input) {
  input.trim();
  Serial.print("Command received: ");
  Serial.println(input);

  char command = toupper(input[0]);
  turnOffAllLeds();

  switch (command) {
    case 'S':
      Serial.println("Thalamus -> Speech: Yellow (fast blinking) -> Red LED (blinking)");
      blinkThalamus();
      blinkLed(redLed);
      Serial.println("OK");
      break;
    case 'V':
      Serial.println("Thalamus -> Vision: Yellow (fast blinking) -> Green LED (blinking)");
      blinkThalamus();
      blinkLed(greenLed);
      Serial.println("OK");
      break;
    case 'H':
      Serial.println("Thalamus -> Hearing: Yellow (fast blinking) -> Blue LED (blinking)");
      blinkThalamus();
      blinkLed(blueLed);
      Serial.println("OK");
      break;
    case 'M':
      Serial.println("Thalamus -> Movement: Yellow (fast blinking) -> White LED (blinking)");
      blinkThalamus();
      blinkLed(whiteLed);
      Serial.println("OK");
      break;
    case 'O':
      Serial.println("Olfactory Bulb -> Smell: White LED (blinking)");
      blinkLed(whiteLed);
      Serial.println("OK");
      break;
    default:
      Serial.println("Invalid command!");
      break;
  }
}

void loop() {
  if (Serial.available() > 0) {
    String input = Serial.readStringUntil('\n');
    processCommand(input);
    while (Serial.available() > 0) {
      Serial.read();
    }
  }
}
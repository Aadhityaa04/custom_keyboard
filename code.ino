#include <HID-Project.h> 

// Define pin constants
const int SW1 = 7;
const int SW2 = 4;
const int SW3 = 2;
const int SW4 = 14;
const int SW5 = 15;
const int SW6 = 18;
const int SW7 = 8;
const int SW8 = 10;
const int SW9 = 16;
#define CLK 3
#define DT 5
#define SW A1
#define LED_ZOOM A2
#define LED_VOLUME A3

// Variables to hold the last state of the buttons
bool lastStateSW1 = HIGH;
bool lastStateSW2 = HIGH;
bool lastStateSW3 = HIGH;
bool lastStateSW4 = HIGH;
bool lastStateSW5 = HIGH;
bool lastStateSW6 = HIGH;
bool lastStateSW7 = HIGH;
bool lastStateSW8 = HIGH;
bool lastStateSW9 = HIGH;
int counter = 0;
int currentStateCLK;
int lastStateCLK;
int btnstate = 0;
String currentDir = ;
unsigned long lastButtonPress = 0;
const unsigned long debounceDelay = 50;
bool buttonPressed = false;

void setup() {
	Serial.begin(9600);
	Keyboard.begin();
	Consumer.begin();

	pinMode(SW1, INPUT_PULLPU);
	pinMode(SW2, INPUT_PULLPU);
	pinMode(SW3, INPUT_PULLPU);
	pinMode(SW4, INPUT_PULLPU);
	pinMode(SW5, INPUT_PULLPU);
	pinMode(SW6, INPUT_PULLPU);
	pinMode(SW7, INPUT_PULLPU);
	pinMode(SW8, INPUT_PULLPU);
	pinMode(SW9, INPUT_PULLPU);
	pinMode(CLK, INPUT);
	pinMode(DT, INPUT);
	pinMode(SW, INPUT_PULLUP);
	pinMode(LED_ZOOM, OUTPUT);
	pinMode(LED_VOLUME, OUTPUT);
	lastStateCLK = digitalRead(CLK);
}

void loop() {
	bool currentStateSW1 = digitalRead(SW1);
	bool currentStateSW2 = digitalRead(SW2);
	bool currentStateSW3 = digitalRead(SW3);
	bool currentStateSW4 = digitalRead(SW4);
	bool currentStateSW5 = digitalRead(SW5);
	bool currentStateSW6 = digitalRead(SW6);
	bool currentStateSW7 = digitalRead(SW7);
	bool currentStateSW8 = digitalRead(SW8);
	bool currentStateSW9 = digitalRead(SW9);


	// Check if button SW1 was pressed
	if (currentStateSW1 == LOW && lastStateSW1 == HIGH) {
		Keyboard.press(KEY_ESC);
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW2 was pressed
	if (currentStateSW2 == LOW && lastStateSW2 == HIGH) {
		Keyboard.press(KEY_LEFT_ALT);
		Keyboard.press(KEY_TAB);
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW3 was pressed
	if (currentStateSW3 == LOW && lastStateSW3 == HIGH) {
		Keyboard.press(KEY_LEFT_CTRL);
		Keyboard.press('c');
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW4 was pressed
	if (currentStateSW4 == LOW && lastStateSW4 == HIGH) {
		Keyboard.press(KEY_LEFT_CTRL);
		Keyboard.press('v');
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW5 was pressed
	if (currentStateSW5 == LOW && lastStateSW5 == HIGH) {
		Keyboard.press(KEY_PAGE_UP);
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW6 was pressed
	if (currentStateSW6 == LOW && lastStateSW6 == HIGH) {
		Keyboard.press(KEY_LEFT_CTRL);
		Keyboard.press('z');
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW7 was pressed
	if (currentStateSW7 == LOW && lastStateSW7 == HIGH) {
		Keyboard.press(KEY_UP_ARROW);
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW8 was pressed
	if (currentStateSW8 == LOW && lastStateSW8 == HIGH) {
		Keyboard.press(KEY_PAGE_DOWN);
		delay(100);
		Keyboard.releaseAll();
	}

	// Check if button SW9 was pressed
	if (currentStateSW9 == LOW && lastStateSW9 == HIGH) {
		Keyboard.press(KEY_DOWN_ARROW);
		delay(100);
		Keyboard.releaseAll();
	}
	// Update the last state of each button
	lastStateSW1 = currentStateSW1;
	lastStateSW2 = currentStateSW2;
	lastStateSW3 = currentStateSW3;
	lastStateSW4 = currentStateSW4;
	lastStateSW5 = currentStateSW5;
	lastStateSW6 = currentStateSW6;
	lastStateSW7 = currentStateSW7;
	lastStateSW8 = currentStateSW8;
	lastStateSW9 = currentStateSW9;

	currentStateCLK = digitalRead(CLK);
	if (currentStateCLK != lastStateCLK && currentStateCLK == 1) {
		if (digitalRead(DT) != currentStateCLK) {
			counter--;
			currentDir = "CCW";
		} else {
			counter++;
			currentDir = "CW";
		}

		Serial.print("Direction: ");
		Serial.print(currentDir);
		Serial.print(" | Counter: ");
		Serial.println(counter);}

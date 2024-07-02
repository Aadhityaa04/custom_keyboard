#include <HID-Project.h> 

// Define pin constants
const int SW1 = 7;
const int SW2 = 4;
const int SW3 = 2;
const int SW4 = 14;
const int SW5 = 15;
const int SW6 = 18;
const int SW7 = 8;

// Variables to hold the last state of the buttons
bool lastStateSW1 = HIGH;
bool lastStateSW2 = HIGH;
bool lastStateSW3 = HIGH;
bool lastStateSW4 = HIGH;
bool lastStateSW5 = HIGH;
bool lastStateSW6 = HIGH;
bool lastStateSW7 = HIGH;

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
}

void loop() {
	bool currentStateSW1 = digitalRead(SW1);
	bool currentStateSW2 = digitalRead(SW2);
	bool currentStateSW3 = digitalRead(SW3);
	bool currentStateSW4 = digitalRead(SW4);
	bool currentStateSW5 = digitalRead(SW5);
	bool currentStateSW6 = digitalRead(SW6);
	bool currentStateSW7 = digitalRead(SW7);

	if (currentStateSW1 == LOW && lastStateSW1 == HIGH) {
		Keyboard.press(ctrl+shift+s);
		delay(100);
		Keyboard.releaseAll();
		}
	if (currentStateSW2 == LOW && lastStateSW2 == HIGH) {
		Keyboard.press(ctrl+shift+c);
		delay(100);
		Keyboard.releaseAll();
		}
	if (currentStateSW3 == LOW && lastStateSW3 == HIGH) {
		Keyboard.press(win+shift+s);
		delay(100);
		Keyboard.releaseAll();
		}
	if (currentStateSW4 == LOW && lastStateSW4 == HIGH) {
		Keyboard.press(win+shift+c);
		delay(100);
		Keyboard.releaseAll();
		}
	if (currentStateSW5 == LOW && lastStateSW5 == HIGH) {
		Keyboard.press(win+shift+v);
		delay(100);
		Keyboard.releaseAll();
		}
	if (currentStateSW6 == LOW && lastStateSW6 == HIGH) {
		Keyboard.press(ctrl+tab);
		delay(100);
		Keyboard.releaseAll();
		}
	if (currentStateSW7 == LOW && lastStateSW7 == HIGH) {
		Keyboard.press(win+i);
		delay(100);
		Keyboard.releaseAll();
		}
}

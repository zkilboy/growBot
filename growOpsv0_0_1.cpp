// For RAMPS 1.4
#define X_STEP_PIN         54
#define X_DIR_PIN          55
#define X_ENABLE_PIN       38
#define X_MIN_PIN           3
#define X_MAX_PIN          -1 
//PIN 2 is used

//extruder 1
#define E0_STEP_PIN        26
#define E0_DIR_PIN         28
#define E0_ENABLE_PIN      24

//extruder 2
#define E1_STEP_PIN        36
#define E1_DIR_PIN         34
#define E1_ENABLE_PIN      30


#define SDPOWER            -1

//ChipSelect, Hardware SS Pin on Mega, 10 for Arduino Boards, always kept as output
#define SDCS_PIN           53
#define SD_DETECT_PIN 	   -1 
//currently not implemented


#define LED_PIN            13

#define FAN_PIN            9

#define PS_ON_PIN          12	
//ATX , awake=LOW, SLEEP=High
#define KILL_PIN           -1
# Guptchar Gupta

A project to create a fun radar mapping experience using a Telegram Bot.

## Getting Started
Follow these steps to set up the project.

### Hardware Requirements
- Arduino Uno Board
- HC-SR04 ultrasonic sensor
- Servo Motor
- Hook-up wires

Assemble the components as per the [Circuit SKetch](https://www.tinkercad.com/things/7t5C7JmpB24-ultrasonicsensor-arduino?sharecode=GbAvTnyDOwDsA554NyLcmwE2JXSzjM35oGXpE17ET6M).

- Compile and upload the code from `sketch.ino`.
- Download and install [Processing IDE](https://processing.org/). Run the code from `./processing/processing.pde` in Processing IDE.
- Create a Telegram bot and obtain the bot token.
- Create a `.env` file and and add your bot token in the following format:
  ```
  BOT_TOKEN="YOUR TOKEN HERE"
  ```
- Install the necessary dependencies with `pip install -r requirements.txt`.
- Start the bot using `python main.py`.


Thanks
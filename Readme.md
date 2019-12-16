# Getting Started #

## Follow the following guide to install GPIO Libraries: ##
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi

## Follow the following guide to install NeoPixel Libraries: ##
Wiring diagram can also be found at the following link
https://learn.adafruit.com/neopixels-on-raspberry-pi/python-usage

## How to Run ##
In order to initialize the lights, run the following command from the project directory
`sudo python3 lights.py`
The reason for running the lights using sudo is due to the lights being connected via GPIO headers. As a result, the underlying neopixels library requires the use of sudo.

Apollo 49 is a high amateur rocket built by the Charlotte rocketry club at UNC Charlotte. This repository is the home of the flight code running on the payload and the data gathered by that payload.

# Hardware

The payload on Apollo consists of a BAM390, MPU6050, a micro-SD card reader, 4 digit 7-segment display, 1 momentary power buttom switch and a remote RF switch all controlled by an Arduino Nano. It is powered by 2 18650 Li-Ion batteries wired in series, connected to a 5V buck converter and a master power switch.

# Software
The software controling the payload is hand writen, inspired by the code that came with the examples form the libraries, unless otherwise specified in the comments. No Gen-AI was used to make the payload.

# Post processing
The post processing done here is done to better visulize and understand the flight path the rocket took during flight.
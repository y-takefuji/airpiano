# What is airpiano? 
[![Open in Code Ocean](https://codeocean.com/codeocean-assets/badge/open-in-code-ocean.svg)](https://codeocean.com/capsule/8694970/tree)

takefuji (2022) airpiano for playing piano in the air [Source Code]. https://doi.org/10.24433/CO.8862673.v1

This is under review.

airpiano has been downloaded by 16,821 downloads worldwide as of Feb.24, 2023.

When the paper is accepted, the contents of the air piano will be disclosed.
airpiano is a Python program to play airpiano composed of 123 lines code. 
You can play 10 music notes by th right hand of five fingers.
airpiano is based on the-state-of-the-art hand gesture recognition using mediapipe.
airpiano uses musicalbeeps for generating music sounds by five fingers.
The paper on airpiano is under submission.
If the paper is accepted, the source code will be disclosed.


Hand landmarks detected by MediaPipe are composed of 21 points in 2D image coordinates.

<img src='hand_landmarks.png' height=270 width=750 >

https://mediapipe.dev/images/mobile/hand_landmarks.png


[![Watch the video](https://img.youtube.com/vi/7KCmVyRpSCo/maxresdefault.jpg)](https://youtu.be/7KCmVyRpSCo)


# airpiano DEMO

"twinkle twinkle little star"
https://youtu.be/7KCmVyRpSCo

"Mary had a little lamb"
https://youtu.be/3J5xjW66MP8

"Tulip" 
https://youtu.be/H7lwHb69ZgM

"buzz buzz buzz" 
https://youtu.be/oG3_ZsW3XrQ

"The Cuckoo" 
https://youtu.be/evyfpph-WOY

# How to install airpiano

Python3.7 or Python3.8 is recommended for running airpiano. 
In order to run airpiano, the following libraries must be installed.

$ pip install musicalbeeps

$ pip install mediapipe

$ pip install airpiano

$ pip install airpiano --force-reinstall --no-cache-dir --no-binary :all:

# How to play airpiano

Moving thumb finger plays C5 note.

Moving index finger plays D5 note.

Middle finger plays E5 note.

Ring finger plays F5 note.

Little finger plays G5 note.

Moving thumb finger deeply plays A5 note.

Moving thumb finger deeply and index finger plays B5 note.

Moving thumb finger deeply and middle finger plays C6 note.

Moving thumb finger deeply and ring finger plays D6 note.

Moving thumb finger deeply and little finger plays E6 note.


$ airpiano

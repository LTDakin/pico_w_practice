"""
  Morse Code Translator

  Reads a string from cli and translates it to led light signals on the Pi PicoW
"""

from machine import Pin
from utime import sleep

led = Pin('LED', Pin.OUT)

dot_duration = 0.2
dash_duration = dot_duration * 3
space_duration = dot_duration * 7

morse_dict = {
    'a' : '.-',   'b' : '-...',  'c' : '-.-.',
    'd' : '-..',  'e' : '.',     'f' : '..-.',
    'g' : '--.',  'h' : '....',  'i' : '..',
    'j' : '.---', 'k' : '-.-',   'l' : '.-..',
    'm' : '--',   'n' : '-.',    'o' : '---',
    'p' : '.--.', 'q' : '--.-',  'r' : '.-.',
    's' : '...',  't' : '-',     'u' : '..-',
    'v' : '...-', 'w' : '.--',   'x' : '-..-',
    'y' : '-.--', 'z' : '--..'
}

def blink_delay(delay):
  led.on()
  sleep(delay)
  led.off()
  sleep(delay)

def send_pulse(morse):
  if(morse == '.'):
    blink_delay(dot_duration)
  elif(morse == '-'):
    blink_delay(dash_duration)
  else:
    sleep(space_duration)

def character_to_morse(char):
  morse = morse_dict.get(char.lower())
  if(morse):
    for signal in morse:
      send_pulse(signal)
  else:
    print('Unknown Character: ' + char)

while True:
  text = input("Message: ")
  for character in text:
    character_to_morse(character)

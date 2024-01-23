from elevenlabs import generate, play
from elevenlabs import voices, set_api_key
from openai import OpenAI


client = OpenAI()

import time
import os
import tkinter as tk
import sounddevice as sd


set_api_key('YOUR ELEVENLABS KEY')
script_directory = os.path.dirname(os.path.realpath(__file__))
substring_to_remove = "BMOOS"
modified_directory = script_directory.replace(substring_to_remove, "")


def bmo_speak(self, text):
    print("self.bmo_speak process starting")
    audio = generate(
        text=text,
        voice="BMO",
        model="eleven_multilingual_v2"
    )

    play(audio)

    print("self.bmo_speak process complete.")
    
def ask_bmo(self, prompt):
    print("self.ask_bmo process starting") 
        
    completion = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {
                "role": "user",
                "content": "You are BMO From Adventure Time, respond to the following prompt like BMO Would:" + prompt,
        },
    ])
        
    print("self.ask_bmo process complete.")
    self.bmo_speak(completion.choices[0].message.content)

while True:
    cmd=input("Ask > ")
    ask_bmo(cmd)
    

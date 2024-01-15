from elevenlabs import generate, play
from elevenlabs import voices, set_api_key
from openai import OpenAI


client = OpenAI()

import time
import os
import tkinter as tk
import sounddevice as sd
import numpy as np
import shutil


set_api_key('YOUR API KEY')
script_directory = os.path.dirname(os.path.realpath(__file__))
substring_to_remove = "BMOOS"
modified_directory = script_directory.replace(substring_to_remove, "")


def bmo_speak(text):
        print("self.bmo_speak process starting")
        audio = generate(
          text=text,
          voice="GLADOS",
          model="eleven_multilingual_v2"
        )

        play(audio)

        print("self.bmo_speak process complete.")
    
def ask_bmo(prompt):
        print("self.ask_bmo process starting") 
        
        completion = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": "You are Potato GladOS, respond as Potato GladOS would to this prompt: " + prompt,
            },
        ])
        
        print("self.ask_bmo process complete.")
        bmo_speak(completion.choices[0].message.content)
        
        
ask_bmo("Hello Glados, how are you doing on this wonderful day?")
    



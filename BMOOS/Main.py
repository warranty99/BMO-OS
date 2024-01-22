from elevenlabs import generate, play
from elevenlabs import voices, set_api_key
from openai import OpenAI
client = OpenAI()
import time
import os
set_api_key('YOUR KEY')
script_directory = os.path.dirname(os.path.realpath(__file__))
substring_to_remove = "BMOOS"
modified_directory = script_directory.replace(substring_to_remove, "")

def bmo_speak(text):
        print("self.bmo_speak process starting")
        audio = generate(
          text=text,
          voice="GLADOS-NON-POTAT",
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
                "content": "You are GlaDOS, respond to this as GlaDOS, if possible, make it kind of short:  " + prompt,
            },
        ])
        
        print("self.ask_bmo process complete.")
        bmo_speak(completion.choices[0].message.content)
        
while True:
    asked=input("ask > ")
    ask_bmo(asked)    

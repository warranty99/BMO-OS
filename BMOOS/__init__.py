import subprocess
subprocess.call(["pip", "install", "elevenlabs"])
subprocess.call(["pip", "install", "openai"])
subprocess.call(["pip", "install", "numpy"])
subprocess.call(["pip", "install", "sounddevice"])


import os
from elevenlabs import voices, set_api_key
from elevenlabs import clone, generate, play

set_api_key('YOUR ELEVENLABS KEY')
script_directory = os.path.dirname(os.path.realpath(__file__))





voice = clone(
    name="GLADOS",
    description="GLADOS, this has been generated by GLADOS, check out our github! BMO-OS!", # Optional
    files=[script_directory + "/TALKING/0114.mp3"],
)

audio = generate(text="Hello world!", voice=voice)

play(audio)





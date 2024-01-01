# IMPORTANT
First off, read this entirely, or else the code will not work, this is a gaurantee

Secondly, read the security.md too, its very important.

Thirdly, im developing this robot as this project is alive, so right now it kinda works i guess but its very early beta, please understand that.

## Description
This is a public repository where i dump my BMO Robot Code (Adventure Time) So if any of you guys want you can make your own using my shitty code
All versions before v1.0.0 expect insane requirements that arent physically possible, just use the latest version

## Necessities:
All libraries are installed in `__init__.py`, however, to run the source code (will discuss later) you will need a python version beyond 3.8

## How to use:
First off, you will need to buy credit for the openai-api, and the elevenlabs api, links [here](https://platform.openai.com/account/billing/overview) and [here](https://elevenlabs.io/subscription) respectively.
Next step is downloading the source code for the most recent version, when downloaded extract all and open `__init__.py` located inside the folder using notepad or any other text changing software and do the following:

```py

import subprocess
subprocess.call(["pip", "install", "elevenlabs"])
subprocess.call(["pip", "install", "openai"])
subprocess.call(["pip", "install", "numpy"])
subprocess.call(["pip", "install", "sounddevice"])

import os
from elevenlabs import voices, set_api_key
from elevenlabs import clone, generate, play

set_api_key('YOUR ELEVENLABS KEY') # << Right here, change this to your actual elevenlabs API key
```
Make sure to save as .py as `__init__.py`

Next step, open  `Main.py` in the same place as `__init__.py` with notepad or any other text changing software

```py
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


set_api_key('YOUR ELEVENLABS KEY') # << Right here, change this to your actual, real elevenlabs key.
```

Make sure to save changes.

To set up your OpenAi Key, create a new environment variable on your device called OPENAI_API_KEY, set its value to your key

Dont know how to create an environment variable? then buckle up partner, skip this part if you know how.

## Creating an environment variable

To create an environment variable, simply double click on the "This pc" icon on your desktop or file explorer and click properties.
This will open a settings tab, next, find the "Advanced settings" option, or something similar.
This should open a tab featuring a pc icon, find the "Environment variables" button, click it.
Find the "Add" button and click it.
Name the variable "OPENAI_API_KEY" and set its value to your key.
Save changes and exit, make sure to double check if it saved.

## Final notes:

If something doesnt work, add an issue using the template found in .github/ISSUE-TEMPLATES



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
set_api_key('YOUR ELEVENLABS KEY')

script_directory = os.path.dirname(os.path.realpath(__file__))
substring_to_remove = "BMOOS"
modified_directory = script_directory.replace(substring_to_remove, "")



class DesktopSimulator:
    def __init__(self, root):
        self.root = root
        root.title("BMO-OS")
        
        root.configure(bg="#789F73")  
        
        root.geometry("480x320")  
     
        root.resizable(False, False)
        #TO-DO change the file directories to the thing

        #CHANGE HERE

        icon_image = tk.PhotoImage(file=modified_directory+r"\IMAGES\BMOOS LOGO.png")
        resized_icon = self.resize_image(icon_image, (93, 112))
        root.iconphoto(True, resized_icon)

	@@ -42,11 +42,11 @@ def __init__(self, root):
        icon_label.lower()  


        

        #CHANGE HERE

        recycle_bin_icon = tk.PhotoImage(file=modified_directory+r"\IMAGES\BMOICON.gif")
        resized_recycle_bin_icon = self.resize_image(recycle_bin_icon, (60, 60))
        recycle_bin_button = tk.Button(root, image=resized_recycle_bin_icon, bd=0, highlightthickness=0, bg="#789F73", command=self.on_recycle_bin_click)
        recycle_bin_button.image = resized_recycle_bin_icon
	@@ -67,13 +67,13 @@ def on_recycle_bin_click(self):
        #CHANGE HERE

        if bmo_talking:
            self.show_image(modified_directory+r"\IMAGES\TALKING.png)
            # self.bmo_speak("Hello World!")
            self.ask_bmo("HI BMO!")


        else:
            self.show_image(modified_directory+r"\IMAGES\IDLE.png") 
            # self.bmo_speak("Hello World!")
            self.ask_bmo("HI BMO!")

	@@ -170,30 +170,8 @@ def ask_bmo(self, prompt):
    def resize_image(self, image, size):
        return image.subsample(int(image.width() / size[0]), int(image.height() / size[1]))

    def display_files(self):
        #CHANGE HERE
        files = os.listdir(modified_directory+r"\IMAGES")

        #CHANGE HERE AS WELL
        folder_size = (126, 102)  # Adjust the size as needed
        folder_icon = tk.PhotoImage(file=r"C:\Users\Usuario\Desktop\gang shit\BMO\BMO OS FOLDER.png")
        resized_folder_icon = self.resize_image(folder_icon, folder_size)


        for file in files:
            file_frame = tk.Frame(self.root, bg="#789F73")  # Frame to hold folder icon and text

            # Pack the folder icon at the top of the frame
            file_label = tk.Label(file_frame, image=resized_folder_icon, bg="#789F73")
            file_label.image = resized_folder_icon
            file_label.pack()

            # Pack the file name label below the folder icon
            file_name_label = tk.Label(file_frame, text=file, bg="#789F73", fg="white")
            file_name_label.pack()

            # Pack the frame with each file, adjusting padding as needed
            file_frame.pack(side=tk.LEFT, padx=0, pady=0)

if __name__ == "__main__":
    root = tk.Tk()
    desktop_simulator = DesktopSimulator(root)
    root.mainloop()

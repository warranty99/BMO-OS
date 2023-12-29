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


class DesktopSimulator:
    def __init__(self, root):
        self.root = root
        root.title("BMO-OS")

        
        root.configure(bg="#789F73")  
        
        root.geometry("480x320")  

     
        root.resizable(False, False)

        #TO-DO change the file directories to the thing

        #CHANGE HERE
      
        icon_image = tk.PhotoImage(file=r"C:\Users\Usuario\Desktop\gang shit\BMO\BMOOS LOGO.png")
        resized_icon = self.resize_image(icon_image, (93, 112))  
        root.iconphoto(True, resized_icon)

        
        icon_label = tk.Label(root, image=resized_icon, bg="#789F73", bd=0, highlightthickness=0, width=200, height=200)  # Create the label for the icon
        icon_label.place(x=0, y=0)
        icon_label.lower()  

        
        self.display_files()

        #CHANGE HERE
     
        recycle_bin_icon = tk.PhotoImage(file=r"C:\Users\Usuario\Desktop\gang shit\BMO\bmo.exeIcon.gif")
        resized_recycle_bin_icon = self.resize_image(recycle_bin_icon, (60, 60))
        recycle_bin_button = tk.Button(root, image=resized_recycle_bin_icon, bd=0, highlightthickness=0, bg="#789F73", command=self.on_recycle_bin_click)
        recycle_bin_button.image = resized_recycle_bin_icon
        recycle_bin_button.place(x=25, y=25)

       
        

        
    
        

    def on_recycle_bin_click(self):
        bmo_talking = self.check_if_bmo_talking()



        #CHANGE HERE
       
        if bmo_talking:
            self.show_image(r"C:\Users\Usuario\Desktop\gang shit\BMO\BMO Faces\Talking.png")
            # self.bmo_speak("Hello World!")
            self.ask_bmo("HI BMO!")
            
    
        else:
            self.show_image(r"C:\Users\Usuario\Desktop\gang shit\BMO\BMO Faces\Idle.png") 
            # self.bmo_speak("Hello World!")
            self.ask_bmo("HI BMO!")

    def check_if_bmo_talking(self):
        # Does this shit even work anymore??
        max_duration = 2
        indata = sd.rec(frames=44100, channels=2, dtype='int16')
        sd.wait()

        # Java is still better
        if np.any(np.isnan(indata)) or np.any(np.isinf(indata)):
            print("Invalid values in audio data. Skipping RMS calculation.")
            return False

        # Calculate RMS only if indata is valid ig
        rms = np.sqrt(np.mean(indata**2))

        print(f"RMS: {rms}")

        # This shit doesnt work and its so easy to tell
        filter_factor = 0.2  # Adjust this factor based on your observations
        smoothed_rms = self.apply_noise_filter(rms, filter_factor)

        
        threshold_adjustment = 1.5  # Adjust this factor based on your observations

        if not hasattr(self, 'last_rms'):
            self.last_rms = smoothed_rms
        else:
            adjusted_threshold = self.last_rms * threshold_adjustment
            self.last_rms = smoothed_rms
            return smoothed_rms > adjusted_threshold

        return False

    def apply_noise_filter(self, rms, factor):
       
        if not hasattr(self, 'last_rms'):
            self.last_rms = rms
        else:
            smoothed_rms = (1 - factor) * self.last_rms + factor * rms
            self.last_rms = smoothed_rms
            return smoothed_rms

        return rms

    def show_image(self, image_path):
        try:
           
            image = tk.PhotoImage(file=image_path)
            resized_image = self.resize_image(image, (480 , 320))  # Adjust the size as needed

            
            image_label = tk.Label(self.root, image=resized_image, bg="#789F73", bd=0, highlightthickness=0)
            image_label.image = resized_image
            image_label.place(x=0, y=0)  # Adjust the coordinates as needed

            
            self.root.after(2000, lambda: image_label.destroy())
        except tk.TclError as e:
            print(f"Error loading image: {e}")

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
        self.bmo_speak("")
        #TO DO: Speak Resppnse
        
        #DAMN YOU GITHUB!! RESPOND IN THE DAMN OPENAI PYTHON ALREADY!
    


    def resize_image(self, image, size):
        return image.subsample(int(image.width() / size[0]), int(image.height() / size[1]))

    def display_files(self):
        #CHANGE HERE
        files = os.listdir(r"C:\Users\Usuario\Desktop\gang shit\BMO\BMO OS Desktop")

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

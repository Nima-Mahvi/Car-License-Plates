## We need (complete_digits_data.csv) file.it is our digits training file.
## Please wait until this file is completely downloaded and then run the program again.
## If this action is not done, you will be able to download it through the following link.
## Please put it next to the main program file after downloading
## (complete_digits_data.csv) is about 207 MB. It contains 38206 rows and 2401 columns.
## Please check that the file has been downloaded correctly.then run the program.
## https://www.dropbox.com/scl/fi/4wxtzmgcm7yi66zge554u/complete_digits_data.csv?rlkey=jmje04sp07kyvc2h41t9bk1d5&st=j7i8id5r&dl=1

import tkinter as tk
from tkinter import *
from tkinter import filedialog , messagebox
from PIL import ImageGrab , Image , ImageDraw , ImageTk
########################################################
from controller import conotrol_proj
########################################################
import requests
import os
import pandas as pd

def download_file(url, destination):
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(destination, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f'File downloaded: {destination}')
        else:
            print(f'Failed to download file. Status code: {response.status_code}')
    
    try:
        There = pd.read_csv("complete_digits_data.csv")
    except:
        if __name__ == "__main__":
            print("File (complete_digits_data.csv) could not be found. \n We need this file. Please wait until this file is completely downloaded and then run the program again.")
            url = 'https://www.dropbox.com/scl/fi/4wxtzmgcm7yi66zge554u/complete_digits_data.csv?rlkey=jmje04sp07kyvc2h41t9bk1d5&st=j7i8id5r&dl=1'
            print("If this action is not done, you will be able to download it through the following link. Please put it next to the main program file after downloading: \n" , url)
            print("******************* \n It is a csv file about 207 MB. It contains 38206 rows and 2401 columns. Please check that the file has been downloaded correctly.")
            print("******************* \n Downloading... \n Please wait")
            
            file_name = url.split('/')[-1].split('?')[0]
            root_path = os.path.dirname(os.path.abspath(__file__))
            destination = os.path.join(root_path, file_name)
            
            download_file(url, destination)
            
########################################################

def select_file():
    global file_path
    file_path = filedialog.askopenfilename(title = "Select your car license plate image",
                                           filetypes = [("All Files" , "*.*")])
    if file_path:
        lbl_msg2.configure(text=f"Selected File: {file_path}", fg='green')
        lbl_msg3.configure(text="(You can follow steps of the running program from the Console after click OK.) \n Click OK and wait for one-two minute..." )
        btn_OK.configure(state="active")
    
def OK():
    global file_path
    # print(file_path)
    if file_path:
        mycontroller=conotrol_proj()
        mystate , myexact = mycontroller.control(file_path)
        lbl_msg3.configure(text="result: " )
        # print(mystate)
        # print(myexact)
        try:
            lbl_mystate.configure(text=f"Province : {mystate}")
        except:
            lbl_mystate.configure(text= "Province : - ")
        try:
            lbl_myexact.configure(text=f"exact location :  {myexact}")
        except:
            lbl_myexact.configure(text="exact location : - ")
    else:
        lbl_msg3.configure(text="Image not found!" )
        
win=tk.Tk()
win.title(" Car License Plate ")
win.geometry('1000x300')

lbl_msg1=tk.Label(win,text="Please select the image file. \n\n Please make sure that: \n 1) the image is clear. \n 2) only the license plate is inside the photo frame." )
lbl_msg1.pack()

btn_select=tk.Button(win,text='Select File' ,command=select_file )
btn_select.pack()

lbl_msg2=tk.Label(win,text="No file selected!" , fg='red')
lbl_msg2.pack()

btn_OK=tk.Button(win,text='OK' ,command=OK ,state= "disabled")
btn_OK.pack()

lbl_msg3=tk.Label(win,text="")
lbl_msg3.pack()

lbl_mystate=tk.Label(win,text="")
lbl_mystate.pack()

lbl_myexact=tk.Label(win,text="")
lbl_myexact.pack()

win.mainloop()















































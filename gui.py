# Importing necessary packages
import shutil
import tkinter
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter import font as tkFont
import os
import glob
from PIL import ImageTk, Image


def CreateWidgets():
    image1 = Image.open("logo.png")
    new_image1 = image1.resize((80, 80))

    test = ImageTk.PhotoImage(new_image1)

    label1 = tkinter.Label(image=test)
    label1.image = test

    # Position image
    label1.place(x=300, y=10)

    link_Label = Label(root, text="  A Computer Vision Approach in Identifying Ticks  " , bg="skyblue1", font="Stencil" , borderwidth=2, relief="solid")
    link_Label.grid(row=0, column=0,pady=100, padx=100)

    root.sourceText = Entry(root, width=53,textvariable=sourceLocation, borderwidth=2, relief="solid")
    root.sourceText.grid(row=2, column=0,pady=5, padx=15, columnspan=1,sticky=W)

    RT_Button = Button(root, text="Real Time", font=helv15, bg="skyblue1", command=RealTime, width=15, height=1)
    RT_Button.grid(row=3, column=0, pady=10, padx=1, sticky=EW)

    source_browseButton = Button(root, text="Select Image", font=helv10, bg="skyblue1", borderwidth=4,relief=RAISED,command=SourceBrowse, width=15)
    source_browseButton.grid(row=2, column=0,pady=5, padx=0, sticky=E)

    copyButton = Button(root, text="Detect", font=helv15, bg="skyblue1",command=CopyFile, width=15, height=1)
    copyButton.grid(row=4, column=0, pady=10, padx=1, sticky=EW)

    show_Button = Button(root, text="Show result", font=helv15, bg="skyblue1", command=Showimg, width=15, height=1)
    show_Button.grid(row=5, column=0, pady=10, padx=1, sticky=EW)




def Showimg():
    # os.system("python segment/train.py --img 640 --batch 2 --epochs 99 --data data/data.yaml --weights yolov5s-seg.pt --project yolo-wandb-demo")
    os.startfile(r"inference\output")
def RealTime():

    tkinter.messagebox.showinfo(title="Opening", message="opening program")
    os.system(
        "yolo task=segment mode=predict model=F:/pythonProject/ultralytics/ultralytics/runs/segment/train7/weights/best23.pt conf=0.50 source=0 show=True")

def SourceBrowse():
    root.sourceText.delete(0, END)
    root.files_list = list(filedialog.askopenfilenames(initialdir="inference/test"))  # default directory
    root.sourceText.insert('1', root.files_list)  # to display root

def CopyFile():
    dir = 'inference/output'
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

    files_list = root.files_list
    destination_location = 'inference/images'

    # Looping through the files present in the list
    for f in files_list:
        # Copying the file to the destination using
        # the copy() of shutil module copy take the
        # source file and the destination folder as
        # the arguments

        shutil.copy(f, destination_location)

    #messagebox.showinfo("Wait for a while")
    tkinter.messagebox.showinfo(title="Detecting", message="program is trying to detect ticks")
    os.system("yolo task=segment mode=predict model=F:/pythonProject/ultralytics/ultralytics/runs/segment/train27/weights/best.pt source=F:/pythonProject/inference/images conf=0.50 project=F:/pythonProject/inference/output save=True")
    #os.system("python segment/predict2.py --weights runs/train-seg/exp/weights/best.pt --source inference\images --project inference/output ")

    files = glob.glob('inference\images\*')
    tkinter.messagebox.showinfo(title="Detection Finished", message="Show Results")
    os.startfile(r"inference\output")


    for f in files:
        os.remove(f)



# Creating object of tk class
root = tk.Tk()
helv15 = tkFont.Font(family='Times New Roman', size=13, weight='bold')
helv10 = tkFont.Font(family='Times New Roman', size=10, weight='bold')
# Setting the title and background color
# disabling the resizing property
root.geometry("635x450")
root.title(77 * " " + "Detectick")
root.config(background="#e8eded")


# Creating tkinter variable
sourceLocation = StringVar()
destinationLocation = StringVar()

# Calling the CreateWidgets() function
CreateWidgets()

# Defining infinite loop
root.mainloop()

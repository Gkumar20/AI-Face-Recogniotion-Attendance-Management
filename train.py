import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np


def Train(root):
    # configure window
    root.title("Multiple Face Recognition System Using AI")
    root.configure(background="gray")
    root.geometry("1520x780+0+0")

    # Header
    header_frame = ttk.Frame(root, style="Header.TFrame")
    header_frame.place(x=10, y=10, width=1500, height=100)

    style = ttk.Style()
    style.configure("Header.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Title in the header
    title_label = Label(header_frame, text="Train Model Using Multiple Face Data", font=("Helvetica", 40, "bold"), bg="white", fg='red')
    title_label.pack(pady=20)

    # Background box with rounded edges (resembling a shadow)
    background_box = ttk.Frame(root, style="Background.TFrame")
    background_box.place(x=10, y=110, width=1500, height=660)
    style.configure("Background.TFrame", background="white", borderwidth=5, relief="groove", borderradius=10)

    # Background image inside the box
    bg_image = Image.open("public/background1.png")
    bg_image = bg_image.resize((1500, 660), Image.LANCZOS)
    bg_photo = ImageTk.PhotoImage(bg_image)

    bg_label = Label(background_box, image=bg_photo)
    bg_label.image = bg_photo  
    bg_label.pack()

    
    # Button
    Train_btn_image = Image.open("public/train_model.png")
    Train_btn_image = Train_btn_image.resize((300, 300), Image.LANCZOS)
    Train_btn_photo = ImageTk.PhotoImage(Train_btn_image)

    btn1 = Button(background_box, image=Train_btn_photo, borderwidth=5, command=train_classifier)
    btn1.image = Train_btn_photo 
    btn1.place(x=600, y=150)
 
# ============Training Classifier =================
def train_classifier():
    data_dir = ("data")
    path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

    faces = []
    ids = []

    for image in path:
        img = Image.open(image).convert('L') 
        imageNp = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split('.')[1])

        faces.append(imageNp)
        ids.append(id)
        cv2.imshow("training", imageNp)
        cv2.waitKey(1)==13
    
    ids = np.array(ids)

    # Train the recognizer and save it
    clf = cv2.face.LBPHFaceRecognizer_create()

    clf.train(faces, ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()
    messagebox.showinfo("Result", "Training datasets Completed")

if __name__ == "__main__":
    root = Tk()
    Train(root)
    root.mainloop()
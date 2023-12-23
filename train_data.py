import os
import pyttsx3
import cv2 as cv
import numpy as np
from tkinter import *
from PIL import Image
from tkinter import messagebox

class Train_data:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x100+500+200")
        self.root.title("Face Recognition System")
        self.root.configure(bg="lightpink")

        main_frame = Frame(self.root, borderwidth=4, relief="ridge", bg="lightgray")
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        def speak():
            # Initialize the text-to-speech engine
            engine = pyttsx3.init()

            engine.say("Your data is trained successfully")
            engine.runAndWait()
            engine.stop()

            messagebox.showinfo("Info", "Your data is trained successfully")

            # Close the current window and go back to the previous window
            self.root.destroy()

        def training_data():
            faces_dir = ('Faces')
            
            path = [os.path.join(faces_dir, file) for file in os.listdir(faces_dir)]

            faces = []
            user_ids = []

            for image in path:
                img = Image.open(image).convert('L')
                
                imageNp = np.array(img, 'uint8')

                id = int(os.path.split(image)[1].split('.')[1])

                # C:\Users\attaa\Desktop\Face Recognition System\Project\Faces\user.1.1.jpg
                # 0                                                            1

                faces.append(imageNp)
                user_ids.append(id)
                cv.imshow("Training", imageNp)
                cv.waitKey(0)

            user_ids = np.array(user_ids)

            algo = cv.face.LBPHFaceRecognizer_create()

            algo.train(faces, user_ids)
            
            algo.write("classifier.xml")
            
            cv.destroyAllWindows()

        def combined_task():
            training_data()
            speak()

        button = Button(main_frame, text="Train Data!!!", font=("times new roman", 12, "bold"), cursor="hand2", command=combined_task)

        button.place(x=20, y=17, width=120, height=40)

if __name__ == "__main__":
    root = Tk()
    obj = Train_data(root)
    root.mainloop()

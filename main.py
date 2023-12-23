from tkinter import *
from student import Student
from attandance import Attandance
from train_data import Train_data
from face_detector import Face_detector

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("620x600+300+25")
        self.root.title("Face Recognition System")

        # Set the background color of the main window
        self.root.configure(bg="lightblue")

        # Create and place the main frame
        main_frame = Frame(self.root, borderwidth=3, relief="ridge", bg="lightgray")
        
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Create and place the label
        label = Label(main_frame, text="Face Recognition System", font=("times new roman", 32, "bold"),bg="lightgray", fg="red")
        
        label.place(x=30, y=0, width=550, height=50)

        # Creating Button
        b1 = Button(main_frame, text="Student Details", font=("times new roman", 20, "bold"), cursor="hand2",bg=None , fg='gray', command = self.student_detail)

        b1.place(x=30, y=100, width=200, height=80)


        b2 = Button(main_frame, text="Face Detector", font=("times new roman", 20, "bold"), cursor="hand2",bg=None , fg='gray',command=self.face_detector)

        b2.place(x=350, y=100, width=200, height=80)


        b3 = Button(main_frame, text="Train Data", font=("times new roman", 20, "bold"), cursor="hand2",bg=None , fg='gray', command=self.train_data)

        b3.place(x=30, y=300, width=200, height=80)

        
        b4 = Button(main_frame, text="Attandance", font=("times new roman", 20, "bold"), cursor="hand2",bg=None , fg='gray', command=self.attandance)

        b4.place(x=350, y=300, width=200, height=80)


        b5 = Button(main_frame, text="Exit", font=("times new roman", 20, "bold"), cursor="hand2",bg=None , fg='gray', command=lambda:self.root.destroy())

        b5.place(x=195, y=460, width=200, height=80)



# ------------- Functions Buttons ----------
    

    def student_detail(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def face_detector(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_detector(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train_data(self.new_window)


    def attandance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attandance(self.new_window)




if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()
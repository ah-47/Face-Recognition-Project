import os
import json
import pyttsx3
import pymongo
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("580x580+300+25")
        self.root.title("Face Recognition System")

        # Set the background color of the main window
        self.root.configure(bg="lightpink")

        # Create and place the main frame
        main_frame = Frame(self.root, borderwidth=4, relief="ridge", bg="lightgray")
        
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Create and place the label
        label = Label(main_frame, text="Enter Your Details", font=("times new roman", 22, "bold"),bg="lightgray", fg="green")
        
        label.place(x=120, y=0, width=300, height=50)


        # Detail Labels
        full_name_label = Label(main_frame, text="Full Name:", font=("times new roman", 22, "bold"), bg="lightgray")

        full_name_label.place(x=100, y=50)

        full_name_entry = Entry(main_frame, font=("times new roman", 12))
        
        full_name_entry.place(x=250, y=55, height=30, width=200)


        with open("all.json", "r") as file:
            data = json.load(file)
            department = data["department"]

        department_label = Label(main_frame, text="Department:", font=("times new roman", 22, "bold"), bg="lightgray")

        department_label.place(x=100, y=115)

        department_combobox = ttk.Combobox(main_frame, values=department, state="readonly", font=("times new roman", 12))

        department_combobox.set(department[0])

        department_combobox.place(x=280, y = 120, height=30, width=200)


        id_label = Label(main_frame, text="ID:", font=("times new roman", 22, "bold"), bg="lightgray")

        id_label.place(x=100, y=180)

        id_label_entry = Entry(main_frame, font=("times new roman", 12))
        
        id_label_entry.place(x=250, y=185, height=30, width=200)


        teacher_label = Label(main_frame, text="Teacher:", font=("times new roman", 22, "bold"), bg="lightgray")

        teacher_label.place(x=100, y=260)

        teacher_label_entry = Entry(main_frame, font=("times new roman", 12))
        
        teacher_label_entry.place(x=250, y=265, height=30, width=200)


        email_label = Label(main_frame, text="Email:", font=("times new roman", 22, "bold"), bg="lightgray")

        email_label.place(x=100, y=340)

        email_label_entry = Entry(main_frame, font=("times new roman", 12))
        
        email_label_entry.place(x=250, y=345, height=30, width=200)


        phone_label = Label(main_frame, text="Phone No:", font=("times new roman", 22, "bold"), bg="lightgray")

        phone_label.place(x=100, y=420)

        phone_label_entry = Entry(main_frame, font=("times new roman", 12))
        
        phone_label_entry.place(x=250, y=425, height=30, width=200)

        def speak():
            # Initialize the text-to-speech engine
            engine = pyttsx3.init()

            engine.say("Your data is added successfully")
            engine.runAndWait()
            engine.stop()

            messagebox.showinfo("Information", "Your data is added")

            # Close the current window and go back to the previous window
            self.root.destroy()
        
        def data_adding_in_db():
            # Getting data
            fullName = full_name_entry.get()
            id = id_label_entry.get()
            teacherName = teacher_label_entry.get()
            email = email_label_entry.get()
            phone = phone_label_entry.get()
            department = department_combobox.get()

            client = pymongo.MongoClient("mongodb://localhost:27017")

            database = client['Project1']

            collection = database['User']

            d1 = {"_id": id, "Name": fullName, "Department":department , "Teacher": teacherName, "Email": email, "Phone": phone}

            collection.insert_one(d1)
        
        def combined_task():
            data_adding_in_db()
            speak()

        # Save Button
        save_button = Button(main_frame, text="Enter data", font=("times new roman", 22), cursor="hand2", command=combined_task)

        save_button.place(x=200, y=490, height=50, width=170)
    

if __name__ == "__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()
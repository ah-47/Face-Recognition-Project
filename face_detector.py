import pymongo
import cv2 as cv
from tkinter import *
from tkinter import messagebox

class Face_detector:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x100+500+200")
        self.root.title("Face Recognition System")
        self.root.configure(bg="lightpink")

        main_frame = Frame(self.root, borderwidth=4, relief="ridge", bg="lightgray")
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        client = pymongo.MongoClient("mongodb://localhost:27017")
        database = client['Project1']
        collection = database['User']

        cursor = collection.find({})

        id_count = 0
        
        for document in cursor:
            id_count += 1

        face_classifier = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            
            faces = face_classifier.detectMultiScale(gray, 1.3, 4)
            
            for (x, y, w, h) in faces:
                face_cropped = img[y:y+h, x:x+w]
                return face_cropped
            
        def capture_images():
            cap = cv.VideoCapture(0)
            img_id = 0

            while True:
                ret, my_frame = cap.read()

                cropped_face = face_cropped(my_frame)
                
                if cropped_face is not None:
                    img_id += 1
            
                face = cv.resize(face_cropped(my_frame), (450, 450))
                
                face = cv.cvtColor(face, cv.COLOR_BGR2GRAY)
                
                file_name_path = f"Faces/user.{id_count}.{img_id}.jpg"
                 
                cv.imwrite(file_name_path, face)
                
                cv.putText(face, str(img_id), (50, 50), cv.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                
                cv.imshow("Cropped Face", face)

                if cv.waitKey(1) == 13 or int(img_id) == 100:
                    break
            
            cap.release()
            cv.destroyAllWindows()
            messagebox.showinfo("Result", "Images Taken")

        b5 = Button(main_frame, text="Photos!!!", font=("times new roman", 12, "bold"), cursor="hand2", command=capture_images)
        b5.place(x=20, y=17, width=120, height=40)



if __name__ == "__main__":
    root = Tk()
    obj = Face_detector(root)
    root.mainloop()

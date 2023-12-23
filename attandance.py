import pymongo 
import cv2 as cv
from tkinter import *

class Attandance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("200x100+500+200")
        self.root.title("Face Recognition System")

        # Set the background color of the main window
        self.root.configure(bg="lightblue")

        # Create and place the main frame
        main_frame = Frame(self.root, borderwidth=3, relief="ridge", bg="lightgray")
        
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        def face_recog():
            def attandance(img, classifier, scaleFactor, minNeighbors, color, text, clf):
                gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
                
                features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

                coord = []

                for (x,y,w,h) in features:
                    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 3)
                    
                    id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                    
                    confidence = int((100*(1-predict/300)))


                    # Database
                    client = pymongo.MongoClient("mongodb://localhost:27017")

                    db = client["Project1"]
                    
                    students_collection = db["User"]

                    id = str(id)

                    query = {"_id": id}

                    result = students_collection.find_one(query)

                    # Initialize with default values
                    name = "Unknown"
                    department = "Unknown"

                    if result:
                        name = result.get("Name", "unknown")
                        department = result.get("Department", "unknown")
                        
                    if confidence>75:
                        cv.putText(img, f"Name: {name}", (x,y-55), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,255,255), 3)
                        
                        cv.putText(img, f"Department: {department}", (x,y-30), cv.FONT_HERSHEY_COMPLEX, 0.8, (0,255,255), 3)
                    
                    else:
                        cv.rectangle(img,(x,y), (x+w, y+h), (0,0,255), 3)
                        
                        cv.putText(img, "Unknown Face", (x,y-5), cv.FONT_HERSHEY_COMPLEX, 0.8, (255,255,255), 3)
                    
                    coord = [x,y,w,y]
                
                return coord
            
            def recognize(img,clf,faceCascade):
                coord = attandance(img, faceCascade, 1.1, 10, (255,25,255), "Face", clf)

                return img

            faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

            clf = cv.face.LBPHFaceRecognizer_create()

            clf.read("classifier.xml")

            video_cap = cv.VideoCapture(0)

            while True:
                ret, img = video_cap.read()
                
                img = recognize(img, clf, faceCascade)
                
                cv.imshow("Welcome to Face Recognizer", img)

                if cv.waitKey(1) & 0xFF == ord('q'):
                    break
            
            video_cap.release()
            cv.destroyAllWindows()


        button = Button(main_frame, text="Attandance", font=("times new roman", 20, "bold"), cursor="hand2",bg=None , fg='gray', command=face_recog)

        button.place(x=10, y=17, width=150, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Attandance(root)
    root.mainloop()
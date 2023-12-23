import cv2 as cv

# Open the default camera

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print('Error: Camera is not opened')
    exit()

while True:
    # Capture Frame by Frame
    ret, frame = cap.read()

    # if the frame is read correctly, ret will return true
    if not ret:
        print('Error: Couldnot read frame')
        exit()

    #! Add text to the frame
    # text = "Hello, OpenCV!"
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # font_scale = 1
    # font_thickness = 2
    # text_color = (255, 255, 255)  # White color
    # text_position = (50, 50)

    cv.putText(frame, 'Camera Opened', (50,50), cv.FONT_HERSHEY_COMPLEX, 1, (143,255,0), 2)

    cv.imshow('Camera Feed', frame)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

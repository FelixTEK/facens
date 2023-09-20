import cv2 #import openCV Library

def detectface(): #face detection
    inputimg = input("Insert path and name of file <e.g. input/example.jpg>")
    img = cv2.imread(inputimg)
    print("Blurring image...")
    face_model = cv2.CascadeClassifier('detection-face.xml') #detection model
    gray_scale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #grayscale to make detection easier
    faces = face_model.detectMultiScale(gray_scale) #detect from grayscale version
    cv2.namedWindow("Resized_Window", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Resized_Window", 300, 400)
    
    for (x,y,w,h) in faces: #blur faces
        ROI = img[y:y+h, x:x+w]
        for i in range(0,75):
            blur = cv2.GaussianBlur(ROI, (99,99), 0)
            img[y:y+h, x:x+w] = blur
            i = i+1
    
    cv2.imshow("Resized_Window", img)
    print("Done!")
    cv2.waitKey(0) #wait for key
    cv2.destroyAllWindows() #close windows

if __name__ == "__main__": #main function
    detectface()
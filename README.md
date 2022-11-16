CV experiment 2: 

Face detection and tracking with opencv

# Requirements
Anaconda 3
opencv
laptop with camera

# Face Recognition
run **face_rec.py** for face detection/recognition

## Step 1: Call computer camera

## Step 2: Create CascadeClassifier to detect face
`face = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')
`
## Step 3: Draw recognition frame
` cv.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(255, 255, 0))`

## Step 4: Save video

## Step 5: Release memory & exit program

# Object Tracking and Draw the Motion Track
import cv2
import numpy as np
import argparse
from collections import deque

ap = argparse.ArgumentParser()
args = vars(ap.parse_args())
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('video_1.mp4')
pts = deque(maxlen=124)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    # print i.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    l = len(faces)
    print(l)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # cv2.putText(frame, 'face', (w / 2 + x, y - h / 5), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 255, 255), 2, 1)
        center = (x + w / 2, y + h / 2)
        print(center)
        pts.appendleft(center)
        for i in range(1, len(pts)):
            if pts[i - 1] is None or pts[i] is None:
                continue
            thickness = int(np.sqrt(64 / float(i + 1)) * 2.5)
            cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
        cv2.imshow("camera", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 摄像头释放
cap.release()
# 销毁所有窗口
cv2.destroyAllWindows()

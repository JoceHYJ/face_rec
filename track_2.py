import sys
import cv2


def tracking():
    count = 0
    (major_ver, minor_ver, subminor_ver) = cv2.__version__.split('.')
    print(major_ver, minor_ver, subminor_ver)
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    # 创建跟踪器
    tracker_type = 'MIL'
    tracker = cv2.TrackerMIL_create()
    # 读入视频
    video = cv2.VideoCapture(0)
    # video = cv2.VideoCapture("video_1.mp4")
    # 读入第一帧
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    # 定义一个bounding box
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )
    if list(faces):
        for (x, y, w, h) in faces:
            bbox = (x, y, w, h)
            print(bbox)
    ok = tracker.init(frame, bbox)
    while True:
        ok, frame = video.read()
        if not ok:
            break
        # Start timer
        timer = cv2.getTickCount()
        # Update tracker
        ok, bbox = tracker.update(frame)
        # Calculate FPS
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)
        # Draw bonding box
        if ok:
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
        else:
            cv2.putText(frame, "Tracking failed detected", (100, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 0, 255), 2)
        # 展示tracker类型
        cv2.putText(frame, tracker_type + "Tracker", (100, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        # 展示FPS
        cv2.putText(frame, "FPS:" + str(fps), (100, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50, 170, 50), 2)
        # Result
        cv2.imshow("Tracking", frame)

        # Exit
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break


if __name__ == '__main__':
    tracking()


import cv2 as cv

if __name__ == '__main__':
    # 打开摄像头
    cap = cv.VideoCapture(0)
    # 读视频文件
    # cap = cv.VideoCapture('video_1.mp4')

    # 人脸识别，级联分类器
    face = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')

    while True:
        flag, frame = cap.read()  # flag 是否读取了图片 frame
        if not flag:
            break
        # gray = cv.cvtColor(frame, cv.cvtColor(frame, code=cv.COLOR_BGR2GRAY))
        faces = face.detectMultiScale(frame)
        for x, y, w, h in faces:
            cv.rectangle(frame,
                         pt1=(x, y),
                         pt2=(x + w, y + h),
                         color=(255, 255, 0))

        cv.imshow('camera', frame)
        key = cv.waitKey(1000 // 24)
        if key == ord('q'):  # quit 'q'
            break

    cv.destroyAllWindows()
    cap.release()  # 释放内存

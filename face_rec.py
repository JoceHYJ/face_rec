import cv2 as cv

if __name__ == '__main__':
    # 打开摄像头
    # cap = cv.VideoCapture(0)
    # 读视频文件
    cap = cv.VideoCapture('video_1.mp4')

    # 人脸识别，级联分类器
    face = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')

    # 保存视频
    writer = cv.VideoWriter(filename='./out.mp4',
                            fourcc=cv.VideoWriter.fourcc(*'MP4V'),  # 视频编码 fourcc
                            frameSize=[int(cap.get(3)), int(cap.get(4))],  # 获取摄像头分辨率
                            fps=24)

    while True:
        flag, frame = cap.read()  # flag 是否读取了图片 frame
        if not flag:
            break
        # gray = cv.cvtColor(frame, cv.cvtColor(frame, code=cv.COLOR_BGR2GRAY))

        # 保存
        writer.write(frame)

        faces = face.detectMultiScale(frame)
        for x, y, w, h in faces:
            cv.rectangle(frame,
                         pt1=(x, y),
                         pt2=(x + w, y + h),
                         color=(255, 255, 0),
                         thickness=2)

        cv.imshow('camera', frame)
        key = cv.waitKey(1000 // 24)
        if key == ord('q'):  # quit 'q'
            break

    cap.release()  # 释放内存
    writer.release()  # 释放内存
    cv.destroyAllWindows()

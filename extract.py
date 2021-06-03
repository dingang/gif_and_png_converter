import os
import cv2

img_name = "test"

dir = "./{}".format(img_name)
if not os.path.isdir(dir):
    os.mkdir(dir)

capture = cv2.VideoCapture("./{}.gif".format(img_name))
cnt = 0

while cv2.waitKey(33) < 0:
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
        break

    ret, frame = capture.read()

    if cnt < 10:
        str = "./{}/{}_00{}.png".format(img_name, img_name, cnt)
    elif cnt < 100:
        str = "./{}/{}_0{}.png".format(img_name, img_name, cnt)
    else :
        str = "./{}/{}_{}.png".format(img_name, img_name, cnt)
    cv2.imwrite(str,frame)
    cnt += 1

capture.release()

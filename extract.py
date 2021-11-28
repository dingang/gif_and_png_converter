import os
import argparse
import cv2

class Extractor():
    def __init__(self):
        self.cnt = 0
        self.iter = 0
        self.__parse_args()

    def __parse_args(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-N",
                                        dest="img_name", type=str, default='test',
                                        help="Source file name without extension")
        arg_parser.add_argument("--name",
                                        dest="img_name", type=str, default='test',
                                        help="Source file name without extension")
        arg_parser.add_argument("--ext",
                                        dest="ext", type=str, default='gif',
                                        help="Source file extention, default is GIF")
        arg_parser.add_argument("--min",
                                        dest="min", type=int, default=0,
                                        help="First frame")
        arg_parser.add_argument("--max",
                                        dest="max", type=int, default=1000,
                                        help="Last frame")
        arg_parser.add_argument("--reverse",
                                        dest="reverse", action="store_true",
                                        help="Reverse for iteration")
        args = arg_parser.parse_args()
        self.__args: dict = args
        self.__setting()

    def __setting(self):
        self.img_name = self.__args.img_name
        self.reverse = self.__args.reverse

        dir = "./{}".format(self.img_name)
        if not os.path.isdir(dir):
            os.mkdir(dir)

        self.capture = cv2.VideoCapture("./{}.{}".format(self.img_name, self.__args.ext))
        if self.reverse:
            self.img_list = []

    def imageWrite(self, frame):
        if self.cnt < 10:
            str = "./{}/{}_00{}.png".format(self.img_name, self.img_name, self.cnt)
        elif self.cnt < 100:
            str = "./{}/{}_0{}.png".format(self.img_name, self.img_name, self.cnt)
        else :
            str = "./{}/{}_{}.png".format(self.img_name, self.img_name, self.cnt)
        cv2.imwrite(str,frame)

    def run(self):
        while cv2.waitKey(33) < 0:
            if self.capture.get(cv2.CAP_PROP_POS_FRAMES) == self.capture.get(cv2.CAP_PROP_FRAME_COUNT):
                self.capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
                break

            ret, frame = self.capture.read()
            if self.iter < self.__args.min :
                self.iter += 1
                continue

            if self.iter > self.__args.max :
                break

            else:
                self.imageWrite(frame)
                if self.reverse:
                    self.img_list.append(frame)

                self.cnt += 1
                self.iter += 1

        if self.reverse:
                self.img_list.reverse()
                for frame in self.img_list:
                    self.imageWrite(frame)
                    self.cnt+=1

        self.capture.release()

if __name__ == '__main__':
    app = Extractor()
    app.run()

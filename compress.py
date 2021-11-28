import os
import argparse
import imageio
from PIL import Image

class Compressor():
    def __init__(self):
        self.__parse_args()

    def __parse_args(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument("-N",
                                        dest="img_name", type=str, default='test',
                                        help="Source directory name without extension")
        arg_parser.add_argument("--name",
                                        dest="img_name", type=str, default='test',
                                        help="Source directory name without extension")
        arg_parser.add_argument("--fps",
                                        dest="fps", type=int, default=20,
                                        help="Frame rate")
        arg_parser.add_argument("--reverse",
                                        dest="reverse", action="store_true",
                                        help="Reverse for iteration")
        args = arg_parser.parse_args()
        self.__args: dict = args
        self.__setting()

    def __setting(self):
        self.reverse = self.__args.reverse

    def run(self):
        img_name = self.__args.img_name
        path = [ f"./{img_name}/{i}" for i in os.listdir("./" + img_name) ]
        paths = [ Image.open(i) for i in path ]
        if self.reverse:
            path_reverse = paths.copy()
            path_reverse.reverse()
            paths = paths + path_reverse
        imageio.mimsave('./' + img_name + '.gif', paths, fps=self.__args.fps)

if __name__ == '__main__':
    app = Compressor()
    app.run()

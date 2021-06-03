import os
import imageio
from PIL import Image

img_name = "for_test_to"

path = [f"./{img_name}/{i}" for i in os.listdir("./" + img_name)]
paths = [ Image.open(i) for i in path]
imageio.mimsave('./' + img_name + '.gif', paths, fps=20)

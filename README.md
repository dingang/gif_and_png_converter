## USAGE
```
python3 extract.py  -N or --name [FILE NAME]
                      [--ext [EXTENSION]]
                      [--min [FIRST FRAME]]
                      [--max [LAST FRAME]]
                      [--reverse]
```
```
python3 compress.py  -N or --name [FILE NAME]
                      [--fps [FRAME RATE, DEFAULT= 20]]
                      [--reverse]
```

## USAGE-KOR
1. 구글에서 gif 혹은 mp4 파일을 다운받는다.
2. gif 혹은 mp4 파일을 extract.py와 같은 폴더로 이동시킨다.
3. extract.py 파일을 실행한다.
```
python3 extract.py --name file_name --ext mp4 --min 32 --max 142
```

4. [이미지 편집 사이트](https://pixlr.com/kr/e/) 에 들어가서 프레임별로 이미지를 편집한다. (혹은 다른 이미지 편집 프로그램 - 포토샵 등)

5. 편집이 완료되면 compress.py와 같은 폴더에 새 폴더를 만들어 병합하길 원하는 파일들을 새로만든 폴더에 모두 옮긴다.
6. compress.py 파일을 실행한다.
```
python3 compress.py --name dir_name --fps 25 --reverse
```
7. 결과 파일을 확인하고 기호에 맞춰 compress.py fps 값을 조정하며 실행한다.

## USAGE-ENG
1. Download GIF or MP4 file on google or others
2. Move the GIF or MP4 file to the same directory as extract.py
3. execute extract.py
```
python3 extract.py --name file_name --ext mp4 --min 32 --max 142
```
4. Edit the image frame by frame (in photoshop, i used [this website](https://pixlr.com/kr/e/ ))
5. After image editing, you make new directory for your images(will be gif) and move all files you want to merge into the newly created directory
6. execute compress.py
```
python3 compress.py --name dir_name --fps 25 --reverse
```
7. Check the results and adjust the number of fps to your liking

## REQUIREMENT

#### python3.9.1 or later, python3-pip, matplotlib, opencv-python, imageio, Pillow

python install at [python official website](https://www.python.org/) (for Windows)
<br>
pip on Windows
```
open cmd(admin)
$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python get-pip.py
```
pip on Linux Ubuntu 20.04
```
open terminal
$ sudo apt install python3-pip
```
pip on Mac
```
open terminal
$ sudo easy_install pip
```
matplotlib
```
$ python3 -m pip install matplotlib
```
opencv-python
```
$ python3 -m pip install scikit-build
$ python3 -m pip install opencv-python
```
imageio
```
$ python3 -m pip install imageio
```
Pillow
```
$ python3 -m pip install Pillow
```

## REFERENCE :
extract.py :	[python-opencv-4_윤대희님](https://076923.github.io/posts/Python-opencv-4/)<br>
compress.py :	[디테일이 전부다. 분석뉴비님](https://data-newbie.tistory.com/413)

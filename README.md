## USAGE-KOR
1. 구글에서 gif 파일을 다운받는다.
2. gif 파일을 extract.py와 같은 폴더로 이동시킨다.
3. extract.py 파일을 열고 (메모장 등) 
    * 4번째줄 img_name = "test" 의 test를 gif파일의 이름으로 바꾼다. (확장자 생략)
4. extract.py 파일을 실행한다.

5. [이미지 편집 사이트](https://pixlr.com/kr/e/) 에 들어가서 프레임별로 이미지를 편집한다. (혹은 다른 이미지 편집 프로그램 - 포토샵 등)

6. 편집이 완료되면 compress.py와 같은 폴더에 새 폴더를 만들어 병합하길 원하는 파일들을 새로만든 폴더에 모두 옮긴다.
7. compress.py 파일을 열고 (메모장 등)
    * 5번째 줄 img_name = "test"의 test를 새로 만든 폴더 이름으로 변경한다.
8. compress.py 파일을 실행한다.
9. 결과 파일을 확인하고 기호에 맞춰 compress.py 마지막줄 fps=20 의 숫자를 조정하며 실행한다.

## USAGE-ENG
1. Download GIF file on google or others
2. Move the GIF file to the same directory as extract.py
3. open extract.py for edit (ex: vim, notepad)
    - Replace 'test' in line 4 img_name = "test" with the name of the GIF file. (without ".gif")
4. execute extract.py
```
python3 extract.py
```
5. Edit the image frame by frame (in photoshop, i used [this website](https://pixlr.com/kr/e/ ))
6. After image editing, you make new directory for your images(will be gif) and move all files you want to merge into the newly created directory
7. open compress.py for edit
    * Replace 'test' in line 5 img_name = "test" with the name of new directory that created at step 6
8. execute compress.py
```
python3 compress.py
```
9. Check the result, change fps number at last line of compress.py (fps=20)

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

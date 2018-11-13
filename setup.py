from pip._internal import main
from os import system

main(['install','--upgrade', 'pip', 'wheel', 'setuptools'])
main(['install', 'opencv-python<=3.4.0'])

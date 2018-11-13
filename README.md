# Northrop Grumman Image Challenge
## Setup
### Dependencies

 - CUDA 9.1 https://developer.nvidia.com/cuda-91-download-archive
 - cuDNN 7.4 https://developer.nvidia.com/cudnn
 - OpenCV <=3.4.0 (does not need to be downloaded separately, installed through setup.py script)
### Setup process
 - Install CUDA and cuDNN
 - Clone this repository
 - Run `python setup.py`
## Usage
To run our model on images and videos, pass an array of space separated file paths to main.py
`python main.py image1.bmp image2.bmp vid.mp4`

## Sample Output
```
Analysis of video Ambulance_Scene_3.bmp

Num of Emergency Vehicles: 1
[[174, 98]]

Analysis of video new_Test.mp4

[4, 4, 4, 4, 4, 4, 4]
[[219, 184], [385, 202], [353, 488], [216, 494]]
[[219, 184], [385, 202], [353, 488], [216, 494]]
[[219, 184], [385, 202], [353, 488], [216, 494]]
[[219, 184], [385, 202], [353, 488], [216, 494]]
[[219, 184], [385, 202], [353, 488], [216, 494]]
[[219, 184], [385, 202], [353, 488], [216, 494]]
[[219, 184], [385, 202], [353, 488], [216, 494]]
```
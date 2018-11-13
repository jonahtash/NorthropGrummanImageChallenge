import sys
import os
import re
import math
from subprocess import Popen, PIPE

CFG = "cfg/tiny-yolo.cfg"

WEIGHTS = "backup/tiny-yolo_38100.weights"

DNETOPTIONS = "-dont_show -ext_output"


def img_process(img_path):
    cmd = "darknet.exe detector test cfg/obj.data " + CFG + " " + WEIGHTS + " " + DNETOPTIONS + " "+ img_path
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    results, traash = p.communicate()

    print("\nAnalysis of video "+ img_path + "\n")
    #results = open('results_fs3.txt', 'r')
    results = str(results).replace('\n','').replace('\r','')

    counter = 0
    bounding_box = []
    centers = []
    bounding_box_pattern = re.compile(r"\(left_x: .+?\)")
    for bounding_box_match in re.finditer(bounding_box_pattern, results):
        bounding_box = bounding_box_match.group()
        bounding_box = bounding_box[:-1]
        counter += 1
        bounding_box = [int(s) for s in bounding_box.split() if s.isdigit()]
        center_x = math.floor(bounding_box[0] + bounding_box[2]/2)
        center_y = math.floor(bounding_box[1] + bounding_box[3]/2)
        center = list((center_x, center_y))
        centers.append(center)

    print("Num of Emergency Vehicles: " + str(counter))

    print(centers)
    


def vid_process(vid_path):
    print("\nAnalysis of video "+ vid_path + "\n")
    
    cmd = "darknet.exe detector demo cfg/obj.data " + CFG + " " + WEIGHTS + " " + DNETOPTIONS + " "+ vid_path
    p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    results, trash = p.communicate()

    #results = os.popen("darknet.exe detector demo cfg/obj.data " + CFG + " " + WEIGHTS + " " + DNETOPTIONS + " "+ vid_path)

    #results = open("boom.txt", 'r')

    #print(results)
    counter = 0
    results = results.decode('utf-8').replace('\r', '').replace(")\n",")").replace("\nO"," O").replace(":\n\n",": ").split("\n")
    #results = results.read().replace(")\n",")").replace("\nO"," O").replace(":\n\n",": ").split("\n")
    counts = []
    centers = []

    bounding_box_pattern = re.compile(r"\(left_x: .+?\)")

    for line in results:
        centers_in_frame = []
        count = 0
        for bounding_box_match in re.finditer(bounding_box_pattern, line):
            center = []
            bounding_box = bounding_box_match.group()
            bounding_box = bounding_box[:-1]
            bounding_box = [int(s) for s in bounding_box.split(" ") if s.isdigit()]
            center_x = math.floor(bounding_box[0] + bounding_box[2]/2)
            center_y = math.floor(bounding_box[1] + bounding_box[3]/2)
            center.append(center_x)
            center.append(center_y)
            centers_in_frame.append(center)
            count +=1

        counts.append(count)
        centers.append(centers_in_frame)

    print(counts)
    for center in centers:
        print(center)



                      
if __name__ == "__main__":

    for arg in sys.argv:
        if arg.endswith('.bmp'):
            #process img
            img_process(arg)
        elif arg.endswith('.mp4'):
            #process vid
            vid_process(arg)

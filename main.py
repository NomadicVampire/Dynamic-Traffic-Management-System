import cv2
from vehicle_detector import VehicleDetector
import glob

# Load images from a folder
images_folder = glob.glob("img/*.jpeg")

vd = VehicleDetector()
# lane arrays
lane = []
count = 0

def syncLane(lane):
    baseTimer = 20 # baseTimer = int(input("Enter the base timer value"))
    timeLimits = [2, 5] # timeLimits = list(map(int,input("Enter the time limits ").split()))
    # print("no of vehicles : ", *lane)

    t = [(i / sum(lane)) * baseTimer if timeLimits[0] < (i / sum(lane)) * baseTimer < timeLimits[1] else min(timeLimits, key=lambda x: abs(x - (i / sum(lane)) * baseTimer)) for i in lane]
    print("--------------------------")
    print("Lane 1 waiting time :", t[0])
    print("Lane 2 waiting time :", t[1])
    print("Lane 3 waiting time :", t[2])
    print("Lane 4 waiting time :", t[3])
    print("Total average waiting time :", sum(t))

    print("--------------------------")
    w = int(sum(t)) *1000

    return w


# Loop through all the images
for img_path in images_folder:

    # calls function to find waiting time for each lane when we get images of all 4 lanes
    if (count % 4 == 0 and count != 0):
        waitTime = syncLane(lane)
        cv2.waitKey(waitTime)
        lane.clear()
        count = 0


    img = cv2.imread(img_path)
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 2)
        cv2.putText(img, "Vehicles Detected: " + str(vehicle_count), (20, 50), 0, 1, (100, 200, 0), 2)
    print("Total current count", vehicle_count)
    lane.append(vehicle_count)
    cv2.imshow("Cars", img)
    count = count + 1
    
    cv2.waitKey(1000)

# For last set of lane
waitTime = syncLane(lane)


# total no. of vehicles for each lane
# for it in lane:
#     print(it)


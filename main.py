import cv2
from vehicle_detector import VehicleDetector
import glob

# Load images from a folder
images_folder = glob.glob("img/*.jpeg")

vd = VehicleDetector()
# lane arrays
lane = []*4
count = 0

# Loop through all the images
for img_path in images_folder:
    #     print("Img path", img_path)
    img = cv2.imread(img_path)
    vehicle_boxes = vd.detect_vehicles(img)
    vehicle_count = len(vehicle_boxes)

    # ClassIndex, confidece, bbox = model.detect(img, confThreshold=0.5)
    font_scale = 3
    font = cv2.FONT_HERSHEY_PLAIN

    for box in vehicle_boxes:
        x, y, w, h = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (25, 0, 180), 2)
        cv2.putText(img, "Vehicles Detected: " + str(vehicle_count), (20, 50), 0, 1, (100, 200, 0), 2)
    print("Total current count", vehicle_count)
    lane.append(vehicle_count)
    cv2.imshow("Cars", img)
    cv2.waitKey(0)


for it in lane:
    print(it)
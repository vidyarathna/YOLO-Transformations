import numpy as np
import argparse
import cv2
import os
import time

def rotate_image(image, angle):
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated_image = cv2.warpAffine(image, M, (w, h))
    return rotated_image

def scale_image(image, scale_percent):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    scaled_image = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
    return scaled_image

def main():
    # Construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    ap.add_argument("-y", "--yolo", required=True, help="base path to YOLO directory")
    ap.add_argument("-c", "--confidence", type=float, default=0.5, help="minimum probability to filter weak detections")
    ap.add_argument("-t", "--threshold", type=float, default=0.3, help="threshold when applying non-maxima suppression")
    ap.add_argument("-r", "--rotation_angle", type=float, default=0, help="rotation angle in degrees")
    ap.add_argument("-s", "--scale_factor", type=float, default=1.0, help="scaling factor")
    args = vars(ap.parse_args())

    # Load the COCO class labels our YOLO model was trained on
    labelsPath = os.path.sep.join([args["yolo"], "coco.names"])
    LABELS = open(labelsPath).read().strip().split("\n")

    # Derive the paths to the YOLO weights and model configuration
    weightsPath = os.path.sep.join([args["yolo"], "yolov3.weights"])
    configPath = os.path.sep.join([args["yolo"], "yolov3.cfg"])

    # Load our YOLO object detector trained on COCO dataset (80 classes)
    print("[INFO] loading YOLO from disk...")
    net = cv2.dnn.readNetFromDarknet(configPath, weightsPath)

    # Load our input image and grab its spatial dimensions
    image = cv2.imread(args["image"])
    
    # Apply transformations
    if args["rotation_angle"] != 0:
        rotated_image = rotate_image(image, args["rotation_angle"])
        output_rotated = args["image"].replace('.jpg', '_rotated.jpg')
        cv2.imwrite(output_rotated, rotated_image)
        print(f"Rotated image saved as {output_rotated}")

    if args["scale_factor"] != 1.0:
        scaled_image = scale_image(image, args["scale_factor"])
        output_scaled = args["image"].replace('.jpg', '_scaled.jpg')
        cv2.imwrite(output_scaled, scaled_image)
        print(f"Scaled image saved as {output_scaled}")

if __name__ == "__main__":
    main()
  

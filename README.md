YOLO-Transformations
This repository contains scripts for performing image transformations using YOLO object detection models. The transformations include rotation and scaling operations on input images.

Prerequisites
Before running the scripts, make sure you have the following installed:

Python 3.x
OpenCV (cv2)
YOLO v3 or v4 model files (yolov3.weights, yolov3.cfg, and coco.names)
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/YOLO-Transformations.git
cd YOLO-Transformations
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Usage
To perform image transformations (rotation and scaling) using YOLO, run the script yolo_transformations.py with the following command:

bash
Copy code
python yolo_transformations.py --image path/to/your/image.jpg --yolo path/to/yolo-coco --rotation_angle 45 --scale_factor 1.5
Arguments
-i, --image: Path to the input image.
-y, --yolo: Base path to the YOLO directory containing coco.names, yolov3.weights, and yolov3.cfg.
-r, --rotation_angle: Rotation angle in degrees (default is 0).
-s, --scale_factor: Scaling factor (default is 1.0).
Example
bash
Copy code
python yolo_transformations.py --image ./input_images/living_room.jpg --yolo ./yolo-coco --rotation_angle 45 --scale_factor 1.5
This command will rotate the living_room.jpg image by 45 degrees and scale it by 1.5 times, saving the transformed images as living_room_rotated.jpg and living_room_scaled.jpg.

import cv2
import numpy as np
import os
import time

from ultralytics.utils.plotting import Annotator  # ultralytics.yolo.utils.plotting is deprecated
from ultralytics import YOLO
from PIL import Image, ImageFilter


model = YOLO("path/to/model.pt")

# saved output
output_folder_path = './processed'

# Create the output directory if it doesn't exist
os.makedirs(output_folder_path, exist_ok=True)

folder_path = './data'
video_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
print('video files: ', video_files)

for video_file in video_files:
    video_path = os.path.join(folder_path, video_file)
    cap = cv2.VideoCapture(video_path)
    cap.set(3, 640)
    cap.set(4, 480)
    time.sleep(2.0)

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out_path = os.path.join(output_folder_path, video_file)
    out = cv2.VideoWriter(out_path, fourcc, 20.0, (640, 480))

    while True:
        ret, img = cap.read()

        if not ret:
            print("Error: Failed to read frame or end of video reached")
            break

        # Check if the frame is empty
        if img is None or img.size == 0:
            print("Error: Empty frame")
            break

        img = cv2.resize(img, (640, 480))
        
        # BGR to RGB conversion is performed under the hood
        results = model.predict(img)

        for r in results:
            boxes = r.boxes

            for box in boxes:
                left, top, right, bottom = np.array(box.xyxy.cpu(), dtype=np.int).squeeze()
                width = right - left
                height = bottom - top

                cv2.rectangle(img, (left, top), (right, bottom), (0, 0, 255), 5)
                
                # extract plate detection img
                img_roi = img[top:bottom, left:right]

                # Apply a blur filter (GaussianBlur)
                gaussian_blur = cv2.GaussianBlur(img_roi, (55, 55), 0)
                img[top:bottom, left:right] = gaussian_blur
        
        # Write the frame to the output video
        out.write(img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    
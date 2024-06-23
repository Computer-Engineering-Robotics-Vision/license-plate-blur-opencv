# License Plate Blurring with OpenCV

This project blurs license plates in videos using OpenCV in Python with an accuracy of about 83%. The blurring technique used is `Gaussian Blur`.

To run this on Google Colab: 
[<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab" style="width: 120px;"/>](https://colab.research.google.com/drive/1j6ojAbOk777XfOO7Gug184GZieeDMx4Z?usp=sharing)


## Requirements

- Python 3.6 or higher
- A GPU (Nvidia GTX or RTX) to run the Yolov8 object detection model locally

## Clone the repo
```sh
git clone https://github.com/Computer-Engineering-Robotics-Vision/license-plate-blur-opencv
cd license-plate-blur-opencv
```

## Create a virtual environment
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

## Install requirements
```sh
pip install -r requirements.txt
```

## Run the script
```sh
python license_plate.py
```


1. **Load Your Videos:**
Place all your videos into a folder called "data" in the root directory of the repo.

2. **Run the Script:**
Run your script.

3. **Processed Videos:**
All processed videos will be stored in a directory called 'processed'.



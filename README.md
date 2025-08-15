# Face Recognition and Multi-Function Project

This is a Python-based face recognition project that supports image and video recognition, as well as model training. The project includes functionalities such as reading images, grayscale conversion, resizing, drawing rectangles, single/multi-face recognition, video recognition, face recording, and model training.

---

## Project Structure
```
- imgs/ # Original images
- train img/ # Training images
- trainer/ # Model training folder
- 1.read image.py
- 2.grayscale conversion.py
- 3.modify size.py
- 4.draw rectangle.py
- 5.face recongnition.py
- 6.multi reco.py
- 7.video reco.py
- 8.face record.py
- 9.data training.py
- 10.face reco.py
```

---

## Installation

```bash
pip install opencv-contrib-python
pip install numpy
```
---

## Usage

1. Run the main program:  
Run each .py file to try each function.  
2. You can also run individual scripts for testing specific functionalities:
```python
# Read images
python 1.read image.py

# Convert to grayscale
python 2.grayscale conversion.py

# Resize images
python 3.modify size.py

# Draw rectangles on faces
python 4.draw rectangle.py

# Single face recognition
python 5.face recongnition.py

# Multi-face recognition
python 6.multi reco.py

# Video face recognition
python 7.video reco.py

# Record face data
python 8.face record.py

# Train face recognition model
python 9.data training.py

# Real-time face recognition
python 10.face reco.py
```
---

### File Description

- 1.read image.py: Read image files.

- 2.grayscale conversion.py: Convert color images to grayscale.

- 3.modify size.py: Resize images to a consistent input size.

- 4.draw rectangle.py: Draw rectangles around detected faces.

- 5.face recongnition.py: Implement single-face recognition.

- 6.multi reco.py: Implement multi-face recognition.

- 7.video reco.py: Perform real-time face recognition on video streams.

- 8.face record.py: Record face data into files or a database.

- 9.data training.py: Train a face recognition model.

- 10.face reco.py: Real-time face recognition.

### Dataset

- imgs/: Original images for testing or training.

- train_img/: Training images used for model training.

### Training and Testing
1. Train the Model
```
python 9.data training.py
```
2. Test Recognition
```
python reco.py
```
---
## Notes

- Make sure all required Python packages are installed.

- Adjust file paths in scripts according to your environment.

- For GPU acceleration, ensure you have the correct PyTorch version installed.

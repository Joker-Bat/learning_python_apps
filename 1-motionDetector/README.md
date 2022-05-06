## Controlling webcam and detecting objects

### To Run
- clone this repo and run 
  ``` py
    python3 plotting.py
  ```

### Features

- It will access the webcam and detects the moving objects

- It will store the initial frame and compare the upcoming frames with it to detect moving objects

- Whenever object moving captured it will save the time stamp of when object entered, or leaved.

- And These time stamps will be saved in a file using pandas and it will show a quad plot of data using bokeh.

### Packages used

- cv2 --> To capture and manipulate image or video

- pandas --> To save the timestamps in a file

- datetime --> To get current Date Time

- bokeh --> To make a plot using timestamp data

### Learned

- How to Access webcam in python using opencv

- How to process the image or video using opencv

- How to detect moving object in webcam

- How to make simple plots using bokeh

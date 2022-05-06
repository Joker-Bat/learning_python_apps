import cv2
import pandas
from datetime import datetime

# Store the first frame
first_frame = None
status_list = [None, None]
times = []

df = pandas.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(0)

while True:
    check, frame = video.read()

    status = 0

    grey_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grey_img = cv2.GaussianBlur(grey_img, (21, 21), 0)

    if first_frame is None:
        first_frame = grey_img
        continue

    delta_frame = cv2.absdiff(first_frame, grey_img)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 10000:
            continue
        status = 1
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)

    status_list.append(status)

    # To avoid memory issues we only keep last two entries
    status_list = status_list[-2:]

    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())
    elif status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Capturing", grey_img)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Original Frame", frame)

    key = cv2.waitKey(1)

    # print(grey_img)
    # print(delta_frame)

    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

# print(status_list)
# print(times)

for index, i in enumerate(range(0, len(times), 2)):
    # df = df.append({"Start": times[i], "End": times[i + 1]}, ignore_index=True) # Deprecated
    df_new_row = pandas.DataFrame(
        {
            'Start': times[i],
            'End': times[i+1],
        },
        index=[index])
    df = pandas.concat([df, df_new_row], ignore_index=True)

df.to_csv("Times.csv")

video.release()

cv2.destroyAllWindows()

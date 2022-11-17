import time
# from cgi import print_form
# import datetime
# from lib2to3.pgen2 import driver
# import re
# import time
# from turtle import color
# import serial
import cv2
import numpy as np
import threading
# from driver import *

time_to_record_data = 10
cam_port = 0


cap = cv2.VideoCapture(cam_port)  # capture video from camera



def mask(framee):
    light_blue = np.array([110, 50, 50])
    dark_blue = np.array([130, 255, 255])
    light_red = np.array([0, 50, 50])
    dark_red = np.array([10, 255, 255])
    light_green = np.array([50, 50, 50])
    dark_green = np.array([70, 255, 255])

    try:
        hsv = cv2.cvtColor(framee, cv2.COLOR_BGR2HSV)

        mask1 = cv2.inRange(hsv, light_green, dark_green)
        output_green = cv2.bitwise_and(framee, framee, mask=mask1)

        mask2 = cv2.inRange(hsv, light_red, dark_red)
        output_red = cv2.bitwise_and(framee, framee, mask=mask2)

        mask3 = cv2.inRange(hsv, light_blue, dark_blue)
        output_blue = cv2.bitwise_and(framee, framee, mask=mask3)

        return output_red, output_green, output_blue

    except Exception as e:
        print(e)


def mean(red_mask, blue_mask, green_mask):
    b = blue_mask[:, :, :1]
    g = green_mask[:, :, 1:2]
    r = red_mask[:, :, 2:3]

    b_mean = np.mean(b)
    g_mean = np.mean(g)
    r_mean = np.mean(r)

    if b_mean > g_mean and b_mean > r_mean:
        print("Blue")
        return "Blue"
    elif g_mean > r_mean and g_mean > b_mean:
        print("Green")
        return "Green"
    elif r_mean > g_mean and r_mean > b_mean:
        print("Red")
        return "Red"
    else:

        return "None"



def find_color():
    endTime = datetime.datetime.now() + datetime.timedelta(seconds=time_to_record_data)
    # open  a data file , if  file not present create one
    f = open("../env/data.txt", "w")
    while datetime.datetime.now() < endTime:
        _, frame = cap.read()
        red_mask, green_mask, blue_mask = mask(frame)
        color = mean(red_mask, blue_mask, green_mask)
        f.write(color)
        f.write("\n")
    f.close()


def read_raw_data():
    f = open("../env/data.txt", "r")
    data = f.read()
    # count the number of times each color appears
    blue_count = data.count("Blue")
    red_count = data.count("Red")
    green_count = data.count("Green")

    if red_count > blue_count and red_count > green_count:
        return "1"  # red
    elif green_count > blue_count and green_count > red_count:
        return "2"  # green
    elif blue_count > red_count and blue_count > green_count:
        return "3"  # blue

    print(blue_count, red_count, green_count)
    f.close()


# def send_data(data):


#     switcher = {
#         "1": red,
#         "2": green,
#         "3": blue
#     }

#     func = switcher.get(data, lambda: "Invalid color")
#     func()







def main():
    return 0
    
    # find_color()

    

    
# identify cube in the frame

# create a function to look for color only in the box

def box_color(frame):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    ret, thresh = cv2.threshold(blur, 60, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            cv2.drawContours(frame, [cnt], 0, (255, 255, 255), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            x = approx.ravel()[0]
            y = approx.ravel()[1]
            #identify the shape of the box and writing it in the frame
            

            if len(approx) == 4:
                cv2.putText(frame, "Cube", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 255, 255), 2)
                crop = frame[y:y + h, x:x + w]
                return crop



            

    return frame 






def cam_display():
    
    while True:
        _, frame = cap.read()
        framee = box_color(frame)
        red_mask, green_mask, blue_mask = mask(frame)
        cv2.imshow("frame", frame)
        cv2.imshow("red", red_mask)
        cv2.imshow("green", green_mask)
        cv2.imshow("blue", blue_mask)
        # framee = box_detection(frame)q
        cv2.imshow("framee", framee)
        # crop = box_color(frame)
        # cv2.imshow("crop", crop)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()



if __name__ == "__main__":
    t1 = threading.Thread(target=cam_display)       # Multithreading
    # t2 = threading.Thread(target=main)
 


    t1.start()
    # t2.start()


    t1.join()
    # t2.join()
   
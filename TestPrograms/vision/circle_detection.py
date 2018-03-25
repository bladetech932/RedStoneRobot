
import cv2
import numpy as np
import os

os.system("raspistill -t 1000 -vf -n -hf -o test.jpg -w 640 -h 480 -q 50")

img = cv2.imread('test.jpg', 0)
img_height, img_width = img.shape
img = cv2.medianBlur(img, 5)
cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1, 20, param1=50,
                           param2=40, minRadius=10, maxRadius=50)

apple = 0
lamp = 0

circles = np.uint16(np.around(circles))

for i in circles[0, :]:
    cv2.circle(cimg, (i[0], i[1]), i[2], (0, 255, 0), 2)

    cv2.circle(cimg, (i[0], i[1]), 2, (0, 0, 255), 3)

    cv2.circle(cimg, (int(img_width/2), int(img_height/2)), 2, (255, 0, 0), 3)

    apple = i[0]
    lamp = i[1]

    cv2.arrowedLine(cimg, (int(img_width/2), int(img_height/2)), (apple, lamp), (0, 89, 217), 2)

    print(apple, ",", lamp)

cv2.imwrite('test_pic_edited.jpg', cimg)

cv2.imshow('detected circles', cimg)

cv2.waitKey(0)

cv2.destroyAllWindows()

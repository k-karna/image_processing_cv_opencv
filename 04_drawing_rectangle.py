from __future__ import print_function

import cv2

image_path = "images/marsrover.jpg"

image = cv2.imread(image_path)

#set the start and end coordinates
# of the top left and bottom-right corners of the rectangle

start = (100,70)
end = (350, 400)

#set the color and thickness of the outline
color = (128, 128, 128)
thickness = 5

#draw the rectangle
cv2.rectangle(image, start, end, thickness)

#save the modified image with the rectangle drawn to it.add()
cv2.imwrite("rectangle.jpg", image)

#display the modified image
cv2.imshow("Rectangle", image)
cv2.waitKey()
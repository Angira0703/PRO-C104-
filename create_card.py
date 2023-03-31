import cv2

read_image = cv2.imread("poster.jpg")
rocket_img = read_image[110:360, 400:500]
read_image[50:300, 500:600]= rocket_img
text = "{I = ([LOVE]); C0d!NG '!'}"
cv2.putText(read_image, text, (20, 220), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale=1, color=(41, 6, 0))
cv2.imshow("Output Window", read_image)
cv2.waitKey(0)





import cv2
import pyperclip

img = cv2.imread("b.jpg", 0)
thresh = 127
img = cv2.resize(img, (80, 16))
im_bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

o = ''
print(im_bw)
for i in range(len(im_bw)):
    for j in range(len(im_bw[i])):
        if im_bw[i][j] == 0:
            o += '.'
        else:
            o += ' '
    o += '\n'

print(o)
pyperclip.copy(o)

cv2.imshow('img', im_bw)

cv2.waitKey(0)




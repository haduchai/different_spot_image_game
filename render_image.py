import cv2
import numpy as np

# Load the image
img = cv2.imread('images\img2.jpg')
raw_img = img.copy()

def changeColor(img, contours, i):
    r, g, b = img[y+h + 10, x+w + 10]
    # random color
    # r, g, b = np.random.randint(0, 255, size=3)
    cv2.drawContours(img,contours,i,(int(r), int(g), int(b)),-1)
    return img

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Threshold the image
# _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
estimatedThreshold, thresh=cv2.threshold(gray,130,255,cv2.THRESH_BINARY)

# Find contours
# contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours, _ = cv2.findContours(thresh, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# Draw contours on a copy of the original image
contour_img = img.copy()

# Remove or change objects in the original image based on the contours
for i, cnt in enumerate(contours):
    areaContour=cv2.contourArea(cnt)
    x, y, w, h = cv2.boundingRect(cnt)
    # Uncomment one of the following lines to remove or change the color of the object
    # nếu diện tích của contour nhỏ hơn 100 thì xóa
    # if w*h < raw_img.shape[0]*raw_img.shape[1]//100*20:
    if  areaContour < 1000 and areaContour > 500:
        # cv2.drawContours(contour_img, cnt, -1, (0, 255, 0), 2)
        cv2.drawContours(contour_img,contours,i,(0,255,0),4)
        try:
            # xóa contour
            # img[y:y+h, x:x+w] = 0
            # img[y:y+h, x:x+w] = img[y+h + 10, x:x+w + 10]
            # img[y:y+h, x:x+w] = (255, 0, 0)
            # change color
            img = changeColor(img, contours, i)
        except:
            pass

# convert the images to jpg
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# contour_img = cv2.cvtColor(contour_img, cv2.COLOR_BGR2RGB)

# show the images
cv2.imshow('Original', raw_img)
cv2.imshow('Contours', contour_img)
cv2.imshow('Modified', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the images
cv2.imwrite('img1.jpg', img)
cv2.imwrite('img2.jpg', raw_img)

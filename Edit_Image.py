import cv2

# Read the image
image = cv2.imread('Python_Logo.png')
# Convert the image into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Display the two images
cv2.imshow('Original', image)
cv2.imshow('Grayscale', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

# Read the image
image = cv2.imread("input.jpg")

# Rotate the image by 180 degrees
rotated = cv2.rotate(image, cv2.ROTATE_180)

# Save the output
cv2.imwrite("rotated_180.jpg", rotated)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("180 Degree Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
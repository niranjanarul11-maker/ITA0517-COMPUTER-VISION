import cv2

# Read the image
image = cv2.imread("input.jpg")

# Get image dimensions
height, width = image.shape[:2]

# Create rotation matrix
center = (width // 2, height // 2)
matrix = cv2.getRotationMatrix2D(center, 45, 1.0)

# Rotate the image
rotated = cv2.warpAffine(image, matrix, (width, height))

# Save the output
cv2.imwrite("rotated.jpg", rotated)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated)

cv2.waitKey(0)
cv2.destroyAllWindows()
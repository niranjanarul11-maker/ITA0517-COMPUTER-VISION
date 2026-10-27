import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

# Get image dimensions
height, width = image.shape[:2]

# Select 3 points from the original image
points1 = np.float32([
    [50, 50],
    [200, 50],
    [50, 200]
])

# Select 3 corresponding points
points2 = np.float32([
    [10, 100],
    [200, 50],
    [100, 250]
])

# Create affine transformation matrix
matrix = cv2.getAffineTransform(points1, points2)

# Apply affine transformation
result = cv2.warpAffine(image, matrix, (width, height))

# Save the output
cv2.imwrite("affine.jpg", result)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Affine Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
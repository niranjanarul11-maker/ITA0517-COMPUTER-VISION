import cv2
import numpy as np

# Read the image
image = cv2.imread("input.jpg")

# Get image dimensions
height, width = image.shape[:2]

# Four points from the original image
points1 = np.float32([
    [50, 50],
    [width - 50, 50],
    [50, height - 50],
    [width - 50, height - 50]
])

# Four destination points
points2 = np.float32([
    [0, 0],
    [width, 0],
    [0, height],
    [width, height]
])

# Create perspective transformation matrix
matrix = cv2.getPerspectiveTransform(points1, points2)

# Apply perspective transformation
result = cv2.warpPerspective(image, matrix, (width, height))

# Save output
cv2.imwrite("perspective.jpg", result)

# Display
cv2.imshow("Original Image", image)
cv2.imshow("Perspective Transformation", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
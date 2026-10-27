import cv2

# Read the image
image = cv2.imread("input.jpg")

# Apply Gaussian blur
blurred = cv2.GaussianBlur(image, (5, 5), 0)

# Save the blurred image
cv2.imwrite("blurred.jpg", blurred)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Gaussian Blurred Image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()
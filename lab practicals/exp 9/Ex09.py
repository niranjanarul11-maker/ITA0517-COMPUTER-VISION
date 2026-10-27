import cv2

# Read the image
image = cv2.imread("input.jpg")

# Resize the image
resized = cv2.resize(image, (400, 300))

# Save the output
cv2.imwrite("resized.jpg", resized)

# Display images
cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()
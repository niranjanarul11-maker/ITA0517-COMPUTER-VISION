import cv2

# Read image
image = cv2.imread("input.jpg")

# Crop a region
roi = image[50:150, 50:150]

# Copy the ROI
copy = roi.copy()

# Paste the ROI at another location
image[50:150, 50:150] = copy

# Save output
cv2.imwrite("roi_result.jpg", image)

# Display
cv2.imshow("ROI Result", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
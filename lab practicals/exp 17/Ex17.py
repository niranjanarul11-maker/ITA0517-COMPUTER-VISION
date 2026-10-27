import cv2

# Read image
image = cv2.imread("input.jpg")

# Add watermark text
cv2.putText(
    image,
    "MY WATERMARK",
    (30, 50),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (255, 255, 255),
    2
)

# Save output
cv2.imwrite("watermarked.jpg", image)

# Display
cv2.imshow("Watermarked Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
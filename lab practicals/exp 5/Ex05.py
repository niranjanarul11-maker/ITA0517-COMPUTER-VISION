import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("input.jpg")

# Calculate histogram for Blue, Green and Red channels
colors = ('b', 'g', 'r')

for i, color in enumerate(colors):
    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color=color)

# Set graph details
plt.xlim([0, 256])
plt.title("Color Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

# Save the histogram
plt.savefig("color_histogram.png")

# Display the histogram
plt.show()
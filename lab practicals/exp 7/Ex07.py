import cv2

# Open the video
video = cv2.VideoCapture("input.mp4")

while True:
    # Read one frame
    ret, frame = video.read()

    # Stop when video ends
    if not ret:
        break

    # Display the frame
    cv2.imshow("Video", frame)

    # Press q to quit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video
video.release()
cv2.destroyAllWindows()
import cv2
import numpy as np

# Create a dummy image
dummy_image = np.zeros((100, 100, 3), dtype=np.uint8)

while True:
    # Display the dummy image in a window named 'Press q to quit'
    cv2.imshow('Press q to quit', dummy_image)

    # Wait for the 'q' key press for 1ms and break the loop if it's pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Destroy all OpenCV windows
cv2.destroyAllWindows()

import cv2

# Define the codec and create a VideoWriter object
# The fourcc code here 'XVID' is just an example, and you might use different ones like 'MP4V' or 'MJPG' depending on your requirements.
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,  480))

# Check if the output is opened successfully
if not out.isOpened():
    print("Error: Couldn't open the output.")

# Don't forget to release the output and destroy all windows when you're done
out.release()
cv2.destroyAllWindows()
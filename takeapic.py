import cv2

def capture_image():
    # Open the default camera
    cap = cv2.VideoCapture(0)

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the captured frame
        cv2.imshow('Press Space to Capture', frame)

        # Wait for the spacebar to be pressed
        if cv2.waitKey(1) & 0xFF == ord(' '):
            # Release the camera
            cap.release()
            cv2.destroyAllWindows()

            # Save the captured frame as a JPEG image
            cv2.imwrite('image.jpg', frame)

            print("Image captured and saved as 'captured_image.jpg'")
            break

if __name__ == "__main__":
    capture_image()

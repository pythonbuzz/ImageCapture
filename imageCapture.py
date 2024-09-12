import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

ret, frame = cap.read()

if ret:
    cv2.imwrite('captured_image.jpg', frame)
    print("Image captured and saved as 'captured_image.jpg'")
else:
    print("Error: Couldn't capture an image.")

cap.release()

cv2.destroyAllWindows()

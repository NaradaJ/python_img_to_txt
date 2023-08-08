import cv2
import pytesseract

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to draw a bounding box on the image
def draw_bounding_box(image, coordinates):
    x1, y1 = coordinates[0]
    x2, y2 = coordinates[1]
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
    cv2.imshow("Image", image)

# Read the image
image_path = r"C:\Users\NArada...RaaZa\Desktop\New folder\Data_Scrap\Advance_Threshold_images\thresholded_img2.png"
image = cv2.imread(image_path)

# Resize the image to a smaller size
full_image = cv2.resize(image, (1024, 768))

# Draw the bounding box using the given coordinates
coordinates = ((288, 394), (467, 418))
draw_bounding_box(small_image, coordinates)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the image with the bounding box
x1, y1 = coordinates[0]
x2, y2 = coordinates[1]
cropped_image = image[y1:y2, x1:x2]
save_path = r"C:\Users\NArada...RaaZa\Desktop\New folder\Data_Scrap\0827\bounding_boxes\bbox1.png"
cv2.imwrite(save_path, cropped_image)
print(f"Image with bounding box saved as {save_path}")

# Perform OCR in the bounding box
text = pytesseract.image_to_string(cropped_image)
print(f"Detected Text in the Bounding Box:")
print(text)

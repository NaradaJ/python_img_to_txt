import cv2
import pytesseract
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Function to handle mouse events
def get_coordinates(event, x, y, flags, param):
    global image, clicked_points, bounding_boxes
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Clicked at coordinates: ({x}, {y})")
        clicked_points.append((x, y))
        
        if len(clicked_points) == 2:
            # Draw a bounding box
            x1, y1 = clicked_points[0]
            x2, y2 = clicked_points[1]
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.imshow("Image", image)
            
            # Store bounding box coordinates
            bounding_boxes.append(((x1, y1), (x2, y2), len(bounding_boxes) + 1))
            clicked_points = []

# Folder containing images
images_folder = r"C:\Users\NArada...RaaZa\Desktop\New folder\Data_Scrap\PNG NEW"

# Loop through images in the folder
for image_file in os.listdir(images_folder):
    image_path = os.path.join(images_folder, image_file)
    image = cv2.imread(image_path)
    
    if image is None:
        print(f"Error loading image: {image_path}")
        continue

    # Set a 4K window size (3840x2160)
    cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Image", 3840, 2160)

    # List to store the clicked points and bounding boxes
    clicked_points = []
    bounding_boxes = []

    # Set the mouse callback function
    cv2.setMouseCallback("Image", get_coordinates)

    while True:
        # Display the image
        cv2.imshow("Image", image)
        key = cv2.waitKey(1) & 0xFF
        
        # Save the bounding boxes and move to the next image
        if key == ord("n"):
            if bounding_boxes:
                for box in bounding_boxes:
                    x1, y1 = box[0]
                    x2, y2 = box[1]
                    box_num = box[2]
                    cropped_image = image[y1:y2, x1:x2]
                    bbx_name = f"bbx_{box_num}_{os.path.basename(image_path)}"
                    cv2.imwrite(os.path.join(images_folder, bbx_name), cropped_image)
                    text = pytesseract.image_to_string(cropped_image)
                    print(f"Detected Text in {bbx_name} (Box {box_num}): {text}")
                bounding_boxes = []
            break
        
        # Exit
        elif key == 27:  # Esc key
            for box in bounding_boxes:
                print(f"Box {box[2]}: Detected Text: {pytesseract.image_to_string(image[box[0][1]:box[1][1], box[0][0]:box[1][0]])}")
            cv2.destroyAllWindows()
            exit()

    cv2.destroyAllWindows()

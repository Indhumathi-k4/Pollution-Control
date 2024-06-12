import cv2
import numpy as np
import matplotlib.pyplot as plt

def identify_and_highlight_planting_areas(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"No image found at {image_path}")
        return

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([36, 25, 25])
    upper_green = np.array([86, 255, 255])
    green_mask = cv2.inRange(hsv_image, lower_green, upper_green)

    lower_gray = np.array([0, 0, 50])
    upper_gray = np.array([180, 18, 230])
    building_mask = cv2.inRange(hsv_image, lower_gray, upper_gray)

    planting_mask = cv2.bitwise_not(cv2.add(green_mask, building_mask))

    kernel = np.ones((15, 15), np.uint8)
    closed_planting_mask = cv2.morphologyEx(planting_mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(closed_planting_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        cv2.drawContours(image, [contour], -1, (0, 255, 255), 2)

    greenery_percentage = np.sum(green_mask == 255) / green_mask.size * 100
    urbanization_level = np.sum(building_mask == 255) / building_mask.size * 100
    plants_needed = int((np.sum(closed_planting_mask == 255) / closed_planting_mask.size) * 10000)

    pollution_level = urbanization_level - (greenery_percentage / 2)
    pollution_level = max(0, min(pollution_level, 100))

    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Adjust subplot parameters to give specified padding
    plt.subplots_adjust(wspace=1/2.54)  # wspace is the width of the padding, 1 cm = 1/2.54 inches (assuming DPI is 100)

    ax[0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    ax[0].set_title('Potential Planting Areas Outlined')
    ax[0].axis('off')

    text_str = [
        f"Greenery Level: {greenery_percentage:.2f}%",
        f"Urbanization Level: {urbanization_level:.2f}%",
        f"Estimated Number of Plants Needed: {plants_needed}",
        f"Simplified Pollution Level: {pollution_level:.2f}%"
    ]
    colors = ['green', 'red', 'blue', 'purple']
    
    text_position = 0.9  # Starting Y position for text
    for i, (text, color) in enumerate(zip(text_str, colors)):
        ax[1].text(0.01, text_position-(i*0.1), text, color=color, transform=ax[1].transAxes, fontsize=12, ha='left', va='top')
        # Adjusted text positioning and alignment

    ax[1].axis('off')
    plt.show()

    

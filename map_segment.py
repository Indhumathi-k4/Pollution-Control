import cv2

def crop_image_opencv(input_image_path, output_image_path, crop_area):
    image = cv2.imread(input_image_path)
    cropped_image = image[crop_area[1]:crop_area[1]+crop_area[3], crop_area[0]:crop_area[0]+crop_area[2]]
    cv2.imwrite(output_image_path, cropped_image)

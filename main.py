from place import search_and_capture
from map_segment import crop_image_opencv
from pollution import identify_and_highlight_planting_areas

if __name__ == "__main__":
    place = input("Enter the place to search in Google Earth: ")
    search_and_capture(place)

    input_image = r"C:\Users\prave\OneDrive\Desktop\final_year_project\Input_Image.png"
    output_image = r"C:\Users\prave\OneDrive\Desktop\final_year_project\Map_Segment.png"
    crop_area = (550, 50, 400, 350)

    crop_image_opencv(input_image, output_image, crop_area)

    identify_and_highlight_planting_areas(output_image)

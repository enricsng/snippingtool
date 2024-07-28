import os
import json
from find_edges import get_all_screenshots, do_screenshots

use_last_default = True if input("Use last default settings? (y/n) ").lower() == "y" else False

if os.path.exists("state.json"):
    with open("state.json") as fp:
        program_config = json.load(fp)
else:
    # Failsafe default config
    program_config = {'screenshot_coordinates': {'x_left': 233, 'x_mid': 1280, 'y_top': 75, 'y_bottom': 1555}, 
                      'test_coordinates': {'x_left': 220, 'x_mid': 1260, 'y_top': 60, 'y_bottom': 1550},
                      'prev_page': 0}
    
screenshot_coordinates = program_config["screenshot_coordinates"]

if not use_last_default:

    if input("Change screenshot coordinates? (y/n) ").lower() ==  "y":
        test_coordinates = program_config["test_coordinates"]
        filenames = get_all_screenshots(test_coordinates)

        screenshot_coordinates["x_left"] = int(input("Enter x_left coordinate: "))
        screenshot_coordinates["x_mid"] = int(input("Enter x_mid coordinate: "))
        screenshot_coordinates["y_top"] = int(input("Enter y_top coordinate: "))
        screenshot_coordinates["y_bottom"] = int(input("Enter y_bottom coordinate: "))
    
        # Files cleanup
        for file_name in filenames:
            if os.path.exists(file_name):
                os.remove(file_name)
    
    if input("Reset first page? (y/n) ").lower() == "y":
        program_config['prev_page'] = 0

    
while True:

    page_num = int(input("Enter number of pages: "))

    prev_page = do_screenshots(screenshot_coordinates, page_num, program_config["prev_page"] + 1)

    print(f"Last taken page: {prev_page}")

    program_config["prev_page"] = prev_page

    if input("Do you wish to continue? (y/n) ").lower() == "n":
        break

# Write back everything to the drive
with open("state.json", "w") as fp:
    json.dump(program_config, fp)
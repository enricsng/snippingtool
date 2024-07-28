import pyautogui
import time
'''
Usual coordinates for 100%
x_left = 220 - 233 - 249
x_mid  = 1260 - 1280 - 1289

y_top = 60 - 75 - 89
y_bottom = 1550 - 1555 - 1579

'''

def get_all_screenshots(coordinates):
    filenames = []

    filenames += take_screenshot(coordinates.get("x_left"),coordinates.get("y_top"), "left")
    filenames += take_screenshot(coordinates.get("x_mid"),coordinates.get("y_top"), "left")
    filenames += take_screenshot(coordinates.get("x_mid"),coordinates.get("y_top"), "top")
    filenames += take_screenshot(coordinates.get("x_mid"),coordinates.get("y_bottom"), "top")

    return filenames

# Define a screenshot function that takes 5 screenshots at varying coordinates
def take_screenshot(left, top, mode, num_test=30, increment=1):
    filenames = []

    for i in range(1, num_test + 1):
        file_name = f'{left}x{top}.jpg'
        filenames.append(file_name)
        open(file_name, 'w').close()
        image = pyautogui.screenshot(region=(left, top, 100, 100))
        image.save(file_name, quality=95)
        if mode == 'left':
            left += increment
        else:
            top += increment
    return filenames

# Take the whole screenshots given the boundaries and start number
def do_screenshots(screenshot_coordinates, page_num, start_page):

    x_left = screenshot_coordinates["x_left"]
    x_mid = screenshot_coordinates["x_mid"]
    y_top = screenshot_coordinates["y_top"]
    y_bottom = screenshot_coordinates["y_bottom"]

    WIDTH = x_mid - x_left
    HEIGHT = y_bottom - y_top

    prev_page = 0

    for i in range(start_page, page_num + start_page + 1, 2):
        open(f'page {i}.jpg', 'w').close()
        open(f'page {i+1}.jpg', 'w').close()

        image1 = pyautogui.screenshot(region=(x_left, y_top, WIDTH, HEIGHT))
        image1.save(f'page {i}.jpg', quality=95)

        image2 = pyautogui.screenshot(region=(x_mid, y_top, WIDTH, HEIGHT))
        # print(f'page {i+1}.jpg')
        image2.save(f'page {i+1}.jpg', quality=95)
        
        pyautogui.click(2530, 50)
        prev_page = i + 1
        time.sleep(1)
    return prev_page
        
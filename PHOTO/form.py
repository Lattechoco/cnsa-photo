'''
 ____                        __              
/\  _`\                     /\ \__           
\ \ \L\ \    __        ____   \ \ ,_\      __   
 \ \ ,__/  /'__`\     /',__ \  \ \ \/    /'__`\ 
  \ \ \/  /\ \L\.\_  /\__, `\   \ \ \_  /\  __/ 
   \ \_\  \ \__/.\_\ \/\____/    \ \__\ \ \____|
    \/_/   \/__/\/_/  \/___/      \/__/  \/____/
'''
import cv2
from datetime import datetime
import qr

# Img Resize Function
def resize_image_keep_aspect_ratio(image, new_width, new_height):
    height, width = image.shape[:2]
    aspect_ratio = width / height
    aspect_height = int(new_width / aspect_ratio)
    if aspect_height > new_height:
        new_height = aspect_height
    else:
        new_width = int(new_height * aspect_ratio)
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

# Img Add Function
def paste(p1, p2, p3, p4, f_t, q):
    pos_l = [107, 465, 820, 1178] # Position List
    pic_l = [p1, p2, p3, p4] # Img Num

    img_name = 'PHOTO/static/image/img_' # Img Location
    img_ext = '.webp'

    frame_name = 'PHOTO/static/image/frame_' # Frame Location
    frame_ext = '.png'

    image2 = cv2.imread(frame_name + str(f_t) + frame_ext)

    past_image = None

    for i in range(4):
        img_full_name = img_name + str(pic_l[i]) + img_ext
        print(img_full_name)
        image1 = cv2.imread(img_full_name)

        # Resize Width To 528
        resized_image1 = resize_image_keep_aspect_ratio(image1, 528, 320)
        width, height = resized_image1.shape[:2]

        # Resize Height To 320
        crop_image1 = resized_image1[:320, :height]

        # Paste image1 To image2
        image2[pos_l[i]:pos_l[i] + crop_image1.shape[0], 133:133 + crop_image1.shape[1]] = crop_image1

    # Cut Img
    output = image2[64:1786, 86:703]
    
    # Save Img
    file_path = "PHOTO/static/image/result"+str(datetime.today())+".png"
    cv2.imwrite(file_path, output)
    qr.file_set(file_path)
import cv2
from datetime import datetime

def resize_image_keep_aspect_ratio(image, new_width, new_height):
    height, width = image.shape[:2]
    aspect_ratio = width / height
    aspect_height = int(new_width / aspect_ratio)
    if aspect_height > new_height:
        new_height = aspect_height
    else:
        new_width = int(new_height * aspect_ratio)
    return cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LANCZOS4)

def paste(p1, p2, p3, p4, f_t, q):
    pos_l = [107, 465, 820, 1178]  # Position List
    pic_l = [p1, p2, p3, p4]

    img_name = 'PHOTO/static/image/img_'
    img_ext = '.webp'

    frame_name = 'PHOTO/static/image/frame_'
    frame_ext = '.png'

    # 2번 사진 열기
    image2 = cv2.imread(frame_name + str(f_t) + frame_ext)

    # 이전에 합성한 이미지를 저장하는 변수
    past_image = None

    for i in range(4):
        img_full_name = img_name + str(pic_l[i]) + img_ext
        print(img_full_name)
        image1 = cv2.imread(img_full_name)

        # 이전 이미지의 비율 유지하며 가로(width) 크기를 528로 조정
        resized_image1 = resize_image_keep_aspect_ratio(image1, 528, 320)
        width, height = resized_image1.shape[:2]

        # 이미지를 320 높이로 자르기
        crop_image1 = resized_image1[:320, :height]

        # 자른 이미지를 2번 사진에 붙여넣기
        image2[pos_l[i]:pos_l[i] + crop_image1.shape[0], 133:133 + crop_image1.shape[1]] = crop_image1

    output = image2[64:1786, 86:703]
    cv2.imwrite("/Users/steal/Documents/vs_code/PHOTO/static/result"+str(datetime.today())+".png", output)

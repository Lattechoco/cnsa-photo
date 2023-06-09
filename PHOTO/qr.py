import dropbox
import os
import qrcode

# Set up Dropbox API
access_token = 'YOUR_DROPBOX_API_KEY'
dbx = dropbox.Dropbox(access_token)

def file_set(file_path):
    # Specify the path to the local image file
    local_image_path = file_path
    
    # Specify the path to the remote Dropbox folder where you want to upload the image
    remote_folder = '/Apps/cnsa-photo/test.png'

    # Get the base name of the image file
    image_basename = os.path.basename(local_image_path)

    # Specify the path to the remote Dropbox file
    remote_image_path = remote_folder + image_basename

    # Upload the image file
    with open(local_image_path, 'rb') as f:
        dbx.files_upload(f.read(), remote_image_path)

    # Get the shared link for the uploaded image
    shared_link = dbx.sharing_create_shared_link(remote_image_path)

    # Get the download URL
    download_url = shared_link.url.replace('dl=0', 'dl=1')
    
    make_qr(download_url)
    
def make_qr(download_url):
    # URL
    url = download_url

    # QR 코드 이미지 생성
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    # QR 코드 이미지를 파일로 저장
    image = qr.make_image(fill_color="black", back_color="white")
    image.save("PHOTO/static/image/qr.png")

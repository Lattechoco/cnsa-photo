import dropbox
import os
import qrcode

##===== URL_API =====##
# https://www.dropbox.com/developers/apps/info/zf048g0xzr8b6kp
##===== URL_API =====##
# Set up Dropbox API

access_token = 'sl.BhghyEFlcsSvNHzFV0wmJR6A2amqNgc2aAfNJLllen81cq5qSEAA1cDpENIeGtDw8kWiwXt1i4P75zAf0p936jHKfF6LChgds_-_hudDjjbO86NE_N9BvNELVrN8SpVHRzmJckLhssMA'
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

    # Generate QR
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)

    # Save QR
    image = qr.make_image(fill_color="black", back_color="white")
    image.save("PHOTO/static/image/qr.png")

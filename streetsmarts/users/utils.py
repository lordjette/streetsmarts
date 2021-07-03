import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from streetsmarts import mail


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    #output_size = (125, 125)
    thumb_width = 125 #nt
    i = Image.open(form_picture)
    
    def crop_center(pil_img, crop_width, crop_height):
        img_width, img_height = pil_img.size
        return pil_img.crop(((img_width - crop_width) // 2,
                         (img_height - crop_height) // 2,
                         (img_width + crop_width) // 2,
                         (img_height + crop_height) // 2))

    def crop_max_square(pil_img):
        return crop_center(pil_img, min(pil_img.size), min(pil_img.size))

    y = crop_max_square(i).resize((thumb_width, thumb_width), Image.LANCZOS)
    #y.thumbnail(output_size)
    y.save(picture_path, quality=95)
    return picture_fn



#RESET EMAIL, we define function
def send_reset_email(user):
    token = user.get_reset_token()   #get_reset_token() from models
    msg = Message('Password Reset Request', 
                    sender='noreply@demo.com',
                    recipients =[user.email])

    #_external=True  , link of URL has full domain
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made
'''
    mail.send(msg)

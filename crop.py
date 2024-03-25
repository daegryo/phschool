from PIL import ImageFont, ImageDraw, Image, ImageOps
from IPython.display import Image as jpImg


def circle_crop(filename, size, color):
    image = Image.new('RGB', size, color = color)
    draw = ImageDraw.Draw(image)

    # draw the border
    avatar_size = size
    x_offset, y_offset = 0, 0
    border_bounding = [x_offset, y_offset, x_offset+avatar_size[0], y_offset+avatar_size[1]]
    draw.ellipse(border_bounding, fill=color)

    # make it into a mask, but scale it down slightly so we have a border
    border_size = 25
    mask = Image.new('L', [ x-border_size for x in avatar_size ], 0)
    mask_draw = ImageDraw.Draw(mask)
    mask_draw.ellipse([0,0,*mask.size], fill=255)

    # crop the avatar into the smaller circle
    avatar = Image.open(f'static/uploads/images/{filename}').convert('RGB')
    output = ImageOps.fit(avatar, mask.size, centering=(0.5, 0.5))
    output.putalpha(mask)

    # now drop that in the center of where our cicle is
    image.paste(output, (x_offset+(border_size//2), y_offset+(border_size//2)), output)

    jpImg(image, filename='static/uploads/images/Forest.jpg')
    return image


img_ava = circle_crop('default.jpg',(100, 100), '#727d71')
img_ava.save(f'static/avatars/default.jpg')

from PIL import Image


def crop_image(img_path):
    image = Image.open(img_path)
    width, height = image.size
    if width > height:
        x = (width - height) // 2
        image = image.crop((x, 0, width - x, height))
    elif height > width:
        y = (height - width) // 2
        image = image.crop((0, y, width, height - y))
    image.save(img_path)

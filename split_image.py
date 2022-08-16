import PIL
from PIL import Image
import os

def split_image(img_path, n, seeds):
    img = Image.open(img_path)
    output_path = os.path.dirname(img_path) + '/'
    if n == 1:
        return img
    w, h = img.size
    if n == 2: 
        img1 = img.crop((0, 0, w // 2, h))
        img2 = img.crop((w // 2, 0, w, h))
        img1.save(output_path + str(seeds[0]) + '.png')
        img2.save(output_path + str(seeds[1]) + '.png')
    if n == 3:
        img1 = img.crop((0, 0, w // 3, h))
        img2 = img.crop((w // 3, 0, 2 * w // 3, h))
        img3 = img.crop((2 * w // 3, 0, w, h))
        img1.save(output_path + str(seeds[0]) + '.png')
        img2.save(output_path + str(seeds[1]) + '.png')
        img3.save(output_path + str(seeds[2]) + '.png')
    if n == 4:
        img1 = img.crop((0, 0, w // 2, h // 2))
        img2 = img.crop((w // 2, 0, w, h // 2))
        img3 = img.crop((0, h // 2, w // 2, h))
        img4 = img.crop((w // 2, h // 2, w, h))
        img1.save(output_path + str(seeds[0]) + '.png')
        img2.save(output_path + str(seeds[1]) + '.png')
        img3.save(output_path + str(seeds[2]) + '.png')
        img4.save(output_path + str(seeds[3]) + '.png')
    else:
        print('grid sizes greater than 4 are not currently supported')


# split_image('images/this is a test/grid.png', 2, [1,2])
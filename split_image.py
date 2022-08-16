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
    elif n == 3:
        img1 = img.crop((0, 0, w // 3, h))
        img2 = img.crop((w // 3, 0, 2 * w // 3, h))
        img3 = img.crop((2 * w // 3, 0, w, h))
        img1.save(output_path + str(seeds[0]) + '.png')
        img2.save(output_path + str(seeds[1]) + '.png')
        img3.save(output_path + str(seeds[2]) + '.png')
    elif n == 4:
        img1 = img.crop((0, 0, w // 2, h // 2))
        img2 = img.crop((w // 2, 0, w, h // 2))
        img3 = img.crop((0, h // 2, w // 2, h))
        img4 = img.crop((w // 2, h // 2, w, h))
        img1.save(output_path + str(seeds[0]) + '.png')
        img2.save(output_path + str(seeds[1]) + '.png')
        img3.save(output_path + str(seeds[2]) + '.png')
        img4.save(output_path + str(seeds[3]) + '.png')
    elif n == 6:
        img1 = img.crop((0, 0, w // 3, h // 2))
        img2 = img.crop((w // 3, 0, 2 * w // 3, h // 2))
        img3 = img.crop((2 * w // 3, 0, w, h // 2))
        img4 = img.crop((0, h // 2, w // 3, h))
        img5 = img.crop((w // 3, h // 2, 2 * w // 3, h))
        img6 = img.crop((2 * w // 3, h // 2, w, h))
        img1.save(output_path + str(seeds[0]) + '.png')
        img2.save(output_path + str(seeds[1]) + '.png')
        img3.save(output_path + str(seeds[2]) + '.png')
        img4.save(output_path + str(seeds[3]) + '.png')
        img5.save(output_path + str(seeds[4]) + '.png')
        img6.save(output_path + str(seeds[5]) + '.png')
    elif n == 9:
        img1 = img.crop((0, 0, w // 3, h // 3))
        img2 = img.crop((w // 3, 0, 2 * w // 3, h // 3))
        img3 = img.crop((2 * w // 3, 0, w, h // 3))
        img4 = img.crop((0, h // 3, w // 3, 2 * h // 3))
        img5 = img.crop((w // 3, h // 3, 2 * w // 3, 2 * h // 3))
        img6 = img.crop((2 * w // 3, h // 3, w, 2 * h // 3))
        img7 = img.crop((0, 2 * h // 3, w // 3, h))
        img8 = img.crop((w // 3, 2 * h // 3, 2 * w // 3, h))
        img9 = img.crop((2 * w // 3, 2 * h // 3, w, h))
        img1.save(output_path + str(seeds[0]) + '.png')
        img2.save(output_path + str(seeds[1]) + '.png')
        img3.save(output_path + str(seeds[2]) + '.png')
        img4.save(output_path + str(seeds[3]) + '.png')
        img5.save(output_path + str(seeds[4]) + '.png')
        img6.save(output_path + str(seeds[5]) + '.png')
        img7.save(output_path + str(seeds[6]) + '.png')
        img8.save(output_path + str(seeds[7]) + '.png')
        img9.save(output_path + str(seeds[8]) + '.png')
    else:
        print(f'Grid size {n} is not currently supported')


# split_image('images/this is a test/grid.png', 2, [1,2])

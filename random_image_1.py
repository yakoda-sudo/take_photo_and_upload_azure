 ## display the latest image in the photo directory

from waveshare_epd import epd5in65f
from PIL import Image
from PIL import ImageDraw
import time
import os
#import random
import glob

#the resolution of 5.65 epaper display
EPD_WIDTH = 600
EPD_HEIGHT = 448

#define palette array
palettedata = [
        0, 0, 0,
        255, 255, 255,
        67, 138, 28,
	100, 64, 255,
        191, 0, 0,
        255, 243, 56,
        232, 126, 0,
        194 ,164 , 244
    ]
p_img = Image.new('P', (16, 16))
p_img.putpalette(palettedata * 32)

#display the latest image from camera
def choose_random_loading_image(path):
#    images=os.listdir(path)
    list_file = glob.glob(path)
#    loading_image=random.randint(0,len(images)-1)
    loading_image = max(list_file, key=os.path.getctime)
    return loading_image
#    return path+images[loading_image]

def main():
    epd = epd5in65f.EPD()
    epd.init()
    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    ImageDraw.Draw(image)
    image = Image.open(choose_random_loading_image('jpg/*'))
#    logging.info("1.Drawing on the image...")
#    print('the loaded pic is:', image)
#   rotate the vertical image
    h, w = image.size
    if h < w:
        image = image.rotate(270, expand=True)
    else:
        pass
#   resize the source image to target resolution
    resized_img = image.resize((EPD_WIDTH, EPD_HEIGHT))
#   replace the color to use 7 color palette
    colored_img = resized_img.quantize(palette=p_img)
    epd.display(epd.getbuffer(colored_img))
#    time.sleep(7200)  # change the image every 2 hour
    exit()
    main()


if __name__ == '__main__':
    main()

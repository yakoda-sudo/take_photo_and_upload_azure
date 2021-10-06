#get&display the latest image and analysis with face API
from waveshare_epd import epd5in65f
from PIL import Image
from PIL import ImageDraw, ImageFont
import time
import os
#import random
import glob
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
#the resolution of 5.65 epaper display
EPD_WIDTH = 600
EPD_HEIGHT = 448
#define the face client
KEY = "your_API_Key"
# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://your_endpoint.cognitiveservices.azure.com/"
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
myfont = ImageFont.truetype('font/tahoma.ttf', 32)

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
#
def choose_random_loading_image(path):
#    images=os.listdir(path)
    list_file = glob.glob(path)
#    loading_image=random.randint(0,len(images)-1)
    loading_image = max(list_file, key=os.path.getctime)
    return loading_image
#    return path+images[loading_image]

local_image = open(choose_random_loading_image('jpg/*'), 'rb')

#print("current pic name is: ", local_image)

response_detection = face_client.face.detect_with_stream(
    image=local_image,
    detection_model='detection_01',
    recognition_model='recognition_04',
    return_face_attributes=['age', 'emotion'],
    return_face_landmarks=True,
)
print(vars(response_detection[0]))
img = Image.open(local_image)
draw = ImageDraw.Draw(img)

for face in response_detection:
    rect = face.face_rectangle
    left = rect.left
    top = rect.top
    right = left + rect.width
    bottom = top + rect.height
    draw.rectangle(((left, top), (right, bottom)), outline='green', width=7)
    age = face.face_attributes.age
    emotion = face.face_attributes.emotion
    neutral = '{0:.0f}%'.format(emotion.neutral * 100)
    happiness = '{0:.0f}%'.format(emotion.happiness * 100)
    anger = '{0:.0f}%'.format(emotion.anger * 100)
    sadness = '{0:.0f}%'.format(emotion.sadness * 100)
    x = face.face_landmarks.nose_tip.x
    y = face.face_landmarks.nose_tip.y
    draw.ellipse(((x - 40, y - 40), (x + 40, y + 40)), fill='#cc0700', width=2)
    draw.ellipse(((x - 12, y - 12), (x + 5, y + 5)), fill='white', width=2)
    draw.text((right + 4, top), 'Age: ' + str(int(age)), fill='red', font=myfont)
    draw.text((right + 4, top + 35), 'Neutral: ' + neutral, fill='red', font=myfont)
    draw.text((right + 4, top + 70), 'Happy: ' + happiness, fill='red', font=myfont)
    draw.text((right + 4, top + 105), 'Sad: ' + sadness, fill='red', font=myfont)
    draw.text((right + 4, top + 140), 'Angry: ' + anger, fill='red', font=myfont)


def main():
    epd = epd5in65f.EPD()
    epd.init()
    # For simplicity, the arguments are explicit numerical coordinates
    image = Image.new('1', (EPD_WIDTH, EPD_HEIGHT), 1)    # 1: clear the frame
    ImageDraw.Draw(image)
#    image = Image.open(choose_random_loading_image('jpg/*'))
    image = img
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

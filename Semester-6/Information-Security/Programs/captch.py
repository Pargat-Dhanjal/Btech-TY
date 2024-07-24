from captcha.image import ImageCaptcha
import random
import string

def generateCaptcha():
    R1 = random.randint(3, 9)
    captcha = []
    for i in range(R1):
        R2 = random.randint(0, 9)
        if R2 < 6:
            R3 = random.randint(0, 9)
            captcha.append(str(R3))
        else:
            R3 = random.choice(string.ascii_letters)
            captcha.append(R3)

    return captcha

def createImageCaptcha(captcha_text, image_path='CAPTCHA.png'):
    image = ImageCaptcha(width=280, height=90)
    data = image.generate(captcha_text)
    image.write(captcha_text, image_path)
    return image_path

captcha = generateCaptcha()
captcha_text = ''.join(captcha)
image_path = createImageCaptcha(captcha_text)

print("Image-based Captcha generated. Please enter the following captcha:")
print(f"Image path: {image_path}")

user_input = input("Enter the captcha shown in the image: ")

if user_input == captcha_text:
    print("Captcha matches")
else:
    print("Captcha didn't match")

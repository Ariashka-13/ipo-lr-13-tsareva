from PIL import Image

class ImageHandler:
    def __init__(self, image):
        self.image = image
    
    def load_image(self):
        self.image = Image.open('image_2.jpg')

    def save_changed_image(self, new_name):
        self.image.thumbnail((200,200))
        self.image.save(new_name)

    def get_image(self):
        return self.image

    
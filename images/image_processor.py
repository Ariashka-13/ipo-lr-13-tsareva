from PIL import ImageFilter, ImageFont, ImageDraw

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def filter_contour(self):
        self.image = self.image.filter(ImageFilter.CONTOUR)

    def text_on_image(self):
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype("arial.ttf", 40)
        text = "Вариант 3"
        
        # Получаем размеры изображения
        img_width, img_height = self.image.size

        # Используем getbbox для получения размеров текста
        bbox = font.getbbox(text)
        text_width, text_height = bbox[2], bbox[3]

        # Вычисляем координаты для центрирования текста
        x = (img_width - text_width) // 2
        y = (img_height - text_height) // 2
        
        # Добавляем текст на изображение
        draw.text((x, y), text, font=font, fill="blue")

    def get_image(self):
        return self.image

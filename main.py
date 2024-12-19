from images.image_handler import ImageHandler
from images.image_processor import ImageProcessor

image_handler = ImageHandler("image_2.jpg")
image_handler.load_image()

image_handler.save_changed_image("new_image_2.jpg")

image_processor = ImageProcessor(image_handler.get_image())

image_processor.filter_contour()
image_processor.text_on_image()

processed_image = image_processor.get_image()
image_handler.image = processed_image
image_handler.save_changed_image("changed_image_2.jpg")

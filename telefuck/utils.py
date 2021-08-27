from PIL import Image

__all__ = ("create_image",)


def create_image(image_data: str, height: int = 63, width: int = 63) -> Image.Image:
    pixels = [int(i) for i in image_data]
    image = Image.new("1", (height, width))
    image.putdata(pixels)
    return image

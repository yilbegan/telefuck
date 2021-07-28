from PIL import Image

__all__ = ("create_image",)


def create_image(image_data: str, height: int = 63, width: int = 63) -> Image.Image:
    pixels = []
    for char in image_data:
        byte = ord(char)
        bits = bin(byte)[2:-1].rjust(7, "0")
        pixels.extend(map(int, bits))
    image = Image.new("1", (height, width))
    image.putdata(pixels)
    return image

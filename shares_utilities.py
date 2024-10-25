from PIL import Image
from random import randint
from constants import BLACK, WHITE


# Funkcja tworzaca udziały
def create_shares(image_path, method):
    tiles = method()

    image = Image.open(image_path)
    image = image.convert('RGB')

    width, height = image.size

    share1 = Image.new('RGB', (2*width, 2*height))
    share2 = Image.new('RGB', (2*width, 2*height))

    image_pixels = image.load()
    share1_pixels = share1.load()
    share2_pixels = share2.load()

    for y in range(0, height):
        for x in range(0, width):
            random_tile = tiles[randint(0, len(tiles) - 1)]

            if image_pixels[x, y] == BLACK:
                random_tile.assign(share1_pixels, x, y, False)
                random_tile.assign(share2_pixels, x, y, True)

            else:
                random_tile.assign(share1_pixels, x, y, False)
                random_tile.assign(share2_pixels, x, y, False)

    return share1, share2


# Funkcja nakladajaca udziały na siebie
def overlay_shares(share1, share2):
    width, height = share1.size

    result = Image.new('RGB', (width, height))

    share1_pixels = share1.load()
    share2_pixels = share2.load()
    result_pixels = result.load()

    for y in range(0, height):
        for x in range(0, width):
            if share1_pixels[x, y] == BLACK or share2_pixels[x, y] == BLACK:
                result_pixels[x, y] = BLACK
            else:
                result_pixels[x, y] = WHITE

    return result

from constants import BLACK, WHITE


# Klasa reprezentujaca kafelek o rozmiarze 2x2 pikseli
class Tile:
    def __init__(self, colors):
        self.colors = colors
        self.negative = [None for i in range(0, len(colors))]
        self.create_negative()

    # Funkcja tworząca negatyw kafelka
    def create_negative(self):
        for i, val in enumerate(self.colors):
            self.negative[i] = WHITE if val == BLACK else BLACK

    # Funkcja przypisująca kafelek do udziału
    def assign(self, image_pixels, x, y, is_negative):
        assigning_values = self.negative if is_negative else self.colors

        image_pixels[2 * x, 2 * y] = assigning_values[0]
        image_pixels[2 * x, 2 * y + 1] = assigning_values[1]
        image_pixels[2 * x + 1, 2 * y] = assigning_values[2]
        image_pixels[2 * x + 1, 2 * y + 1] = assigning_values[3]

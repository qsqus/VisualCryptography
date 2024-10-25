from tile import Tile
from constants import *


class TileGenerator:

    # Funkcja tworząca zbiór 16 kafelków - wszystkie możliwe
    @staticmethod
    def full_random():
        tiles = []

        for c1 in COLORS:
            for c2 in COLORS:
                for c3 in COLORS:
                    for c4 in COLORS:
                        tiles.append(Tile((c1, c2, c3, c4)))

        return tiles

    # Funkcja tworząca zbiór 15 kafelków - bez całego czarnego (przecieki danych)
    @staticmethod
    def no_black():
        tiles = TileGenerator.full_random()

        for t in tiles:
            if t.colors.count(BLACK) == 4:
                tiles.remove(t)
                break

        return tiles

    # Funkcja tworząca zbiór 15 kafelków - bez całego białego (przecieki danych)
    @staticmethod
    def no_white():
        tiles = TileGenerator.full_random()

        for t in tiles:
            if t.colors.count(WHITE) == 4:
                tiles.remove(t)
                break

        return tiles

    # Funkcja tworząca zbiór 14 kafelków - bez całego czarnego i bez całego białego
    @staticmethod
    def no_black_white():
        tiles = TileGenerator.full_random()
        tile_set = []

        for t in tiles:
            if not(t.colors.count(BLACK) == 4 or t.colors.count(WHITE) == 4):
                tile_set.append(t)

        return tile_set

    # Funkcja tworząca zbiór Naora-Shamira - 6 zbalansowanych kafelków
    @staticmethod
    def naor_shamir():
        tiles = TileGenerator.full_random()
        tile_set = []

        for t in tiles:
            if t.colors.count(BLACK) == 2:
                tile_set.append(t)

        return tile_set

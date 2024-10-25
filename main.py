from shares_utilities import create_shares, overlay_shares
from tile_generator import TileGenerator


# Funkcja wyświetlająca udziały i wynik
def show_shares_and_result(image_path, method, save_images=False, file_name=''):
    s1, s2 = create_shares(image_path, method)
    r = overlay_shares(s1, s2)

    if save_images:
        s1.save(f'share1_{file_name}.png')
        s2.save(f'share2_{file_name}.png')
        r.save(f'result_{file_name}.png')

    s1.show()
    s2.show()
    r.show()


if __name__ == "__main__":
    path = input("Image path: ")

    try:
        with open(path, 'r'):
            pass
    except FileNotFoundError:
        print(f"Error: '{path}' is no a valid path")
        exit()

    method_name = input("Method (full_random / no_black / no_white / no_black_white / naor_shamir): ")

    try:
        method = getattr(TileGenerator, method_name)
    except AttributeError:
        print(f"Error: '{method_name}' is not a valid method")
        exit()

    save_images = True if input("Save images? (T / F): ") == "T" else False

    show_shares_and_result(path, method, save_images)

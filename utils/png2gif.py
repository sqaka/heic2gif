from PIL import Image
import os
from natsort import natsorted

INPUT_DIR = "input/rename/"
OUTPUT_DIR = "output/"


def generate_list(list_file_name, input_dir):
    dir = input_dir
    for file_name in os.listdir(dir):
        if file_name.endswith('png'):
            list_file_name.append(file_name)
    list_file_name = natsorted(list_file_name)
    return list_file_name


def png2gif(list_file_name, input_dir, list_images, gif_name):
    for i in list_file_name:
        i = (f'{input_dir}{i}')
        img = Image.open(i)
        list_images.append(img)
    list_images[0].save(f'{OUTPUT_DIR}{gif_name}.gif', save_all=True, append_images=list_images[1:],
                        optimize=True, duration=200, loop=0)


def main(dir_name, gif_name):
    list_file_name = []
    list_images = []
    input_dir = (f'{INPUT_DIR}{dir_name}')
    output_dir = (f'{OUTPUT_DIR}{dir_name}')
    os.makedirs(output_dir, exist_ok=True)
    list_file_name = generate_list(list_file_name, input_dir)
    png2gif(list_file_name, input_dir, list_images, gif_name)


if __name__ == "__main__":
    main()

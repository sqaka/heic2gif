import os
from PIL import Image
import pillow_heif

HEIC_DIR = "input/heic/"
PNG_DIR = "input/png/"


def get_heic_files(input_dir):
    heic_files = [f for f in os.listdir(input_dir) if f.endswith('.heic')]
    return heic_files


def heic2png(heic_files, input_dir, output_dir):
    for heic_file in heic_files:
        heic_path = os.path.join(input_dir, heic_file)

        png_file = os.path.splitext(heic_file)[0] + '.png'
        png_path = os.path.join(output_dir, png_file)

        heif_file = pillow_heif.read_heif(heic_path)
        image = Image.frombytes(
            heif_file.mode,
            heif_file.size,
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        image.save(png_path, 'PNG')

        print(f'{heic_file} を {png_file} に変換しました。')

    print('変換が完了しました。')


def main(dir_name):
    input_dir = (f'{HEIC_DIR}{dir_name}')
    output_dir = (f'{PNG_DIR}{dir_name}')
    os.makedirs(output_dir, exist_ok=True)
    heic_files = get_heic_files(input_dir)
    heic2png(heic_files, input_dir, output_dir)


if __name__ == "__main__":
    main()

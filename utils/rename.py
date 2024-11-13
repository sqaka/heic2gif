import os
import glob
from natsort import natsorted

PNG_DIR = "input/png/"
RENAME_DIR = "input/rename/"


def get_png_files(input_dir, output_dir):
    files = glob.glob(f'{input_dir}*')
    sorted_files = natsorted(files)

    for idx, f in enumerate(sorted_files):
        ftitle, fext = os.path.splitext(f)
        os.rename(f, (f'{output_dir}{idx}{fext}'))


def main(dir_name):
    input_dir = (f'{PNG_DIR}{dir_name}')
    output_dir = (f'{RENAME_DIR}{dir_name}')
    os.makedirs(output_dir, exist_ok=True)
    get_png_files(input_dir, output_dir)


if __name__ == "__main__":
    main()

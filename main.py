import click

from utils.heic2png import main as heic2png
from utils.rename import main as rename
from utils.png2gif import main as png2gif


@click.command()
@click.option('--heic_dir', '-h', type=str, default='')
@click.option('--png_dir', '-p', type=str, default='')
@click.option('--rename_dir', '-r', type=str, default='')
@click.option('--gif_name', '-g', type=str, default='')
def main(heic_dir, png_dir, rename_dir, gif_name):
    heic2png(heic_dir)
    rename(png_dir)
    png2gif(rename_dir, gif_name)


if __name__ == '__main__':
    main()

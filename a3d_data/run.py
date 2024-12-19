from glob import glob
from pathlib import Path

import cv2
import numpy as np
from PIL import Image
from tqdm import tqdm


def main():
    """Main entry point for the CLI."""

    depth_files = [Path(f) for f in glob("./seathru/**/**/**/*.tif")]
    for depth_file in tqdm(depth_files):
        png_file = (
            depth_file.parent.parent
            / "linearPNG"
            / f"{depth_file.stem[len("depth"):]}.png"
        )
        numpy_file = depth_file.parent / f"{depth_file.stem}"

        png = cv2.imread(png_file)
        height, width, _ = png.shape

        tif_image = Image.open(depth_file)
        tif = np.array(tif_image)
        tif = cv2.resize(tif, (width, height),  interpolation = cv2.INTER_NEAREST)

        np.savez_compressed(numpy_file, depths=tif)


if __name__ == "__main__":
    main()

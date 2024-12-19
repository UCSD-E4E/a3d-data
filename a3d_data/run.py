from glob import glob
from pathlib import Path

import numpy as np
from PIL import Image
from tqdm import tqdm


def main():
    """Main entry point for the CLI."""

    depth_files = [Path(f) for f in glob("./seathru/**/**/**/*.tif")]
    for depth_file in tqdm(depth_files):
        numpy_file = depth_file.parent / f"{depth_file.stem}"

        tif_image = Image.open(depth_file)
        tif = np.array(tif_image)

        np.savez_compressed(numpy_file, depths=tif)


if __name__ == "__main__":
    main()

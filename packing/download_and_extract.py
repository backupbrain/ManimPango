#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import logging
import shutil
import tarfile
import tempfile
import urllib.request
from pathlib import Path

logging.basicConfig(format="%(levelname)s - %(message)s", level=logging.INFO)
parser = argparse.ArgumentParser(description="Download things.")
parser.add_argument("url", help="the url to download")
parser.add_argument("folder", help="folder name to extract")
args = parser.parse_args()

with tempfile.TemporaryDirectory() as tmpdirname:
    fname = Path(tmpdirname, Path(args.url).name)

    logging.info(f"Download & Saving file to {fname}")

    urllib.request.urlretrieve(args.url, fname)

    with tarfile.open(fname, "r") as tar:
        logging.info(f"Extracting {fname} to {tmpdirname}")
        tar.extractall(tmpdirname)

    logging.info(
        f"Moving {Path(tmpdirname, Path(Path(args.url).stem).stem)} "
        f"to {str(args.folder)}"
    )
    shutil.move(
        Path(tmpdirname, Path(Path(args.url).stem).stem),
        str(args.folder),
    )

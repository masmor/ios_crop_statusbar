#!/usr/bin/env python3

import os, sys, tempfile, shutil, subprocess
from PIL import Image


def crop_size(image):
  w, h = image.size
  if h == 960 or h == 1136 or h == 640:
    return 0, 40, w, h
  else:
    return None


def main():
  for infile in sys.argv[1:]:
    name, ext = os.path.splitext(infile)
    image = Image.open(infile)
    size = crop_size(image)
    if (size is None):
      print("skipping " + infile)
      continue

    cropped = image.crop(size)
    temp = tempfile.NamedTemporaryFile(suffix=ext)
    cropped.save(temp)

    shutil.move(infile, name+".orig"+ext)
    subprocess.call(["pngcrush", "-q", temp.name, infile])

    print("cropped " + infile + " to " + str(size))


if __name__ == "__main__":
  main()

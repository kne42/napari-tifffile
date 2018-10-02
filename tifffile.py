from tifffile import imread, imsave

from napari import io


SUPPORTED_EXTENSIONS = ['.tif', '.tiff', '.ome.tif', '.ome.tiff']


io.input(SUPPORTED_EXTENSIONS, imread)
io.output(SUPPORTED_EXTENSIONS, imsave)

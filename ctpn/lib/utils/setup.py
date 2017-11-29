from Cython.Build import cythonize
import numpy as np
from distutils.core import setup

try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()

setup(
    ext_modules=cythonize(["bbox.pyx","cython_nms.pyx"],numpy_include),
)

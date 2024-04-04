# Код для создания .dll с помощью Cython (setup.py)
from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("main.py")
)

from distutils.core import setup, Extension
setup(name = 'myModuleC', version = '1.0',  \
   ext_modules = [Extension('myModuleC', ['modulc_hello.c'])])
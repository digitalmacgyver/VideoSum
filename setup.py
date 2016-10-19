from setuptools import setup

def readme():
    with open( 'README.rst' ) as f:
        return f.read()

setup( name='vedit',
       version='0.1',
       description='Library for editing video by wrapping ffmpeg.',
       long_description=readme(),
       url='https://github.com/digitalmacgyver/vedit',
       author='Matthew Hayward',
       author_email='mjhayward@gmail.com',
       license='MIT',
       packages=['vedit'],
       classifiers=[
           'Development Status :: 3 - Alpha',
           'Environment :: Console',
           'Intended Audience :: Developers',
           'License :: OSI Approved :: MIT License',
           'Topic :: Multimedia :: Video'
       ],
       zip_safe=False )

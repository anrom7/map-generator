import setuptools

with open('README.md', 'r', encoding = 'utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name = 'map-generator-Alina-Voronina',
    version = '0.0.1',
    author = 'Alina Voronina',
    author_email = 'alina.voronina@ucu.edu.ua',
    description = "A paskage to generate a map with 10 closest to user's\
 location film locations.",
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/linvieson/map-generator.git',
    packages = setuptools.find_packages(),
    classifiers = [
        'Programming language :: Python :: 3',
        'License :: OSI Approved :: MIT License', 
        'Operating System :: Windows 10',
    ],
    python_requires = '>=3.8',
)
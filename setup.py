import setuptools
# from importlib_metadata import entry_points

setuptools.setup(
    name="coursetemplater",
    version="0.0.1",
    packages=setuptools.find_packages(),
    install_requires=[
        "mdtemplater"
    ],
    entry_points={
        "console_scripts": [
            "coursetemplater = coursetemplater.coursetemplate:main"
        ]
    }
)

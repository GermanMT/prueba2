import setuptools


setuptools.setup(
    name="prueba1",
    version="0.0.1",
    author="Antonio German Marquez Trujillo",
    author_email="germanoctako@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=[
        'pytest>=4.0.0,<=6.2.5',
        'pytest-httpbin==1.0.0',
        'pytest-mock==2.0.0',
        'Flask>=1.0,<2.0',
    ]
)

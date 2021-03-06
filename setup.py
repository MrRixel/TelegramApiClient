import setuptools

install_requires = ['telepot==12.6']
setuptools.setup(
    name="TelegramApiClient",
    version="0.2",
    author="AmirHo3inF",
    author_email="MrAmirho3inf@gmail.com",
    description="Telepot upgraded version",
    install_requires=install_requires,
    long_description='',
    url="https://github.com/amirho3inf/TelegramApiClient",
    license='MIT',
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3.5",
        "License :: OSI Approved :: MIT License"
    ),
)

from setuptools import setup


def readme():
    with open('README.md') as f:
        README = f.read()
    return README


def get_requirements():
    with open("requirements.txt", encoding="utf8") as f:
        return f.read().splitlines()


setup(
    name="wideryolo",
    version="0.0.5",
    description="Wider-Yolo Kütüphanesi ile Yüz Tespit Uygulamanı Yap",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/kadirnar/",
    author="Kadir Nar",
    author_email="kadir.nar@hotmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9"
    ],
    packages=["wideryolo"],
    include_package_data=True,
    install_requires=get_requirements(),
)

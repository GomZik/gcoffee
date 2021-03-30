from distutils.core import setup

setup(
    name="GCoffee",
    version="0.1",
    description="Simple script to prevent screen lock due to inactivity",
    author="Aliakisiej Homza",
    author_email="aliaksiej.homza@gmail.com",
    packages=["gcoffee"],
    package_data={"gcoffee": ["*.svg"]},
    scripts=["gcoffee/gcoffee"],
    include_package_data=True,
)

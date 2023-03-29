from setuptools import setup

setup(
    name="Hello World",
    version="1",
    entry_points={
        'console_scripts': ['hello-world=hello_world:main'],

        'hello_world.output': ['default=hello_world:default_output'],
    }
)
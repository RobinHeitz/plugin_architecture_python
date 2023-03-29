from setuptools import setup


setup(
    name="hello-world-uppercase-output",
    version="1",
    py_modules=["uppercase_output"],
    entry_points = {
        "hello_world.output": ["uppercase=uppercase_output:hello_world_uppercase_output"]
    },


)
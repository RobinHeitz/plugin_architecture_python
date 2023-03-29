# plugin_architecture_python
Shows an example plugin architecture.
Example is taken from: https://www.youtube.com/watch?v=fY3Y_xPKWNA&ab_channel=anthonywritescode

# Install
Create a virtual environment to install packages:
`python3 -m venv env` 

install the 3 packages locally (in root dir): `pip install -e hello-world` (and also for hello-world-json and hello-world-uppercase-output)

# Use
Each plugin for an outputer should have this entry point: `hello_world.output`
Once every plugin/ package is installed (locally), one just call e.g. `hello-world -outputer json` to choose json as outputer.


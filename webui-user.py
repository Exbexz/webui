import subprocess

# Set the desired values for the environment variables
PYTHON = ""
GIT = ""
VENV_DIR = ""
COMMANDLINE_ARGS = "--skip-torch-cuda-test --precision full --no-half"

# Execute the 'webui.bat' file
subprocess.call("webui.bat", shell=True)

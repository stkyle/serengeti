
#!/bin/bash

# create a new virtual environment
virtualenv serengeti
source serengeti/bin/activate

# Install Package Requirements
pip install django
pip install djangorestframework
pip install pygments  


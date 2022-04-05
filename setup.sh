#!/bin/bash

conda update -n base -c defaults conda
source $(conda info --base)/etc/profile.d/conda.sh
conda create -n webapp
conda activate webapp
conda install pip
python -m pip install pyqtwebengine
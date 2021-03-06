"""
Relevant constants and configurations
"""
import os
import matplotlib.style
import matplotlib as mpl
from .utils import configure_logger

os.environ['KERAS_BACKEND'] = 'tensorflow'

# Configure paths
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(os.path.dirname(__file__), "data"))
RESULTS_DIR = os.environ.get("RESULTS_DIR", os.path.join(os.path.dirname(__file__), "results"))

# FIXME: Disable eager in TF (for Tensorboard implementation we are using)
import tensorflow as tf
if tf.__version__[0] == "2":
    tf.compat.v1.disable_eager_execution()
    
import cv2
cv2.setNumThreads(0) # turn off problematic cv2 multithreading
    
# Workaround for absl.logging issue
import sys

if 'absl.logging' in sys.modules:
    import absl.logging

    absl.logging.set_verbosity('info')
    absl.logging.set_stderrthreshold('info')
    
# Configure logger
configure_logger('')

# Some useful plotting styles
mpl.style.use('seaborn-colorblind')
mpl.rcParams.update({'font.size': 14, 'lines.linewidth': 2, 'figure.figsize': (6, 6/1.61)})
mpl.rcParams['grid.color'] = 'k'
mpl.rcParams['grid.linestyle'] = ':'
mpl.rcParams['grid.linewidth'] = 0.5
mpl.rcParams['lines.markersize'] = 6
mpl.rcParams['lines.marker'] = None
mpl.rcParams['axes.grid'] = True
DEFAULT_FONTSIZE = 13
mpl.rcParams.update({'font.size': DEFAULT_FONTSIZE, 'lines.linewidth': 2,
                     'legend.fontsize': DEFAULT_FONTSIZE, 'axes.labelsize': DEFAULT_FONTSIZE,
                     'xtick.labelsize': DEFAULT_FONTSIZE, 'ytick.labelsize': DEFAULT_FONTSIZE,
                     'figure.figsize': (7, 7.0/1.4)})

import inspect
import librosa
import numpy as np 
import os 
import pickle
import random 
import sklearn 
import sklearn.cluster

from pathlib import Path
from typing import List, Dict, Union
from utils.logger_setup import logger

def read_config(path : str) -> Dict:
    """ Load configuration files from path. 

    Parameters
    ------------

    Returns
    --------

    """
    with open(path, 'r') as confile:
        config = yaml.safe_load(confile)
    return config


def list_files(path : str, extension : str) -> List:
    """ List files with proper extensions. 

    Parameters
    -----------


    Returns
    --------

    """

    _files = list(Path(path).rglob(f"*{extension}"))
    assert len(_files) > 0, 'Number of files should be greater than 0'
    return _files

def concat_iters(_iter : np.ndarray) -> np.ndarray:
    _tmp = _iter.reshape(-1)
    return _tmp


def training_decor(func):
    """ Decorator for training procedure.

    Parameters 
    -----------
        func (method)

    Returns
    --------
        wrapper object

    """
    def wrapper(self, *args, **kwargs):
        logger.info("Trainin process started")
        try: 
            func(self, *args, **kwargs)
        except Exception as _error:
            logger.critical(_error, exc_info = True)
    return wrapper


def exception_handler(func):
    """ Extend logger information if any exception appears

    Parameters
    -----------
    func : class.method

    Returns
    --------
    wrapper : object
    """
    def wrapper(self, *args, **kwargs):
        try:
            func(self, *args, **kwargs)
        except Exception as exc:
            logger.critical(exc, exc_info = True)
    return wrapper

def load_data(path : str) -> np.array:
    assert os.path.exists(path), 'Provided path does not exist'
    with open(path, 'rb') as file:
        _data = pickle.load(file)
    return _data

def initialize_colors(n_cols : int) -> List:
    """ Create list with random colors 
        which length is equal to n_cols value. 

    Parameters 
    -----------
    n_cols : int
        Number of colors to produce.

    Returns 
    --------
    List
        List of length n_cols which is filled with tuples of shape (3,)
    """
    _colors = tuple(np.random.choice(range(256), size = 3) for el in range(n_cols))
    return _colors

def sort_values_dict(_dict : Dict) -> Dict:
    """ Sort dictionary by its values. 

    Parameters 
    ------------
    _dict : Dict 
        Dictionary 

    Returns 
    --------
    dict
    """
    return sorted(_dict.items(), key = lambda item : item[1], reverse = True)

def perc_values(_dict : Dict) -> Dict:
    """ Dictionary with percentage of values. 

    Parameters 
    -----------
    _dict : Dict 
        Dictionary 

    Returns 
    ---------
    dict
    """

    return {k : v/len(_dict.values()) for k, v in dict.items()}


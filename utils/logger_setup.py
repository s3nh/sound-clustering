import logging 
import os

os.makedirs('log', exist_ok=True)
logging.basicConfig((filename = 'log/clusterlog.log'))
logger = logging.getLogger('')
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
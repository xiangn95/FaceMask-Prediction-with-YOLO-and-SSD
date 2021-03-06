

import cv2
import os
import numpy as np
import argparse
#from matplotlib import pyplot as plt
#import plotly.express as px
#import plotly.graph_objects as go

from six.moves import urllib
import requests
from pdb import set_trace
import glob




# FILE_ID = "1QspxOJMDf_rAWVV7AU_Nc0rjo1_EPEDW"
# DESTINATION = '../face_mask_detection.zip'
SOURCE_URL = "https://cloud.tsinghua.edu.cn/f/a3d6633e74744db0a507/?dl=1"

def maybe_download(filename, work_directory):
	"""Download the data from website, unless it's already here."""
	if not os.path.exists(work_directory):
		os.makedirs(work_directory)
	filepath = os.path.join(work_directory, filename)
	
	if not os.path.exists(filepath):
		print("start downloading model...")
		filepath, _ = urllib.request.urlretrieve(SOURCE_URL, filepath)
		# filepath = download_file_from_google_drive(FILE_ID, filepath)
	with open(filepath, "r") as f:
		print('Successfully downloaded', filename)
	return filepath



if __name__=="__main__":
	parser = argparse.ArgumentParser(description="FaceMaskDetection")
	
	parser.add_argument('--dest', type=str, default="./", help='path to dataset.')
	args = parser.parse_args()
	maybe_download("checkpoint_ssd300.pth.tar", args.dest)
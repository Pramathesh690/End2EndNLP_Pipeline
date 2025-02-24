from hate.logger import logging
from hate.exception import CustomException
import sys
from hate.configuration.gcloud_syncer import GCloudSync
#logging.info("Welcome to our project")


obj = GCloudSync()

obj.sync_folder_from_gcloud("hate-speechnlp","dataset.zip","download/dataset.zip")
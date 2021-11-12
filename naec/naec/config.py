import os

CUR_PATH = os.getcwd()
DATA_PATH_PREFIX = CUR_PATH.replace("naec/naec", "data") + "/AEC-Challenge/datasets/"
DATA_PATHS = [DATA_PATH_PREFIX + "test_set", DATA_PATH_PREFIX + "test_set_interspeech2021"]
# All rights reserved. 
#  
# Released under the BSD 3-Clause license as published at the link below.
# https://openwsn.atlassian.net/wiki/display/OW/License

import traceback
import time
import json
import os

log_file_path = "..\\..\\"

files = os.listdir(log_file_path)

for file in files:
    if file.startswith("eventLog_"):
        with open(log_file_path+file, 'r') as f:
            for line in f:
                data_entry = json.loads(line)
                for k,v in data_entry.items():
                    if len(v[0]['data']) > 0:
                        for k_data,v_data in v[0]['data'][0].items():
                            print k_data, v_data
                            raw_input()
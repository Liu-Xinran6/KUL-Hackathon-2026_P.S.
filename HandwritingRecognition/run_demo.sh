#!/bin/bash

# 1. load Python 
module load Python/3.11.5-GCCcore-13.2.0

# 2. activate virtual environment
source /scratch/leuven/387/vsc38790/hack_env/bin/activate

# 3. enter
cd /data/leuven/387/vsc38790/

# 4. activate the web
streamlit run app.py --server.enableCORS false --server.enableXsrfProtection false
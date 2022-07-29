# This is a boilerplate template for spark apps

## the goal of this repo is to provide a guideline on how to build a pyspark code base

submitting a pyspark job 
*  ```spark-submit --py-files pyfile.py,zipfile.zip main.py --arg1 val1```

zip files can be treated as ny directory (import modules and functions from zip) as long we add the zip file to seach path 
```
import sys
sys.path.insert(0, jobs.zip)
``` 
assuming that `jobs.zip` contains a python module called jobs we can import that module and whatever it contains 

```
from jobs.wordcount import run_job
run_job()
```

```
├── Makefile
├── README.md
├── requirements.txt
├── src
│   ├── jobs
│   │   ├── __init__.py
│   │   └── wordcount
│   │       └── __init__.py
│   ├── main.py
│   └── shared
└── test
```

- when we submitt a job to spark we wnat to submit main.py as our job file and the rest of the code as --py-files extra(jobs.zip)
  so we use the Makefile to add the build command 
  ```
  build:
    mkdir ./dist
    cp ./src/main.py ./dist
    cd ./src && zip -x main.py -r ../dist/jobs.zip .
  ```
  and submit the job as folows 
  ```
  make build
  cd dist && spark-submit --py-files jobs.zip main.py --job wordcount
  ```

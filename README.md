# Avedian-EDL-Examples

## Requirements:
- Python 3
- Avedian EDL Credentials
- Avedian AWS Credentials

## Steps EDL-Trino
```
cd EDL-Trino
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 Example-DBAPI.py
```
## Steps EDL-S3
```
cd EDL-S3
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
python3 Example-Upload-S3.py
```
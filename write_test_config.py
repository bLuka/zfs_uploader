import configparser
import os

config = configparser.ConfigParser()

config['DEFAULT'] = {
    'bucket': 'z3-test',
    'region': 'us-east-2',
    'access_key': os.environ['AWS_ACCESS_KEY_ID'],
    'secret_key': os.environ['AWS_SECRET_ACCESS_KEY'],
    'storage_class': 'STANDARD'
}
config['test-pool/test-filesystem'] = {
    'cron': '* * * * *',
    'max_snapshots': 3,
    'max_incremental_backups': 5
}

with open('config.cfg', 'w') as f:
    config.write(f)

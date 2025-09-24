import logging
import yaml
import os

def load_config():
    try:
        with open('config.yaml','r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Error loading config : {e}")
        return {
            'logging':{
                'level':'INFO',
                'file':'logs/app.log'
            }
        }
    
config=load_config()

log_file=config['logging'].get('file','logs/app.log')
os.makedirs(os.path.dirname(log_file),exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=getattr(logging,config['logging'].get('level','INFO')),
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logger=logging.getLogger(__name__)

console_handler = logging.StreamHandler()
console_handler.setLevel(getattr(logging,config['logging'].get('level','INFO')))
formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.WARNING)

logging.getLogger('flake8').setLevel(logging.WARNING)
logging.getLogger('docker').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)

pytest_plugins = ['pytester']

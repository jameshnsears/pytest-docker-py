import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d  %(levelname)8s --- [%(process)5d] %(filename)25s:%(funcName)30s, %(lineno)3s: %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S',
    level=logging.DEBUG)

logging.getLogger('docker').setLevel(logging.WARNING)
logging.getLogger('urllib3').setLevel(logging.WARNING)

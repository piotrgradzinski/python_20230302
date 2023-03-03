import logging

logging.basicConfig(level=logging.DEBUG)

logging.debug('debug')
logging.info('info')
logging.warning('warning')
logging.error('error')
logging.log(logging.ERROR, 'error')
logging.critical('critical')

my_logger = logging.getLogger(__name__)

# Handlers
console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file.log')

# możemy określić, które logi nas interesują
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.WARNING)

# dopinam formatter
console_formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(pathname)s|%(lineno)d|%(message)s')
console_handler.setFormatter(console_formatter)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)


# dopinam handler do mojego loggera
my_logger.addHandler(console_handler)
my_logger.addHandler(file_handler)

my_logger.debug('my_logger debug')
my_logger.info('my_logger info')
my_logger.warning('my_logger warning')
my_logger.error('my_logger error')
my_logger.critical('my_logger critical')

# unikamy robienia f-stringa, tylko korzystamy z notacji:
my_logger.error('my_logger error, %s', [1, 2, 3])

# wyjątki...
try:
    my_list = [1, 2, 3]
    print(my_list[10])
except IndexError as e:
    my_logger.error('Missing key, %s', e, exc_info=True)

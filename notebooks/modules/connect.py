import pysftp
from loguru import logger
import time


def main():
    try:
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None
        with pysftp.Connection("157.230.104.127",
                               username="root",
                               password="3VTWNY4J",
                               cnopts = cnopts
                               ) as sftp:
            sftp.get('/root/events/events.csv', 'events.csv')


        sftp.close()
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    while True:
        main()
        time.sleep(600)


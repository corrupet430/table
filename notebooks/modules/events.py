import requests
from loguru import logger
import time

key = 'b5de5cac35e1a3020cff4b8866aeeff5'
local_events_time = None


def base():
    try:
        global local_events_time
        with requests.Session() as s:
            download = s.get('https://offvariance.com/api/public/csv/events/finished/', params={'key': key}, verify=False)
            if local_events_time != download.headers['Last-Modified']:
                logger.info('Download update')
                local_events_time = download.headers['Last-Modified']
                decoded_content = download.content.decode('utf-8')

                with open('events.csv', 'w', encoding="utf-8") as temp_file:
                    temp_file.writelines(decoded_content)

    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    while True:
        base()
        time.sleep(1800)
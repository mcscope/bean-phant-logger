#!/usr/bin/env python

import config

import time
from datetime import datetime
import pytz
import serial
logging_begin =  datetime.now(pytz.utc)
print_timing = False

bean = serial.Serial(config.BEAN_SERIAL_PATH,
                     timeout=config.BEAN_REQ_TIMEOUT_SECS)
last_run = None
delays = []

def log_data(data_to_log):

    print str(data_to_log)

def read_n_log(bean_serial):
    bean.write(b'\n')
    raw_data = bean.readline()
    data = raw_data.decode('utf-8').rstrip('\r\n')

    if len(data) == 0:
        print 'Bean timed out.\n'
        return False

    data_split = data.split('\t')
    if len(data_split) < len(config.DATA_FIELDS):
        print 'Expected %s fields, but only received %s from Bean.' % \
              (len(config.DATA_FIELDS), len(data_split))
        return False

    labeled_data = dict(zip(config.DATA_FIELDS, data_split))
    labeled_data['time'] = (datetime.now(pytz.utc) - logging_begin).total_seconds()

    log_data(labeled_data)
    return True


while True:
    now = datetime.now(pytz.utc)

    if last_run:
        since_last_run = (now - last_run).total_seconds()
        delays.append(since_last_run)

    if delays and len(delays) % 10 == 0 and print_timing:  # log average delay, for troubleshooting
        print sum(delays)/len(delays)

    if not last_run or since_last_run >= config.INTERVAL_SECS:
        success = read_n_log(bean)
        if success:
            last_run = now

    else:
        until_next_run = config.INTERVAL_SECS - since_last_run
        print "TRIED TO READ FASTER THAN INTERVAL -- MUST SLEEP"
        time.sleep(until_next_run)

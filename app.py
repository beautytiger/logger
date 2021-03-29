#!/usr/bin/env python
import logging
import sys
import os
import uuid
import time
import signal

def main():
    uid = uuid.uuid1().hex
    logger = logging.getLogger(__name__)
    
    logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s,%(msecs)03d %(process)d %(filename)s %(lineno)d %(name)s %(levelname)s %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[
        logging.StreamHandler()
    ])

    line_total = os.getenv("LINE_TOTAL")
    if not line_total:
        line_total = 10**7
    else:
        line_total = int(line_total)

    line_per_second = os.getenv("LINE_PER_SECOND")
    if not line_per_second:
        line_per_second = 1000
    else:
        line_per_second = int(line_per_second)

    no_sleep = os.getenv("INSECURE_SELFTESTONLY_NO_SLEEP")
    if no_sleep == 'true':
        for i in range(1, line_total+1):
            logger.info("%s %032d" % (uid, i))
    else:
        if line_per_second >= 1000:
            sleep_time = 0.05 / line_per_second
        elif line_per_second >= 100:
            sleep_time = 1.0 / line_per_second
        elif line_per_second >= 10:
            sleep_time = 1.0 / line_per_second
        else:
            sleep_time = 0.97
        for i in range(1, line_total+1):
            time.sleep(sleep_time)
            logger.info("%s %032d" % (uid, i))

    logger.info("%s %s" % (uid, "alldone"))

    while True:
        time.sleep(1)


def do_exit(sig, stack):
    sys.exit(0)

signal.signal(signal.SIGINT, do_exit)
signal.signal(signal.SIGTERM, do_exit)

if __name__ == "__main__":
   main()

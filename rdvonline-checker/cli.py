import logging
import time
import sys
import click
import schedule

import rdvonline_web

logger = logging.getLogger(__name__)


@click.group()
def cli():
    # Configure logger for all sub commands
    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('[%(name)s %(asctime)s]%(levelname)s: %(message)s')
    handler.setFormatter(formatter)
    logging.root.addHandler(handler)
    logging.root.setLevel(logging.INFO)


@click.command()
def rdvonline():
    # Schedule the command to rerun every 60 seconds
    schedule.every(4).seconds.do(rdvonline_web.check_available_date)
    while True:
        schedule.run_pending()
        time.sleep(2)


cli.add_command(rdvonline)

if __name__ == '__main__':
    rdvonline_web.check_available_date()

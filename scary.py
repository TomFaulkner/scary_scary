import os

from datetime import datetime
from glob import glob
from random import choice, randint
from time import sleep


def play(sleep_time):
    files = glob('sounds/*')
    file = choice(files)
    print(f'Running {file}. Next sound in {sleep_time} seconds.')
    sleep(sleep_time)
    os.system(f"mpg123 '{file}'")


if __name__ == '__main__':
    now = datetime.now()
    print(f"Called at {now}")
    if 8 <= now.hour <= 19:
        sleep_time = randint(1, 74)
        play(sleep_time)

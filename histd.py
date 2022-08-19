#!/usr/bin/env python3
from datetime import date
import os
import subprocess


def main():
    base_dir = get_base_dir()
    today = date.today()
    edit_note(base_dir, today)


def get_base_dir() -> str:
    """
    Creates the directories necessary for the program
    to work, if they are not present.

    Returns the path to the directory where data can be stored.
    """
    local_dir = os.path.expanduser('~/.local')
    if not os.path.exists(local_dir):
        os.mkdir(local_dir)

    histd_dir = os.path.join(local_dir, 'histd')
    if not os.path.exists(histd_dir):
        os.mkdir(histd_dir)

    return histd_dir


def edit_note(base_dir: str, note_date: date):
    """
    Creates the required directories and opens a text editor
    so that the user can describe the day.
    """
    # Create dirs (base_dir/year/month)
    year_dir = os.path.join(base_dir, str(note_date.year))
    if not os.path.exists(year_dir):
        os.mkdir(year_dir)

    month_dir = os.path.join(year_dir, f'{note_date.month:02}')
    if not os.path.exists(month_dir):
        os.mkdir(month_dir)

    # Open file (base_dir/year/month/day.txt) with default editor
    path_to_file = os.path.join(month_dir, f'{note_date.day:02}.txt')
    editor = os.environ.get('EDITOR', 'nano')
    subprocess.run([editor, path_to_file])


if __name__ == '__main__':
    main()

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
    base_dir = os.path.expanduser('~/.local/share/histd')
    os.makedirs(base_dir, exist_ok=True)
    return base_dir


def edit_note(base_dir: str, note_date: date):
    """
    Creates the required directories and opens a text editor
    so that the user can describe the day.
    """
    # Create dirs (base_dir/year/month)
    year = str(note_date.year)
    month = f'{note_date.month:02}'
    workdir = os.path.join(base_dir, year, month)
    os.makedirs(workdir, exist_ok=True)

    # Open file (base_dir/year/month/day.md) with default editor
    filename = f'{note_date.day:02}.md'
    path_to_file = os.path.join(workdir, filename)
    editor = os.environ.get('EDITOR', 'nano')
    try:
        subprocess.run([editor, path_to_file], check=True, cwd=base_dir)
    except FileNotFoundError:
        print("Error: I can't find your text editor")
        print("Make sure the 'EDITOR' environment variable is set correctly")
    except subprocess.CalledProcessError:
        print("Your editor returned non-zero exit code")


if __name__ == '__main__':
    main()

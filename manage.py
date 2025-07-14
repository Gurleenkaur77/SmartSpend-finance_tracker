#!/usr/bin/env python
"""Entry point for Django admin tasks like runserver, migrate, etc."""

import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'smart_spend.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Django isn't installed or the virtual environment isn't activated."
        ) from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

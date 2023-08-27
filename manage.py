#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ProjectPlanner.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

""" 
{
    "id": "9",
    "name": "John Washington",
    "username": "John",
    "userdescription": "Junior Developer"
}

            {
                "Teamname": "IT Operations Team",
                "description": "Developing the IT Infrastructure",
                "members": "9","10","11",
                "admin": 2
            }
"""

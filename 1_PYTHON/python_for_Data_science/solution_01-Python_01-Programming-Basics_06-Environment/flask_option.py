# pylint: disable=missing-docstring

import os

def start():
    """returns the right message"""
    # $CHALLENGIFY_BEGIN
    env = os.getenv(key = 'FLASK_ENV', default="empty")

    return f"Starting in {env} mode..."
    # $CHALLENGIFY_END

if __name__ == "__main__":
    print(start())

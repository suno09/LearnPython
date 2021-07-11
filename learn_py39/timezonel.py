from datetime import datetime, timezone
from zoneinfo import ZoneInfo


if __name__ == '__main__':
    print(datetime.now(tz=timezone.utc))
    '''
    when you find ZoneInfoNotFoundError: 'No time zone found with key America/Vancouver'
    execute: python -m pip install tzdata
    '''
    print(ZoneInfo("America/Vancouver"))

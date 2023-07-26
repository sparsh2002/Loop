import pytz
from datetime import datetime

def convert_time_to_utc(time_str, timezone):
    time_format = "%H:%M:%S"
    dt_str = f"1970-01-01 {time_str}"  # Use any arbitrary date since we are only interested in time
    dt = datetime.strptime(dt_str, f"%Y-%m-%d {time_format}")

    tz = pytz.timezone(timezone)
    dt_with_timezone = tz.localize(dt)
    dt_utc = dt_with_timezone.astimezone(pytz.utc)

    return dt_utc.time()

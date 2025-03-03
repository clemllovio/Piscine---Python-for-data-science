from datetime import datetime

dt = datetime.today()
seconds = datetime.timestamp(dt)
scientific_format = "{:e}".format(seconds)
date_str = dt.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", seconds, "or", scientific_format, "in scientific format")
print(date_str)

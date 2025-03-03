from datetime import datetime

dt = datetime.today()

seconds = datetime.timestamp(dt)
formated_seconds = f"{seconds:,.4f}"

scientific_format = "{:.2e}".format(seconds)

date_str = dt.strftime("%b %d %Y")

print("Seconds since January 1, 1970:", formated_seconds, "or", scientific_format, "in scientific format")
print(date_str)

import time
from datetime import datetime

seconds_since_epoch = time.time()

seconds_formatted = f"{seconds_since_epoch:,.4f} or {seconds_since_epoch:.2e} \
    in scientific notation"

current_date = datetime.now().strftime("%b %d %Y")

print(f"Seconds since January 1, 1970: {seconds_formatted}")
print(current_date)

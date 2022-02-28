from datetime import datetime

now = datetime.now()

print(f'with ms: {now}')

now = now.replace(microsecond = 0)

print(f'without ms: {now}')
 
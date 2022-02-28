from datetime import datetime, timedelta

now = datetime.now() 

print(f'today: {now.strftime("%d %B %Y")}')

fiveDaysAgo = now - timedelta(days = 5) 

print(f'5 days ago: {fiveDaysAgo.strftime("%d %B %Y")}')




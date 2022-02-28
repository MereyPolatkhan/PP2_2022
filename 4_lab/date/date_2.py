from datetime import datetime, timedelta

today = datetime.today() 

yesterday = today - timedelta(days = 1)

tomorrow = today + timedelta(days = 1) 

print(yesterday.strftime("%A"))

print(f'yesterday = {yesterday.strftime("%d %B %Y | day: %A")}')
print(f'today = {today.strftime("%d %B %Y | day: %A")}')
print(f'tomorrow = {tomorrow.strftime("%d %B %Y | day: %A")}')
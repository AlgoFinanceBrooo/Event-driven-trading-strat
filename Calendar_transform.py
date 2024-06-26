import pandas as pd
import re

us_calendar = pd.read_csv('us_calendar.csv')



#drop change/change_percent/importance/currency from us_calendar

drop_col = ['change','change_percent','importance','currency','country']

us_calendar.drop(columns = drop_col, inplace= True)

#remove sub
def remove_months(event):
    return re.sub(r'\((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Q1|Q2|Q3|Q4)\)', '', event)

# Applying the function to the 'event' column
us_calendar['event'] = us_calendar['event'].apply(remove_months)

### Always print head and tail at the end

us_calendar.shape

print(us_calendar.head(10))
print(us_calendar.tail(10))

us_calendar.to_csv('trade_calendar_us', sep=',', encoding='utf-8', index= True)
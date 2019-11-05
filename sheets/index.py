import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('Spreedsheet-68e3c62d39c1.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open('DADOS').sheet1

df = pd.DataFrame(wks.get_all_records())
print(df)
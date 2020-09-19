import gspread
from oauth2client.service_account import ServiceAccountCredentials

def getSpreadsheet():
   scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
   creds = ServiceAccountCredentials.from_json_keyfile_name('movie-picker-278421-5db6a26eccea.json', scope)
   client = gspread.authorize(creds)
   sheet = client.open('SM Movie List').sheet1
   return sheet.get_all_records()

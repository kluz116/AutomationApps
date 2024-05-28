import pyodbc

try:
    conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.255.201.179,1629;DATABASE=FTBTEST2023;UID=realm;PWD=friend;TDS_Version=8.0;MARS_Connection=Yes;')

except Exception as e:
    print(f'What is the crap error {e}')



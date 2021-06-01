import sqlite3
import pandas as pd
# from pandas import DataFrame
#
conn = sqlite3.connect('WindowsAppSDB.db')
c = conn.cursor()

read_clients = pd.read_csv(r'C:\Users\QuickboostTest\Documents\RajareddyV\microsoft_store_apps\Combine_Excel_sheets\All_Categories_windowsApps.csv',encoding='latin-1')
read_clients.to_sql('WINDOWS_Apps_Store', conn, if_exists='append',index=False)  # Insert the values from the csv file into the table 'CLIENTS'
# print(read_clients)
# c.execute('''
# INSERT INTO WINDOWS_Apps_Store (web-scraper-order,web-scraper-start-url,Pagination,Pagin[ation-href,App link,App link-href,App_Name,Company Name,App Type,Wish list,NumberOfUserRateTheApp,FreeorPaid,ShortDescriptions,UsersInterect,AvailableOn,Descriptions,AdditionalInfo,Permissions,PublishedBy,ReleaseDate,Category,App Size,ReviewLink,ReviewLink-href,OverAllReview,ReviewDetails,Five,Four,Three,Two,One,Users_Comments)
# ''')

# df = DataFrame(c.fetchall(), columns=['web-scraper-order' , 'web-scraper-start-url' , 'Pagination' , 'Pagination-href' , 'App link' , 'App link-href' , 'App_Name' , 'Company Name' , 'App Type' , 'Wish list' , 'NumberOfUserRateTheApp' , 'FreeorPaid' , 'ShortDescriptions' , 'UsersInterect' , 'AvailableOn' , 'Descriptions' , 'AdditionalInfo' , 'Permissions' , 'PublishedBy' , 'ReleaseDate' , 'Category' , 'App Size' , 'ReviewLink' , 'ReviewLink-href' , 'OverAllReview' , 'ReviewDetails' , 'Five' , 'Four' , 'Three' , 'Two' , 'One' , 'Users_Comments'])
# print(df)  # To display the results after an insert query, you'll need to add this type of syntax above: 'c.execute(''' SELECT * from latest table ''')

# df.to_sql('DAILY_STATUS', conn, if_exists='append',index=False)  # Insert the values from the INSERT QUERY into the table 'DAILY_STATUS'

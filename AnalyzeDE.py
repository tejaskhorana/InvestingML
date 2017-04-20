import pandas as pd
import os
import time
from datetime import datetime

path="res/intraQuarter"

#data we are trying to 'gather'
def Key_Stats(gather="Total Debt/Equity (mrq)"):
	statspath = path+"/_KeyStats"
	#gathers just the name of each the folder for entire directory

	stock_list = [x[0] for x in os.walk(statspath)]
	#print(stock_list)

	df = pd.DataFrame(columns=['Date','Unix','Ticker','DE Ratio','Price','SP500'])

	sp500_df = pd.DataFrame.from_csv("res/snp500.csv")


	#start at one because we don't want root directory
	for each_dir in stock_list[1:25]:
		each_file = os.listdir(each_dir)

		#define stock ticker
		ticker = each_dir.split("_KeyStats/")[1]
		if len(each_file) > 0:
			for aFile in each_file:
				date_stamp = datetime.strptime(aFile, '%Y%m%d%H%M%S.html')
				unix_time = time.mktime(date_stamp.timetuple())
				#print(str(date_stamp), str(unix_time))
				full_file_path = each_dir+'/'+aFile
				#print(full_file_path)
				sourceCode = open(full_file_path,'r').read()
				#print(sourceCode)
				#parse table to get data that we need
				value = 0.0
				try:	
					#should hit exception as float and will thus pass over i.e. N/A
				    value = float(sourceCode.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0])

				    try:
				    	sp500_date = datetime.fromtimestamp(unix_time).strftime('%Y-%m-%d')
				    	row = sp500_df[(sp500_df.index == sp500_date)]
				    	sp500_value = float(row["Adj Close"])
				    except:
				    	sp500_date = datetime.fromtimestamp(unix_time-259200).strftime('%Y-%m-%d')
				    	row = sp500_df[(sp500_df.index == sp500_date)]
				    	sp500_value = float(row["Adj Close"])

				    stock_price = float(sourceCode.split('</small><big><b>')[1].split('</b></big>')[0])


				    df = df.append({'Date':date_stamp,
				    				'Unix':unix_time,
				    				'Ticker':ticker,
				    				'DE Ratio':value,
				    				'Price':stock_price,
				    				'SP500':sp500_value,
				    				}, ignore_index = True)
				except Exception as e:
				    pass

	save = gather.replace(' ', '').replace(')','').replace('(','').replace('/','')+str('.csv')
	print(save)
	df.to_csv(save)

				#print(str(date_stamp))
				#print(str(unix_time))
				#time.sleep(1)
		#print(each_file)
		#time.sleep(10)


Key_Stats()
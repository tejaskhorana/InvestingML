import pandas as pd
import os
import time
from datetime import datetime

path="res/intraQuarter"

def Key_Stats(gather="Total Debt/Equity (mrq)"):
	statspath = path+"/_KeyStats"
	#gathers just the name of the folder
	stock_list = [x[0] for x in os.walk(statspath)]
	#print(stock_list)



	#start at one because we don't want root directory
	for each_dir in stock_list[1:]:
		each_file = os.listdir(each_dir)
		print str(each_dir)
		#define stock ticker
		ticker = each_dir.split("_KeyStats/")[1]
		if len(each_file) > 0:
			for aFile in each_file:
				date_stamp = datetime.strptime(aFile, '%Y%m%d%H%M%S.html')
				unix_time = time.mktime(date_stamp.timetuple())
				full_file_path = each_dir+'/'+aFile
				print(full_file_path)
				sourceCode = open(full_file_path,'r').read()
				#print(sourceCode)
				#parse table to get data that we need
				value = sourceCode.split(gather+':</td><td class="yfnc_tabledata1">')[1].split('</td>')[0]
				print(ticker)
				print(value)



				#print(str(date_stamp))
				#print(str(unix_time))
				time.sleep(1)
		#print(each_file)
		#time.sleep(10)


Key_Stats()
import pandas as pd
'''data=pd.read_csv(r"C:\\Users\nive_\Desktop\sample\sample.csv")

print(data) #only show 1st 5 and last 5 values to show

print(data.to_string()) #whole dataset show

pd.options.display.max_rows = 9999 #Max_rows settings
print(pd.options.display.max_rows) #print max_rows'''



data = pd.read_json(r"C:\\Users\nive_\Desktop\sample\iris.json")
#print(data.to_string())

#print(data.head(10))

#print(data.tail(10))

#print(data.info())









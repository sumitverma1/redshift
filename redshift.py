import re
import numpy as np
import pandas

file1=open('nr.txt')

file2=file1.readlines()

result1 = [k for k in file2 if '--' not in k]

result2 = [k for k in result1 if '\\' not in k]

result3=re.sub("WITH SYSID\s\d+","",str(result2))

result4=result3.split(",")

result5 = [k for k in result4 if '[' not in k] 
result6 = [k for k in result5 if ']' not in k] 

'''values=[]
for line in result4:
    values.append(line)'''


values = np.asarray(result6)
df1=pandas.DataFrame(values)


print(df1)

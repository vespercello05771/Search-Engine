import math as m
text = "This Python interpreter is in a conda environment, but the environment hasnot been activated.  Libraries may fail to load.  To activate this environmentplease see https://conda.io/activation."
op_list = list()
string = ""
for i in range(len(text)) :
 if text[i] == '.' :
  op_list.append(string)
  string = ""  
 else :
  string+=text[i]

segmentedText = op_list

for v in segmentedText :
    print(v)

def Index_No_Error(data,value):
    try:
        index = data.index(value)
        return index
    except:
        return -1
    
data = ["COol","Stuff"]

if (Index_No_Error(data,"Cool") >= 0):
    print("Exists")
else:
    print("Doesn't")

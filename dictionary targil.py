
dict_names={"dudu":25000,"avi":30000,"idan":76000,"ortal":66000,"gal":120000}
print(dict_names)
summary=dict_names["dudu"]+dict_names["gal"]
print("The summary is:" + str(summary))
print("The summary is: " + str(dict_names["dudu"]+dict_names["gal"]))
#dict_names["yoel"]=summary
#print(dict_names)
dict_names.update({"yoel":summary})
print(dict_names)
print("Number of entries: " + str(len(dict_names)))
print("elkana" in dict_names)

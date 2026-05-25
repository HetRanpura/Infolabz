data=[{"states":["gujarat","rajasthan",{"portion":"west indian"},
                 {"languages":["gujarati","marwadi",["hindi","english"]]}]},
{"codes":{"gujarat":"GJ","rajasthan":"RJ"}},
["7.07 CR","8.5 CR"]]

#print total no. of main keys
print(len(data))
#print name of all main keys
print(data[0].keys(),data[1].keys())
#print GJ
print(data[1]["codes"]["gujarat"])
#print gujarat
print(data[0]["states"][0])
#print marvadi
print(data[0]["states"][3]["languages"][1])
#print english
print(data[0]["states"][3]["languages"][2][1])
#print west indian
print(data[0]["states"][2]["portion"])
#print 7.07 CR
print(data[2][0])

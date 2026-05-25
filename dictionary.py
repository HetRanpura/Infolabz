# data={"person1":100000, "person2":50000, "person3":20000}
# print(data)
#keys
# print(data.keys())
#values
# print(data.values())
#items
# print(data.items())
#value of key
# print(data["person3"])
# print(data["person1"])


# data2={"person1":100000, "person2":[50000,10000,2000], "person3":20000}
# print(data2)

# print(data2["person2"])
# print(data2["person2"][1])


data3={"person1":[{"date":"09 may 2024", "salary":10000},
                  {"date":"09 may 2025", "salary":15000},
                  {"date":"09 may 2026", "salary":20000},],
       "person2":[50000,10000,2000],
       "person3":20000
       }
print(data3)
# 10000
print(data3["person1"][0]["salary"])
# 09 may 2025
print(data3["person1"][1]["date"])
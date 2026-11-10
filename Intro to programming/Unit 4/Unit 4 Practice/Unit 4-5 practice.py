seth_data = {
    "name":"Seth",
    "age": 16,
    "fav_animal": "Wolf",
    "bucket_list": "Snowboard in Switzerland",
    "height": "6 foot 0 inches"
}

print(seth_data["bucket_list"])

seth_data["bucket_list"]= "Do a wheely in a wheelchair"
print(seth_data["bucket_list"])

seth_data["Allergy"]= "Cats"
print(seth_data["Allergy"])

del seth_data["bucket_list"] #Removes a key value pair by key

for key in seth_data:
    print(seth_data[key])



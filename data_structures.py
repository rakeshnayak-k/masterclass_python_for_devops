list_of_cloud = ['AWS','Azure','GCP','Oracle']
list_of_env = ['dev','test','prod']

# print(list_of_cloud)
# print(list_of_cloud[0])
for i in list_of_cloud:
    if i== "AWS":
        print(i,'is the best cloud')

dict_of_cloud = {
    "AWS": "Amazon Web Server",
    "Azure": " Microsoft Azure",
    "GCP": "Google Cloud Platform"
}

print(dict_of_cloud['AWS'])
print(dict_of_cloud.get('GCP'))
print(dict_of_cloud.get('GCPpp','Not found'))

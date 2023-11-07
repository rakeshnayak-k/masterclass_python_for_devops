import boto3

# download aws cli 
#  boto3 is a package used to interact with aws from local
# connct the system with aws account in command line using asses key and secret key created in aws 
# cammand id $ aws confiure

s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')


c = 0 
for buckets in s3.buckets.all():
    print(buckets)
    c = c + =

print('total buckets: ',c)

s3.Bucket("bucket_name").download_file("file_name","rename_file_name")
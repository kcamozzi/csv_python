import requests, zipfile, io

url_list = []

for num in range(1980,2018):
    url_list.append("https://aqs.epa.gov/aqsweb/airdata/hourly_44201_"+str(num)+".zip")

for url in url_list:
    print("Downloading "+str(url))
    dl_url = requests.get(url)
    if dl_url.status_code == 200:
        print("Extracting...")
        z = zipfile.ZipFile(io.BytesIO(dl_url.content))
        z.extractall()
        print("Done!")
    else:
        print("There is no zip for "+str(url))
        print("Skipping...")


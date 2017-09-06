import requests, zipfile, io, glob, pandas

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

print("Finished Downloading")
print("Combining CSV files")

fileList = glob.glob("*.csv")
dfList = []

for filename in fileList:
    print("Adding "+filename)
    df=pandas.read_csv(filename)
    dfList.append(df)

concatDF = pandas.concat(dfList,axis=0)
print("Saving file as 'combined.csv'")

concatDF.to_csv("combined.csv",index=None)
print("Finished!")
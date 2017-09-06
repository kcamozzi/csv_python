import glob, pandas
dfList = []
fileList = glob.glob("*.csv")
df = pandas.DataFrame()
for filename in fileList:
    for chunk in pandas.read_csv(filename, chunksize = 100000, low_memory=False):
        print("Adding "+filename)
        df = pandas.concat([df,chunk])
        dfList.append(df)
concatDF = pandas.concat(dfList,axis=0)
concatDF.to_csv("combined.csv",index=None)
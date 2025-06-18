import pandas

file = input("enter the csv-file's name (please include the .csv): " )

#read the file but only take the relevant columns 👍
csvData = pandas.read_csv(file, usecols=["collectioncode", "catalognumber", "scientificname", "commonname", "datelastmodified", "detectedby", "receiver_group", "station", "receiver", "bottom_depth", "receiver_depth", "tagname", "codespace", "sensortype", "datecollected", "timezone", "longitude", "latitude", "the_geom", "yearcollected", "monthcollected", "daycollected", "timeofday", "local_area", "unqdetecid"])

# sorting the csv data by the individual fish and then by the time collected so we could see each fish's movements in order
csvData.sort_values(["tagname", "datecollected"],
                    axis=0,
                    ascending=[True, True],
                    inplace=True)

#The new processed file will be saved with the same name but with "_processed" added before the .csv extension
csvData.to_csv(file[:-4]+"_processed.csv", index=False)

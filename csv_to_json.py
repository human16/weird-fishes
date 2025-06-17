import pandas

file = input("enter the csv-file's name (please include the .csv): " )

csvData = pandas.read_csv(file)

csvData.sort_values(["tagname", "datecollected"],
                    axis=0,
                    ascending=[True, True],
                    inplace=True)

print(csvData)

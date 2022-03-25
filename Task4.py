# Revision 1 BEGIN/ 24Mar22
## Begin Derek Ruggirello here (24Mar22)

import csv
import json

sales_data = []
csvDict = {"Transaction_date": "", "Product": "", "Price": "", "Payment_Type": "", "Name": "", "City": "", "State": "", "Country": ""}
file = open("SalesJan2009.csv")
csvDict = csv.DictReader(file, fieldnames="Transaction_date" "Product" "Price" "Payment_Type" "Name""City""State" "Country")
jsonFile = open("transaction_data.json", "w")
json.dump(csvDict, jsonFile)
print(jsonFile.read())
file.close()
jsonFile.close()

# Revision 1 FINAL 24Mar22
## End Derek Ruggirello here
# HALF-LIFE/Ron Bass/John Richards Sr./After-Burner Elite #
import xml.etree.ElementTree as ET
import urllib.request

url = 'http://www.cbr.ru/scripts/XML_daily.asp'
response = urllib.request.urlopen(url).read()
tree = ET.fromstring(response)
raw_data_list = []
currency_refined_data = {}
for sub in tree:
    raw_data_list_item = []
    for sub_sub in sub:
        raw_data_list_item.append(sub_sub.text)
    raw_data_list.append(raw_data_list_item)

for item in raw_data_list:
    item[4] = item[4][:-5] + '.' + item[4][-4:]
    currency_refined_data[item[3]] = item[:3] + item[4:]
# print(currency_refined_data['Белорусский рубль'], currency_refined_data['Доллар США'])
# print(float(currency_refined_data['Доллар США'][3]) / float(currency_refined_data['Белорусский рубль'][3]))

# x = {'Австралийский доллар': [('code', '036'), ('abbr', 'AUD'), ('nominal', '1'), ('value', '45,8756')]}

currency_names = []
for key in currency_refined_data.keys():
    currency_names.append(key)

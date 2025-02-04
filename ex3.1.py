import json
from matplotlib import pyplot as plt

with open('internetdata.json', 'r', encoding='UTF-8') as file:
    data = json.load(file)

below10000 = []
above10000 = []

for country in data:
    if country['incomeperperson'] != None:
        if country['incomeperperson'] >= 10000:
            above10000.append(country)
        else:
            below10000.append(country)

belowUse = []
aboveUse = []

for country in below10000:
    if country['internetuserate'] != None:
        belowUse.append(country['internetuserate'])

for country in above10000:
    if country['internetuserate'] != None:
        aboveUse.append(country['internetuserate'])
    
plt.hist(belowUse)
plt.title('Internet Use Rate for Countries with Income Below 10 000')
plt.xlabel('Use Rate (%)')
plt.ylabel('Frequency')
plt.show()

plt.hist(aboveUse)
plt.title('Internet Use Rate for Countries with Income At or Above 10 000')
plt.xlabel('Use Rate (%)')
plt.ylabel('Frequency')
plt.show()
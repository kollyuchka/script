import json

with open("operations.json", "r") as read_file:
    data_1 = json.load(read_file)


def operation(data):
    # sort data by date
    for i in data:
        if "date" in i:
            s = i['date'][0:10]

            i["date"] = s
        else:
            i["date"] = "0"

    data = sorted(data, key=lambda x: (x.get('date')), reverse=True)

    data = data[0:5]

    for i in data:  ## format field "date"
        x = i['date'][8:10] + i['date'][4:8] + i['date'][0:4]
        x = x.replace('-', '.')

        i["date"] = x

    ## formatting fields "to"/"from"
    for i in data:

        if i['to'].find('Счет') != -1 or i['from'].find("Счет") != -1:
            s = i['to'][0:4]
            s1 = i['to'][-4:]
            value = s + " **" + s1
            i['to'] = value
            i['from'] = value

        else:
            s = i['from'][0:-12]
            s1 = i['from'][-16:-12]
            s2 = i['from'][-12: - 10]
            s3 = i['from'][-4:]
            value = s + s1 + " " + s2 + "**" + " ****" + " " + s3
            i['to'] = value
            i['from'] = value

    data_2 = []
    for i in data:
        a = i['date'] + " " + i['description']
        b = i['from'] + " -> " + i["to"]
        c = i['operationAmount']['amount'] + " " + i['operationAmount']['currency']['name']
        data_2.append(a + '\n' + b + '\n' + c)

    return data_2


data = operation(data_1)

for i in data:
    print(i, '\n')

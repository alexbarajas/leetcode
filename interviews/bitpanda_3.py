from json import loads
def sort_by_price_ascending(json_string):
    json = loads(json_string)
    for i in range(1, len(json)):
        currentPrice = json[i]["price"]
        currentPosition = i
        while currentPosition > 0 and json[currentPosition - 1]["price"] > currentPrice:
            json[currentPosition] = json[currentPosition - 1]
            currentPosition = currentPosition - 1
        json[currentPosition] = currentPrice
    return json

print(sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))

# THIS WAS ALL THE WAY WRONG

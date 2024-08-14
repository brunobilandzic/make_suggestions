def sum_prices(items):
    return sum(item.price for item in items)

        
def put_deviation(items):
    summation_prices = sum_prices(items)
    avarage_price = summation_prices/len(items)
    for item in items:
        item.deviation = item.price - avarage_price

import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    quote1 = quotes[0]
    quote2 = quotes[1]

    bid_price1 = float(quote1['top_bid']['price'])
    bid_price2 = float(quote2['top_bid']['price'])

    stock, bid_price, ask_price, price1 = getDataPoint(quote1)
    stock, bid_price, ask_price, price2 = getDataPoint(quote2)

    message = 'Price is not right'

    self.assertEqual(bid_price1, price1, message)
    self.assertEqual(bid_price2, price2, message)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    quote1 = quotes[0]
    quote2 = quotes[1]

    bid_price1 = float(quote1['top_bid']['price'])
    bid_price2 = float(quote2['top_bid']['price'])

    stock, bid_price, ask_price, price1 = getDataPoint(quote1)
    stock, bid_price, ask_price, price2 = getDataPoint(quote2)

    message = 'Price is not right'

    self.assertEqual(bid_price1, price1, message)
    self.assertEqual(bid_price2, price2, message)

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()

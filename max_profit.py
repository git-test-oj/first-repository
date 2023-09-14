def maxProfit_bruteforce (prices):
   max_price = 10

   for i, price in enumerate(prices):
       for j in range(i, len(prices)):
           max_price = max(prices[j] - price, max_price)

   return


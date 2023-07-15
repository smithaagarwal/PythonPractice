"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.



Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
from typing import List
class Solution:
    #Final version o the method, which is both time and memory efficient.
    def maxProfit2(self, prices: List[int]) -> int:
        print("call function with first element ", prices[0])
        #print("length of list",len(prices))

        startPos = 0
        for i, num in enumerate(prices[:-1]):
            if (num < prices[i + 1]):
                #print(num)
                startPos=i
                break
        else:
            return 0
        final_profit = 0
        minPrice = min(prices[startPos:])
        maxPrice = max(prices[startPos:])
        print("minPrice=",minPrice)
        print("maxPrice=", maxPrice)
        print("startPos",startPos)
        minday= prices[startPos:].index(minPrice)
        print("minday",minday)
        maxday = prices[startPos:].index(maxPrice)
        print("maxday", maxday)
        if(maxday<=minday):
            if(minday!=len(prices[startPos:])-1):
                print("len ",len(prices[startPos:]),"minday",minday)
                profit1 = max(prices[startPos+minday + 1:]) - minPrice
                print("profit1:",profit1)
            else:
                print("going recursive ")
                profit1 = self.maxProfit2( prices[startPos+maxday+1:startPos+minday]) if (startPos+maxday+1 < startPos+ minday ) else 0
            if(maxday+startPos!=startPos):
                print("prices[startPos]",prices[startPos],"   ",prices[startPos+maxday])
                profit2 = maxPrice - min(prices[startPos:startPos+maxday])
            else:
                profit2 = self.maxProfit2( prices[startPos+maxday+1:startPos+minday]) if(startPos+maxday+1<startPos+minday) else 0
            print("maxday before minday")
            print("Profit after max day", profit1)
            print("Profit before max day", profit2)
            final_profit = profit1 if (profit1 >= profit2) else profit2
        else:
            final_profit = maxPrice - minPrice
            print("minday before maxday. Profit ",final_profit)
        return final_profit
    #cleaner code than first version but time exceeded for huge inputs
    def maxProfit1(self, prices: List[int]) -> int:
        final_profit = 0
        for index, price in enumerate(prices[:-1]):
            max_price = max(prices[index + 1:len(prices)])
            profit = max_price - price
            if final_profit < profit:
                final_profit = profit
        return final_profit

#first version of the method. these were my first thoughts of the logic without thinking about time and memory. 
    def maxProfit(self, prices: List[int]) -> int:
        day1_min = prices[0]
        day1 = 1
        day2 = len(prices)
        day2_max = prices[-1]
        for index, price in enumerate(prices):
            print(index)
            if day1_min > price and index+1 < day2:
                day1_min = price
                day1 = index+1
                print("Day1 min ", day1_min, "and day is ", day1)

            if day2_max < price and index+1 > day1:
                day2_max = price
                day2 = index
                print("Day2 max ", day2_max, "and day is ", day2)

        if (day2_max - day1_min) < 0:
            return 0
        else:
            return day2_max-day1_min


s = Solution()
#prices=[3,2,6,5,0,3]
#prices = [3,3,5,1,3,1,4,0,5]
#prices=[7,6,2,1,1]
#prices = [7,1,7,1,0,9]

print("profit =",s.maxProfit2(prices))

'''
A group of K  friends want to buy N flowers where each flower i has some base cost, ci . The florist wants to maximize his number of new customers, so he increases the price of flowers purchased by repeat customers; more precisely, if a customer has already purchased  flowers, the price, , for flower  is .

Given , , and the base cost for each flower, find and print the minimum cost for the group to purchase  flowers.

Note: Flowers can be purchased in any order.

n, k
c0 c1 ... cn
input format:
3 3
2 5 6


pi = (n flowers by custumer + 1) * flower cost
https://www.hackerrank.com/challenges/greedy-florist/problem
'''


'''
    Solution
    sort the costs in the decreasing order,
    for each cost, give the first to the customer 1, the second to customer 2 and so on,
    so that each customer buys the most expensive flower first.
    Increment the number of flowers per customer and reset the customer number until
    all flowers were bought. Then, sum all the costs.

'''

#!/bin/python3

import sys

def getMinimumCost(n_flowers, n_customers, costs):
    # array that holds the cost per customer
    customer_cost = [0] * n_customers

    # sort costs by decreasing order
    costs = sorted(costs, reverse=True)

    # amount of flowers each customer has bought
    n_flowers_per_customers = 1

    # customer index
    index = 0

    for cost in costs:
        customer_cost[index] += n_flowers_per_customers * cost
        index += 1

        if index == n_customers:
            # each customer has bought one flower
            n_flowers_per_customers += 1
            index = 0

    return sum(customer_cost)

n_flowers, n_customers = input().strip().split(' ')
n_flowers, n_customers = [int(n_flowers), int(n_customers)]
costs = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n_flowers, n_customers, costs)
print(minimumCost)


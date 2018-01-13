'''
N(#of preliminaty contests) K(maximun number of important contests Lena can loose)
L(uck) T(importance)

Whats the maximum amout of luch she can save?

EX:
6 3
5 1
2 1
1 1
8 1
10 0
5 0

# solution 1
order by most luck
luck       [10,8,5,5,2,1]
importance [0,1,1,0,1,1]

for each of the luck/importance,
add to her luck if it is not important,
it it is important, add only if $looses < k

'''
#!/bin/python3
class Contest:

    def __init__(self, luck, importance):
        self.luck = luck
        self.important = importance == 1

    def __lt__(self, other):
        return self.luck < other.luck

def can_loose(k, looses, contest):
    return looses < k or not contest.important

def luckBalance(contests, k):
    # order by decreasing importance
    contests = sorted(contests, reverse=True)
    # number of importanr contest lost
    looses = 0
    # luck
    luck = 0
    for contest in contests:
        if can_loose(k, looses, contest):
            luck+= contest.luck
            if contest.important:
                looses+= 1
        else:
            #win contest
            luck-= contest.luck
    return luck


if __name__ == "__main__":
    n, k = map(int, input().strip().split(' '))
    contests = []
    for c in range(n):
        luck, importance = map(int, input().strip().split(' '))
        contests.append(Contest(luck, importance))
    print(luckBalance(contests, k))


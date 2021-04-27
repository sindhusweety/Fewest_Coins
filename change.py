"""
Find a minimum number of coins from a list of coins
The Sum of minimum numbers must equal the target value
Used BackTracking technique that explores all the possibilities(solutions)
to choose an optimal solution from all possible solutions

ALGORITHMS' STEPS
create empty result list obj and deep copy the coins to another obj
write base case and sub-function must move toward to base case.
sub-function must have a base case and it must call itself
In sub-function, minus min value (min value found in coins &
min value that closes to target) from target recursively
till it gets the base case.
"""
from copy import deepcopy
class FindMinimumCoins:
    """ Find a minimum number of coins from a list of coins """
    def final_check(self, deepcpy_coins, target, result):
        """
        last option :  2) when a minimum coin less than or equal to target not found
       including all the possibilities,choosing 1
        :param deepcpy_coins:
        :param target:
        :param result:
        :return:
        """
        try:
            #base case
            if target == 0:
                return result
            if target in deepcpy_coins:
                result.append(target)
                return result
            min_ele = find_minimum(deepcpy_coins, target)
            remaing_coin = target - min_ele
            result.append(min_ele)
            self.final_check(deepcpy_coins, remaing_coin, result)

        # raise error if minum coin less than or equal to target not found
        except:
            raise ValueError("Meaningful message indicating the source of the error")

    def min_num_coins(self, coins, target, result, deepcpy_coins):
        """
        Backtracking Technique used here
        :param coins:
        :param target:
        :param result:
        :param deepcpy_coins:
        :return:
        """
        try:
            #base case
            if target == 0:
                return result
            if target in coins:
                result.append(target)
                return result

            #calling sub-sub fun to get the minimum coin from list
            #minimum coin less than or equal to target
            min_ele = find_minimum(coins, target)

            # 1) choosing minimum coins except coin 1
            coins, target, result = check_min_available(coins, target, min_ele, result)

            # 2) when a minimum coin less than or equal to target not found
            #  including all the possibilities,choosing 1
            if min_ele == 1 and min_ele < target and len(coins) == 1 and min_ele in coins:
                self.final_check(deepcpy_coins, target, result)
                return result


            #recursively calling a sub-fun to get the optimal solution
            self.min_num_coins(coins, target, result, deepcpy_coins)

            return result

        except ValueError:
            raise ValueError("Meaningful message indicating the source of the error")


    def find_fewest_coins(self, coins, target):
        """
          find fewest coins
        """
        try:
            #deepcopy coins obj to another obj to avoid overlapping
            deepcpy_coins = deepcopy(coins)

            #creating empty list for adding shortlisted coins
            result = []

            #base case
            if target == 0:
                return result
            if target in coins:
                result.append(target)
                return result

            #call the sub-function which does back tracking technique
            result = self.min_num_coins(coins, target, result, deepcpy_coins)
            #return optimal solution
            return result[::-1]

        #raise error if minum coin less than or equal to target not found
        except ValueError:
            raise ValueError("Meaningful message indicating the source of the error")

def find_minimum(coins, target):
    """
    when a minimum coin less than or equal to target
    :param coins:
    :param target:
    :return:
    """
    for coin in coins[::-1]:
        if coin < target:
            return coin
def check_min_available(coins, target, min_ele, result):
    """
     checking minimum available coins
    :param coins:
    :param target:
    :param min_ele:
    :param result:
    :return:
    """
    try:
        # minimum is not available and target is not deducted either
        if min_ele is None:
            if len(coins) == 1 and target not in coins:
                adj_e = (target + coins[0] + 1) - target
                if adj_e in result:
                    result.remove(adj_e)
                    target = adj_e + target
                    return coins, target, result
            if len(result) >= 1 and result[-1] in coins:
                coins.remove(result[-1])
                target = result[-1] + target
                result.remove(result[-1])
                return coins, target, result

            # raise error if minum coin less than or equal to target not found
            raise ValueError("Meaningful message indicating the source of the error")

        # [1, 5, 10, 21, 25], 63 -> 25,25,10, | minEle=1 | target=2
        # rechecking the possibilities
        # by readding coins to target
        # recursively eleminating last coin to check minimum possibilities
        if min_ele == 1 and min_ele < target:
            if len(result) >= 1:
                coins.remove(result[0])
                target = sum(result) + target
                result.clear()
                return coins, target, result

        # len of coins is 1 after reducing the size and still min coin in coins.
        # it is probably referring coin 1. So we must choose coin at last
        if len(coins) == 1 and min_ele in coins and len(result) == 0:
            target = target + min_ele
            return coins, target, result

        # get remaining value by deducting minimum coin
        # (less than or equal to target coin) from target
        remaing_coin = target - min_ele
        result.append(min_ele)
        return coins, remaing_coin, result

    # raise error if minum coin less than or equal to target not found
    except ValueError:
        raise ValueError("Meaningful message indicating the source of the error")

OBJECT = FindMinimumCoins()
print(OBJECT.find_fewest_coins([1, 5, 10, 21, 25], 63))

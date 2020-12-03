def least_coin(target,coins,known_results):
    print(known_results)
    min_coins=target
    if target in coins:
        known_results[target]=1
        return 1
    elif known_results[target]>0:
        return known_results[target]
    else:
        for i in [c for c in coins if c<=target]:
            num_coins = 1+least_coin(target-i,coins,known_results)
            if num_coins<min_coins:

                min_coins=num_coins
                known_results[target]=min_coins
    return min_coins

target=16
known_results=[0]*(target+1)
coins=[1,2,5,10,25]
print(least_coin(target,coins,known_results))
# 0/1 Knapsack problem

def knapsack(weights, values, max_weight):
    # weights: contains weights of objects
    # values: contains values of objects
    # max_weight: maximum weight/ capacity of weight that can be hold by the knapsack
    
    cache = {} #(n, remaining_weight) -> res

    def dfs(weights, values, remaining_weight, n):
        if n == 0 or remaining_weight == 0:
            return 0
        
        if (n, remaining_weight) in cache:
            return cache[(n, remaining_weight)]
        
        if weights[n-1] > remaining_weight:
            return dfs(weights, values, remaining_weight, n-1)
        
        res =  max(
            values[n-1] + dfs(weights, values, (remaining_weight - weights[n-1]), n-1),
            dfs(weights, values, remaining_weight, n-1),
        )
        # first store result in cache then return it
        cache[(n, remaining_weight)] = res
        return res
    
    n = len(weights)
    return dfs(weights, values, max_weight, n)

if __name__ == "__main__":
    print(knapsack(weights=[1,2,3], values=[10,15,40], max_weight=5))
    print(knapsack(weights=[1,2,3], values=[10,15,40], max_weight=6))
    print(knapsack(weights=[3,4,7], values=[4,5,8], max_weight=7))
    print(knapsack(weights=[3,4,7], values=[4,5,22], max_weight=7))
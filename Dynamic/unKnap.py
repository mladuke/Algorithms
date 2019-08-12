def unboundedKnapsack(maxWeight, numberItems, value, weight):
    totValue = [0]*(maxWeight+1)
    for i in range(maxWeight + 1):
        for j in range(numberItems):
            if (weight[j] <= i):
                totValue[i] = max(
                    totValue[i], totValue[i - weight[j]] + value[j])
        # print(i,totValue[i])
    return totValue[maxWeight]

maxWeight = 10
value = [9, 14, 16, 30]
weight = [2, 3, 4, 6]
numberItems = len(value)
print(unboundedKnapsack(maxWeight, numberItems, value, weight))

from collections import Counter

data = Counter('aksjaskfjsklfjdslkfjajfopewtoieqpwdpqworiiqjskanvmcxbmpewrqopkqwlmdzczmxvmvlnjpjqpkqzxvmbowiqeorewi')
data.min_values = lambda: [i for i in data.most_common() if i[1] == min(data.values())]
data.max_values = lambda: [i for i in data.most_common() if i[1] == max(data.values())]

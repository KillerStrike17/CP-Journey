class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        deg_dict = {}
        for x in roads:
            graph[x[0]].append(x[1])
            graph[x[1]].append(x[0])
            if x[0] not in deg_dict:
                deg_dict[x[0]] = 1
            else:
                deg_dict[x[0]] += 1
            if x[1] not in deg_dict:
                deg_dict[x[1]] = 1
            else:
                deg_dict[x[1]] += 1
        l = []
        for x in deg_dict:
            l.append([deg_dict[x], x])
        l.sort(reverse=True)

        print(l)
        print(graph)
        num = {}
        k = n
        for x in l:
            num[x[1]] = k
            k -= 1

        sum = 0
        print(num)
        for x in graph:
            for k in graph[x]:
                sum += num[x]+num[k]
        return sum//2

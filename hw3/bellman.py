def txt2dic(name_txt_file):
    dic = {}
    with open(name_txt_file) as f:
        for i, line in enumerate(f):
            if '\n' in line:
                line = line.replace('\n', '')
            line = line.strip()
            if i % 2 == 0:
                line = int(line)
                dic[line] = None
                last_key = line
            else:
                val = {}
                if line != '':
                    line = tuple(line.split(','))
                    for j, st in enumerate(line):
                        st = st.strip()
                        if j % 2 == 0:
                            if st[1] == '-':
                                for i in range(2, len(st)):
                                    if not st[i].isdigit():
                                        break
                                val[-1*int(st[2:i])] = None
                            else:
                                val[int(st[1:])] = None
                            key = int(st[1])
                        else:
                            if st[0] == '-':
                                for i in range(1, len(st)):
                                    if not st[i].isdigit():
                                        break
                                val[key] = -1*int(st[1:i])
                            else:
                                for i in range(len(st)):
                                    if not st[i].isdigit():
                                        break
                                val[key] = int(st[:-1])
                dic[last_key] = val
    return dic
def find_negative_circles(name_txt_file):
    graph = txt2dic(name_txt_file)
    nodes = list(set(graph.keys() + [k for v in graph.values() if v!= None for k in v.keys()]))
    l = 0
    pre = {}
    print(graph)
    while pre == {} and l < len(nodes):
        n = len(nodes) + 1
        M = {i: {j: float("inf") for j in nodes} for i in range(n)}
        M[0][nodes[l - 1]] = 0
        opt = float("inf")
        pre = {}
        for i in range(1, n):
            for j in nodes:
                minimum = float("inf")
                min_node = None
                #print(j)
                if j in graph.keys() and graph[j]:
                    for k in graph[j].keys():
                        if M[i - 1][k] + graph[j][k] < minimum:
                            minimum = M[i - 1][k] + graph[j][k]
                            min_node = k
                if minimum < M[i][j]:
                    pre[min_node] = j
                M[i][j] = min(M[i - 1][j], minimum)
                if M[i][j] < opt:
                    opt = M[i][j]
                    source = j
        if M[n-1][nodes[-1]] > M[n -2][nodes[-1]]:
            return None
        l += 1

    def path(source, destination, bk, n):
        ans = []
        i = 0
        tracker = None
        prv = source
        while prv in bk.values() and i < n:
            prv = bk.keys()[bk.values().index(prv)]
            ans.append(prv)
            i += 1
        ans = ans[::-1]
        while i < n and tracker != source:
            ans.append(source)
            if source in bk.keys():
                source = bk[source]
                tracker = None
            else:
                tracker = source
            i += 1
        return ans[::-1]
    #return path(source, nodes[-1], pre, n), opt, source, nodes[-1]
    p1 = path(source, nodes[-1], pre, n - 1)

    def detect(path, graph):
        stack = []
        cycles = []
        val = 0
        stack.append(path.pop(0))
        while path != []:
            val += graph[stack[-1]][path[0]]
            stack.append(path.pop(0))
            if len(set(graph[stack[-1]].keys()) & set(stack)) > 0:
                if val == 0:
                    continue
                if val < 0:
                    cycles.append(stack)
                else:
                    val = 0
                if path != []:
                    stack = [path.pop(0)]
        return cycles if cycles != [] else None
    cycles = detect(p1, graph)
    return cycles[0] if len(cycles) == 1 else cycles

if __name__ == "__main__":
    print(find_negative_circles("graph3.txt"))

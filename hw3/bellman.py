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
    n = len(nodes) + 1
    M = {i: {j: float("inf") for j in nodes} for i in range(n)}
    M[0][nodes[-1]] = 0
    opt = float("inf")
    pre = {}
    for i in range(1, n):
        for j in nodes:
            minimum = float("inf")
            min_node = None
            if graph[j] != None:
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
    #return pre
    def path(source, destination, bk, n):
        ans = []
        i = 0
        while destination in bk and i < n:
            ans.append(destination)
            destination = bk[destination]
            i += 1
        return ans[::-1]
    return path(source, nodes[-1], pre, n)

if __name__ == "__main__":
    print(find_negative_circles("graph3.txt"))

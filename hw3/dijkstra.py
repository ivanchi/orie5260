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

def find_shortest_path(name_txt_file, source, destination):
    graph = txt2dic(name_txt_file)
    S = []
    F = PriorityQueue()
    d = {}
    d[source] = 0
    F.add(source, d[source])
    bk = {}
    while not F.isEmpty():
        f = F.poll()
        S.append(f)
        if f in list(graph.keys()) and graph[f] != None:
            for w in list(graph[f].keys()):
                if w not in S and not F.exist(w):
                    d[w] = d[f] + graph[f][w]
                    F.add(w, d[w])
                    bk[w] = f
                elif d[w] > d[f] + graph[f][w]:
                    d[w] = d[f] + graph[f][w]
                    bk[w] = f
    def path(source, destination, bk):
        ans = []
        while destination in bk and bk[destination] not in ans:
            ans.append(destination)
            destination = bk[destination]
        ans.append(source)
        return ans[::-1]
    return (d[destination], path(source, destination, bk))


class PriorityQueue(object):

    def __init__(self):
        self.heap = []

    def add(self, e, d):
        if len(self.heap) == 0:
            self.heap.append([e, d])
        for i in range(1, len(self.heap)+1):
            if self.heap[-i][1] > d:
                self.heap.append([e, d])
                break
            if i == len(self.heap):
                self.heap.insert(0, [e, d])

    def isEmpty(self):
        if len(self.heap) == 0:
            return True
        else:
            return False

    def peek(self):
        assert self.isEmpty() == False
        return heap[-1][0]

    def poll(self):
        assert self.isEmpty() == False
        e = self.heap.pop()[0]
        return e

    def exist(self, e):
        for i in range(1, len(self.heap) + 1):
            if self.heap[-i][0] == e:
                return True
        return False

if __name__ == "__main__":
    print(find_shortest_path('graph2.txt', 1, 7))

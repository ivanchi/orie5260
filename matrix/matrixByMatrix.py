from pyspark import SparkConf, SparkContext

def matrixByMatrix(M1, M2):
    '''Using spark multiply a matrix (n x p) by vector (p x m)
       Output - n x m matrix
    '''
    
    def mul(tuple):
        s = 0
        for i in range(len(tuple[1][0])):
            s += tuple[1][0][i] * tuple[1][1][i]
        return (tuple[0], s)
    
    
    # Reading input
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    data1 = sc.textFile(M1)
    data2 = sc.textFile(M2)
    
    # Transform data and count index
    nRow1 = data1.count()
    matrix1 = data1.map(lambda l: l.split(',')).flatMap(lambda entry: [(int(e), int(entry[e])) for e in range(len(entry))])
    nCol1 = matrix1.count()/nRow1
    
    nRow2 = data2.count()
    matrix2 = data2.map(lambda l: l.split(',')).flatMap(lambda entry: [(int(e), int(entry[e])) for e in range(len(entry))])
    nCol2 = matrix2.count()/nRow2
    
    assert nCol1 == nRow2
    
    mat1 = matrix1.zipWithIndex().map(lambda l: (l[1]//nCol1, l[0][1]))
    ma1 = mat1.groupByKey().mapValues(list).map(lambda v: [((v[0], int(i)),v[1]) for i in range(nCol2)])
    m1 = ma1.flatMap(lambda l: l)
    
    mat2 = matrix2.groupByKey().mapValues(list)
    ma2 = mat2.map(lambda v: [((i, v[0]), v[1]) for i in range(nRow1)])
    m2 = ma2.flatMap(lambda l: l)
    
    # Merge two matrics
    matrix = m1.union(m2).groupByKey().mapValues(list)
    
    output = matrix.map(mul).sortByKey().collect()
    str_mat = ''
    
    for i in range(len(output)):
        if i % nCol2 == 0:
            str_mat += str(output[i][1]) + ','
        else:
            str_mat += str(output[i][1]) + '\n'
    
    f = open("matrixByMatrixResult.txt","w")
    f.write(str_mat)
    f.close()
    
    return str_mat



if __name__ == "__main__":
    a = matrixByMatrix('matrix1.txt', 'matrix2.txt')

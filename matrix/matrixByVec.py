from pyspark import SparkConf, SparkContext

def matrixByVec(M, v):
    '''Using spark multiply a matrix (n x p) by vector (p x 1)
       Output - n x 1 vector
    '''
    
    # Reading input
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    matrix = sc.textFile(M)
    vector = sc.textFile(v)
    
    # Transform data and count index
    m = matrix.map(lambda line: line.split(','))
    nRow = matrix.count()
    mat = m.flatMap(lambda parts: [(int(i), int(parts[i])) for i in range(len(parts))])
    nCol = mat.count()/nRow
    
    a = mat.zipWithIndex()
    new_mat = a.map(lambda t: [(t[1])//nCol, t[0]])
    
    v = vector.map(lambda line: line.split(',')).flatMap(lambda e: [(int(i), int(e[i])) for i in range(len(e))])
    
    assert nCol == v.count()
    
    rows = new_mat.join(v)
    
    # Multiply matrix by vector then reduce
    rows_mult = rows.map(lambda tuple: (tuple[0], (tuple[1][0][0], tuple[1][0][1] * tuple[1][1])))
    rows_val = rows_mult.map(lambda t: t[1])
    
    new_v = rows_val.reduceByKey(lambda v1, v2: v1 + v2)
    vector = new_v.sortByKey().collect()
    
    vec2str = ''.join(str([i[1] for i in vector]))[1:-1]
    
    f = open("matrixByVecResult.txt","w")
    f.write(vec2str)
    f.close()
    
    return vector

if __name__ == "__main__":
    a = matrixByVec('A.txt', 'B.txt')

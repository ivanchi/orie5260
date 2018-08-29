from pyspark import SparkConf, SparkContext
import numpy as np

def pyspark_kmeans(data_txt, c_txt):
    """k-mean algotihm to cluster
    """
    # suppress large decimal floats
    np.set_printoptions(suppress=True)
    
    # set up spark
    conf = SparkConf()
    sc = SparkContext(conf=conf)
    
    # loading data and initial points
    data = sc.textFile(data_txt).map(lambda line: np.array([float(x) for x in line.split(' ')])).cache()
    centroids = sc.textFile(c_txt).map(lambda line: np.array([float(x) for x in line.split(' ')]))
    
    # adding index to data
    dat = data.zipWithIndex()

    max_iter = 20
    
    for _ in range(max_iter):
        # adding index to centroids
        cen = centroids.zipWithIndex()
        # adding every centoirds to data
        distance = dat.cartesian(cen)
        # map and calculate distance to each centroids
        dist = distance.map(lambda line: (line[0][1], (np.linalg.norm(line[0][0] - line[1][0]), line[0][0], line[1][1])))
        # reduce to get the minimum distance cluster
        dis = dist.reduceByKey(lambda v1, v2: min(v1, v2)).map(lambda line: (line[1][2], (line[1][1], 1)))
        # average cluster to get new centroids
        centroids = dis.reduceByKey(lambda (v1, v2), (x1, x2): (v1 + x1, v2 + x2)).map(lambda l: [l[1][0]/l[1][1]])
    lists = centroids.collect()
    
    # output to txt file
    txt = ''
    for i in lists:
        line = np.array2string(i[0], separator='' ,suppress_small=True)
        new_line = ' '.join(line.split())[2:-2] + '\n'
        txt += new_line
    new_txt = txt.rstrip('\n')
    text_file = open("Output.txt", "w")
    text_file.write(new_txt)
    text_file.close()
    
    return new_txt


if __name__ == "__main__":
    pyspark_kmeans("data.txt", "c1.txt")

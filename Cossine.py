from scipy import spatial

dataSetI = [4, 14, 2, 8]
dataSetII = [2, 7, 1, 4]
result = 1 - spatial.distance.cosine(dataSetI, dataSetII)
print(result)
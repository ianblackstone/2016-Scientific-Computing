import numpy as np

data = np.loadtxt(fname='co2_mm_mlo.txt')
december = np.squeeze(np.where(data, 1 == 12))

print(data[december])
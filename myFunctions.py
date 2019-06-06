import numpy as np

def hello():
  print ("Hello World \n")


def features_1(data):
  feature_avg  = data.mean(axis=1)
  feature_std  = data.std(axis=1)
  feature_max  = data.max(axis=1)
  feature_min  = data.min(axis=1)
  #return feature_avg
  #return np.column_stack((feature_avg, feature_std))
  #return np.column_stack((feature_max, feature_min))
  #return np.column_stack((feature_avg, feature_std, feature_max, feature_min))

  return np.column_stack((feature_avg, feature_std, feature_max))

def features_2(data):
  feature_avg  = data.mean(axis=1)
  feature_std  = data.std(axis=1)
  feature_max  = data.max(axis=1)
  feature_min  = data.min(axis=1)
  feature_avg_sqr = np.power(feature_avg, 2)
  feature_avg_cube = np.power(feature_avg, 3)

  data_diff1 = np.diff(data, axis=1)
  feature_avg_diff1  = data_diff1.mean(axis=1)
  feature_std_diff1  = data_diff1.std(axis=1)
  feature_max_diff1  = data_diff1.max(axis=1)
  feature_min_diff1  = data_diff1.min(axis=1)
  feature_avg_diff1_sqr  = np.power(feature_avg_diff1, 2)
  feature_avg_diff1_cube = np.power(feature_avg_diff1, 3)

  data_diff2 = np.diff(data, n=2, axis=1)
  feature_avg_diff2  = data_diff2.mean(axis=1)
  feature_std_diff2  = data_diff2.std(axis=1)
  feature_max_diff2  = data_diff2.max(axis=1)
  feature_min_diff2  = data_diff2.min(axis=1)
  feature_avg_diff2_sqr  = np.power(feature_avg_diff2, 2)
  feature_avg_diff2_cube = np.power(feature_avg_diff2, 3)


  #return feature_avg
 

  #return np.column_stack((feature_avg, feature_avg_sqr, feature_avg_cube, feature_max, feature_avg_diff1, feature_avg_diff1_sqr, feature_max_diff1, feature_avg_diff2, feature_avg_diff2_sqr, feature_avg_diff2_cube, feature_max_diff2))

  #return np.column_stack((feature_avg, feature_avg_sqr, feature_max, feature_avg_diff1, feature_avg_diff1_sqr ))

  #return np.column_stack((feature_avg, feature_avg_sqr, feature_avg_cube, feature_max, feature_avg_diff1, feature_max_diff1, feature_avg_diff2, feature_max_diff2))

  #return np.column_stack((feature_avg, feature_avg_sqr, feature_avg_cube, feature_max, feature_avg_diff1, feature_avg_diff1_sqr,feature_avg_diff1_cube, feature_max_diff1, feature_avg_diff2, feature_avg_diff2_sqr, feature_avg_diff2_cube, feature_max_diff2))
  return np.column_stack((feature_avg, feature_avg_sqr, feature_avg_cube, feature_max, feature_avg_diff1, feature_avg_diff1_sqr,feature_avg_diff1_cube, feature_max_diff1, feature_avg_diff2, feature_avg_diff2_sqr, feature_avg_diff2_cube, feature_max_diff2, feature_std, feature_std_diff1, feature_std_diff2))

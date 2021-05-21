import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer

cancer = load_breast_cancer()
cancer.keys()

#print(cancer.DESCR) # Print the data set description
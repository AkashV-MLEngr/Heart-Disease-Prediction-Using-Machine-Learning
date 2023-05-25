import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pickle
from numpy import random

def colc():
  x = random.randint(100, size=(10))
  y = np.sort(x)
  return y[-1]
def colcN():
  x = random.randint(100, size=(10))
  y = np.sort(x)
  print('nnnn',y[0])
  return y[0]
def pn(x, y):
    if x == 2 and y == 0:
        print('p :', colcN())
        return colcN()
        
    else:
        print('nn :', colc())
        return colc()
        
if __name__ == "__main__":
    data=pd.read_csv("heart.csv")
    X=data.drop("DEATH_EVENT",axis=1)
    Y=data[["DEATH_EVENT"]]
    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=7)
    model=LogisticRegression(max_iter=1000)
    model.fit(X_train,Y_train)


    file =open('model.pkl','wb')
    pickle.dump(model,file)
    file.close()
    

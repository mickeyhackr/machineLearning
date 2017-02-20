import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d, Axes3D



def predict(time,position,innings,ball_faced):
    df_adv = pd.read_csv("C:/Users/vaibhav_shu/Desktop/cricdata.csv")
    mat = df_adv.as_matrix()
    X = (df_adv[['Time', 'Pos', 'Inns', 'BF']])
    Y = (df_adv[['Runs']])
    est = sm.OLS(Y, X).fit()
#    print(est.summary())
    runs =  float(est.params["Time"])*time + float(est.params["Pos"])*position + float(est.params["BF"])*ball_faced + float(est.params["Inns"])*innings
    print("Predicted run : ")
    print runs

    fig, ax = plt.subplots()
    fig = sm.graphics.plot_fit(est, 0, ax=ax)
    ax.set_ylabel("Run Scored")
    ax.set_xlabel("Time")
    ax.set_title("Multivariate Regression")
    plt.show()


time = input("Time spent in the crease in minutes : ")
position = input("Position(1,9) : ")
innings = input("Innings (1,2) : ")
ball_faced = input("balls faced : ")


predict(time,position,innings,ball_faced)





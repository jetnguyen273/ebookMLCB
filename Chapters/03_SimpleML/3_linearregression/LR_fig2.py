# -*- coding: utf8 -*-
from __future__ import print_function, unicode_literals
import matplotlib.font_manager as fm
set([f.name for f in fm.fontManager.ttflist])
import numpy as np 
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
plt.rcParams['font.family'] = 'Lucida Grande'
from sklearn import datasets, linear_model

N = 30
N_test = 20 
X = np.random.rand(N, 1)*5
y = 3*(X -2) * (X - 3)*(X-4) +  10*np.random.randn(N, 1)

X_test = (np.random.rand(N_test,1) - 1/2) *2
y_test = 3*(X_test -2) * (X_test - 3)*(X_test-4) +  10*np.random.randn(N_test, 1)

def buildX(X, d = 2):
    res = np.ones((X.shape[0], 1))
    for i in range(1, d+1):
        res = np.concatenate((res, X**i), axis = 1)
    return res 

def myfit(X, y, d):
    Xbar = buildX(X, d)
    regr = linear_model.LinearRegression(fit_intercept=False) # fit_intercept = False for calculating the bias
    regr.fit(Xbar, y)

    w = regr.coef_
    # Display result
    w_0 = w[0][0]
    w_1 = w[0][1]
    x0 = np.linspace(-1, 7, 200, endpoint=True)
    y0 = np.zeros_like(x0)
    ytrue = 5*(x0 - 2)*(x0-3)*(x0-4)
    for i in range(d+1):
        y0 += w[0][i]*x0**i
    plt.figure(figsize=(5,4))
    # Draw the fitting line 
    with PdfPages('polyreg.pdf') as pdf:
        plt.scatter(X.T, y.T, c = 'w', s = 40, edgecolors = 'k', label = "training data")     # data 
        print(X_test.shape, y_test.shape)
    #     plt.scatter(X_test.T, y_test.T, c = 'y', s = 40, label = 'Test samples')     # data 

        l1, = plt.plot(x0, y0, 'k', linewidth = 2, label="trained model")   # the fitting line
        plt.legend(handles = [l1], fontsize = 18)
    #     plt.plot(x0, ytrue, 'b', linewidth = 2, label = "train model")   # the fitting line
        plt.xticks([], [])
        plt.yticks([], [])


        plt.title('Polynomial regression', fontsize = 14)
        plt.axis([-4, 10, np.amax(y_test)-100, np.amax(y) + 30])
        plt.legend(loc="lower right", fontsize = 14)

        fn = 'linreg_' + str(d) + '.png'

        plt.xlabel('$x$', fontsize = 20);
        plt.ylabel('$y$', fontsize = 20);

        pdf.savefig(bbox_inches='tight') #, dpi = 600)

        plt.show()
    print(w)

myfit(X, y, 3)
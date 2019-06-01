
# coding: utf-8

# In[1]:


import sklearn
sklearn.__version__


# In[7]:


import plotly.plotly as py
import plotly.graph_objs as go
from plotly import tools

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler
from sklearn import datasets


# In[8]:


params = [{'solver': 'sgd', 'learning_rate': 'constant', 'momentum': 0,
           'learning_rate_init': 0.2},
          {'solver': 'sgd', 'learning_rate': 'constant', 'momentum': .9,
           'nesterovs_momentum': False, 'learning_rate_init': 0.2},
          {'solver': 'sgd', 'learning_rate': 'constant', 'momentum': .9,
           'nesterovs_momentum': True, 'learning_rate_init': 0.2},
          {'solver': 'sgd', 'learning_rate': 'invscaling', 'momentum': 0,
           'learning_rate_init': 0.2},
          {'solver': 'sgd', 'learning_rate': 'invscaling', 'momentum': .9,
           'nesterovs_momentum': True, 'learning_rate_init': 0.2},
          {'solver': 'sgd', 'learning_rate': 'invscaling', 'momentum': .9,
           'nesterovs_momentum': False, 'learning_rate_init': 0.2},
          {'solver': 'adam', 'learning_rate_init': 0.01}]
 
labels = ["constant learning-rate", "constant with momentum",
          "constant with Nesterov's momentum",
          "inv-scaling learning-rate", "inv-scaling with momentum",
          "inv-scaling with Nesterov's momentum", "adam"]

plot_args = [{'c': 'red', 'linestyle': '-'},
             {'c': 'green', 'linestyle': '-'},
             {'c': 'blue', 'linestyle': '-'},
             {'c': 'red', 'linestyle': '--'},
             {'c': 'green', 'linestyle': '--'},
             {'c': 'blue', 'linestyle': '--'},
             {'c': 'black', 'linestyle': '-'}]


# In[9]:


def plot_on_dataset(X, y, name, leg):
    # for each dataset, plot learning for each learning strategy
    print("\nlearning on dataset %s" % name)
    
    X = MinMaxScaler().fit_transform(X)
    mlps = []
    if name == "digits":
        # digits is larger but converges fairly quickly
        max_iter = 15
    else:
        max_iter = 400

    for label, param in zip(labels, params):
        print("training: %s" % label)
        mlp = MLPClassifier(verbose=0, random_state=0,
                            max_iter=max_iter, **param)
        mlp.fit(X, y)
        mlps.append(mlp)
        print("Training set score: %f" % mlp.score(X, y))
        print("Training set loss: %f" % mlp.loss_)
        
    data = []
    
    for mlp, label, args in zip(mlps, labels, plot_args):
            trace = go.Scatter(y=mlp.loss_curve_, name=label,
                               mode='lines', showlegend=leg,
                               line=dict(width=1))
            data.append(trace)
    
    return data


# In[10]:


iris = datasets.load_iris()
digits = datasets.load_digits()
data_sets = [(iris.data, iris.target),
             (digits.data, digits.target),
             datasets.make_circles(noise=0.2, factor=0.5, random_state=1),
             datasets.make_moons(noise=0.3, random_state=0)]

names = ['iris', 'digits', 'circles', 'moons']
fig = tools.make_subplots(rows=2, cols=2, print_grid=False,
                          subplot_titles=tuple(names))

for i, data, name in zip(np.linspace(0, 3, 4), 
                         data_sets, names):
    if(i==0):
        leg=True
    else:
        leg=False
    trace = plot_on_dataset(*data, name=name, leg=leg)
    for j in range(0, len(trace)):
         fig.append_trace(trace[j], int(i/2+1), int(i%2+1))
            
fig['layout'].update(height=700, hovermode='closest')





# In[17]:


py.iplot(fig)


# In[19]:


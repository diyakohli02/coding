import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
from tkinter import messagebox
import json


with open("data.json","r") as data_read:
    data=json.load(data_read)

d=data["daily practice score"]
a=data["assessment score"]
t=data["final test score"]

d = int(d)
a = int(a)
t = int(t)
print(d)
x = np.array(["Daily Practice", "Assessment", "Final Testing"])
y = np.array([d, a, t])
plt.bar(x, y)
plt.show()


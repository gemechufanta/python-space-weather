# coding: utf-8
import pandas as pd
ds = pd.read_csv('noaa_goes13_epead_electron_flux_a_5m.csv')
ds
ds.columns=['time','electron_flux']
ds.time 
time = ds.time 
ef=ds.electron_flux
import matplotlib.pyplot as plt
plt.plot(time, ef)
plt.show() 
plt.savefig("electron_density.png")
plt.plot(time, ef)
plt.savefig("electron_density.png")

# coding: utf-8
import pandas as pd
ds = pd.read_csv('noaa_goes13_epead_electron_flux_a_5m.csv')
ds.columns=['time','electron_flux']
reference_date = '1970-01-01'
ds['time'] = pd.date_range(start=reference_date, periods=len(ds.time), freq='L')
ds.time 
time = ds.time 
ef=ds.electron_flux
import matplotlib.pyplot as plt
plt.plot(time[ef > 0], ef[ef > 0], 'ro-')
plt.title('Electron Density for Space Weather')
plt.ylabel('$\sigma $')
plt.xlabel('time ')
plt.savefig("electron_density.png")
plt.show() 

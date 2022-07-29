##########################
# This is a tutorial for space weather interns
# Prepared by Dr. Gemechu Fanta
#########################
import pandas as pd
ds = pd.read_csv('noaa_goes13_epead_electron_flux_a_5m.csv')
ds.columns=['time','electron_flux']
reference_date = '1970-01-01'
#ds['time'] = pd.date_range(start=reference_date, periods=len(ds.time), freq='L')
ds['time'] = pd.to_datetime(ds['time'], unit='ms', origin = pd.Timestamp(reference_date))
ds.time 
time = ds.time 
ef=ds.electron_flux
import matplotlib.pyplot as plt
plt.plot(time[ef > 0], ef[ef > 0], 'ro-')
plt.xticks(rotation = 30)
plt.title('Electron Density for Space Weather')
plt.ylabel('$\sigma $')
plt.xlabel('time in days ')
plt.savefig("electron_density.png")
plt.show() 

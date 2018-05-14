import xarray as xr
import matplotlib.pylab as plt

"""Plotando dados e controles para todo Brasil em um dia:

Todos os arquivos da variavel diarios de Rs sao necessarios, ou seja,
os de controle tambem"""

# set correct path of the variables
path_var = 'D:/Dropbox/ParaUbuntu/netcdfgrid3/'

# set correct path of the controls
path_control = 'D:/Dropbox/netcdfgrid3/controls/'

data = xr.open_mfdataset(path_var + 'Rs_daily_UT_Brazil_v2*1.nc')
data_control = xr.open_mfdataset(path_control + '/Rs_daily_UT_Brazil_v2*_Control.nc')
Rs = data['Rs']
Rs_count = data_control['count']
Rs_dist_nearest = data_control['dist_nearest']

# escolhendo o dia
day2get = '2008-05-15'

Rs2_one_day = Rs.sel(time=day2get)
Rs2_one_day_count = Rs_count.sel(time=day2get)
Rs2_one_dist_nearest = Rs_dist_nearest.sel(time=day2get)

# plotando
plt.subplot(131), Rs2_one_day.plot(), plt.axis('off')
plt.subplot(132), Rs2_one_day_count.plot(), plt.axis('off')
plt.subplot(133), Rs2_one_dist_nearest.plot(), plt.axis('off')
plt.show()
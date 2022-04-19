
# Matplotlib simple tick customizer

mpl_scaler customize your matplotlib axes' tick location/label simply;
```
from mpl_scaler import set_xticks, set_yticks
set_xticks(ax, diff=7.5, format=lambda x, _: f"{x:.0f}km" if x%1==0 else f"{x:.1f}km")
set_yticks(ax, n=5, format="{:d}$")
```
![example](images/example.png)

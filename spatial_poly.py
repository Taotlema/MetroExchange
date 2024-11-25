import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import geopandas as gpd

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# import data shp
indo = gpd.read_file("/kaggle/input/map-data/INDONESIA_PROP.shp")
indo.head()

#vizualize with polygon data
indo.plot(column='Propinsi', cmap='Setl', legend=True, figsize=(30,40))
plt.title('TITIK GEMPA')
plt.show()
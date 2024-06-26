import numpy as np
import pandas as pd
import os


try:
    os.makedirs("data")
except:
    pass

for year in range(2004,2024):
   for month in range(1,13):
     for day in range(31):
      try:
          os.makedirs(f"data/activity_{year}_{month}")
      except:
          pass
      data = []
      for hour in range(24):
            if hour < 9:
                a = 0
            else:
                a = np.random.randint(1,5)
            data.append({
                "hour": hour,
                "activity_level": np.random.randint(1,5)
            })
      data = pd.DataFrame(data)
      data.to_csv(f"data/activity_{year}_{month}/activity_{year}_{month}_{day}.csv")




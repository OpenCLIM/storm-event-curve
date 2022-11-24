import pandas as pd
import numpy as np
import os

data_path = os.getenv('DATA_PATH','/data')
inputs_path = os.path.join(data_path, 'inputs')
outputs_path = os.path.join(data_path, 'outputs')
if not os.path.exists(outputs_path):
    os.mkdir(outputs_path)

# Read environment variables
rainfall_total = 60 #int(os.getenv('TOTAL_DEPTH'))
duration = 2 #int(os.getenv('DURATION'))

unit_profile = np.array([0.017627993, 0.027784045, 0.041248418, 0.064500665, 0.100127555, 0.145482534, 0.20645758,
                         0.145482534, 0.100127555, 0.064500665, 0.041248418, 0.027784045, 0.017627993])

rainfall_times = np.linspace(start=0, stop=duration*3600, num=len(unit_profile))
rainfall_times = rainfall_times.astype(int)

unit_total = sum((unit_profile + np.append(unit_profile[1:], [0])) / 2 *
                 (np.append(rainfall_times[1:], rainfall_times[[-1]]+1)-rainfall_times))

rainfall = pd.DataFrame(list(unit_profile*rainfall_total/unit_total/1000) + [0,0],
                        index=list(rainfall_times) + [duration*3600+1, duration*3600+2])

with open(os.path.join(outputs_path,'rainfall_data.txt'),'a') as f:
    print('* * *', file = f)
    print('* * * rainfall ***', file = f)
    print('* * *', file = f)
    print(len(unit_profile), file = f)
    print('* * *', file = f)
    print(rainfall.to_string(header=False), file=f)
f.close()
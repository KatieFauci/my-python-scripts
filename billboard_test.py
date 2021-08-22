import os
import billboard



charts_list = billboard.charts()
output = ''
# check each chart
for chart in charts_list:
  this_chart = billboard.ChartData(chart)
  rank = 0
  print(this_chart.title)
  for entry in this_chart:
    #print(str(entry))
    rank = rank + 1
    if 'BTS' in str(entry):
      output = output + f'{this_chart.title} - {rank} - {entry}\n'

  print(output)
print(output)



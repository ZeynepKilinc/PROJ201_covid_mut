import pandas as pd
import matplotlib.pyplot as plt

def positional_conservation_calculator(filename):
  with open(filename, 'r') as f:
    lines=f.readlines()
  titles=[]
  sequences=[]
  for i in range(0, len(lines)):
    index=lines[i].find(' ')
    titles.append(lines[i][0:index])
    temp_sequence=lines[i][index:].strip()
    sequences.append(temp_sequence)
  sequence_dictionary={}
  for index in range(0,len(titles)):
    sequence_dictionary[titles[index]]=sequences[index]
  df=pd.DataFrame()
  nucleotide_list=[]
  for j in range(0,len(sequences[0])):
    for k in range(0,len(sequences)):
      nucleotide_list.append(sequences[k][j])
    df[str(j)]=nucleotide_list
    nucleotide_list=[]
  modes = df.mode()
  counts = df.apply(lambda x: x.value_counts().get(x.mode()[0], 0))
  percentages = counts / len(df) * 100
  plt.bar(x=percentages.index, height=percentages.values)
  plt.xlabel('')
  plt.xticks([])
  plt.ylabel('Conservation Rate')
  plt.show()
  return sequence_dictionary

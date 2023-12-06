import pandas as pd
import numpy as np


#file name
#specify path for file
data_frame = pd.read_csv ('/Users/u5504461/Downloads/Part2Data 4/C1_002/1.csv')

data_array = data_frame.values
print(data_array)

total_size = len(data_array)

#reorganizing array into matrix
#block_size = the number of frames / column = all the values for one ROI
#num_blocks = number of ROIs = number of rows / each row is for one ROI, with 87 measurements.
block_size = 87
num_blocks = 47
expected_size = block_size * num_blocks

if total_size != expected_size:
    print("not good")
else:
    data_blocks = data_array.reshape (num_blocks, block_size)
    #Reshape data into 47 blocks of size 87

print(data_blocks.shape)
print(data_blocks)

block_means = np.mean(data_blocks, axis=1)

for i, mean_value in enumerate(block_means):
    print(f"Block {i + 1}: Mean = {mean_value}")

np.savetxt('/Users/u5504461/Desktop/block_means.csv', block_means, delimiter=',', fmt='%.6f')

#column means
column_means = np.mean(data_blocks, axis=0)

# Display the means of each position
for i, mean_value in enumerate(column_means):
    print(f"Position {i + 1}: Mean = {mean_value}")

np.savetxt('/Users/u5504461/Desktop/column_means.csv', column_means, delimiter=',', fmt='%.6f')

# Image-Analysis-
Author: 5504461 
Date: December 2023 

The code was written to analyse data acquired by running ImageJ script for counting the number of motors on each microtubule in time. 
The script gives back the data organised in a column. Make sure when uploading the files for analysis, to only have only column in the .csv file (which means deleting the first numeric column, and only leaving number of motors column - your data). 

The script makes an array, then organises it into matrix with specified number of rows and columns. 

ImageJ script gives back the data file with number of motors on one microtubule (ROI) in all the frames, and then goes onto giving the data for second ROI, and then third, etc. All the data is organised in one column, which makes life easier. 

The number of rows in a matrix is the number of ROIs (in the script = num_blocks). And number of columns is the number of frames (in the script = block_size). 

block_means = calculates the mean values of motors on one microtubule in all the frames (in time). This is also a mean of each row in the matrix. 

column_means = calculates the mean value of motors on all the microtubules in each frame. So it would give mean number of all the motors on all microtubules in each frame (in time). Column 1 is the first frame, column 2 the second frame, column 3 the third, etc. 

The script exports data as means in specified directory. Remember to specify the file path for exporting. 

Running the script: 

1. Install numpy and pandas libraries. Pandas allows you to upload data in a .csv format. Numpy library helps you analyse the data. 
To install these two libraries, go to terminal and type first: ‘pip install numpy’, once it is installed type ‘pip install pandas’. 
2. When uploading the data for analysis, you need to check the file paths. First path of each file uploaded for analysis, then paths for exporting the files. 
3. When uploading the data make sure to organise it nicely. Your .csv file needs only one column with you data, and do not remove the first row (header row), as the script will then starting organising data from the second data value. 
4. Change the block_size and num_blocks according to your needs. 

Limitations: 

1. The script runs only when you have one column of data. 
2. You need to install two libraries, and then import them in your script, otherwise it will not work. 
3. Overwrites the exported data with new one if you do not change the file names in the script, or after you have exported them. 
4. It does not give graphical representation. You could use another library in python for this called MatPlotLib, or import your data in excel or R studio. 

If you have any suggestions on how to improve the script, please let the author know. 



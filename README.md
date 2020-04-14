# CS451 Project

CS451 Project

## Download dataset

1. `source cs451/bin/activate`  

2. `kaggle datasets download -d smid80/coronavirus-covid19-tweets`  

3. `mkdir data`  

4. `unzip coronavirus-covid19-tweets.zip -d data`  

5. remove first lines from all tweet csv files (2020-03-*.CSV), and combine all files together. (ex. `cat file1 file2 file3 > merged_data.csv`). Then put them inside data directory.  

6. If you want to run on datasci, I think you have to `hadoop fs -put merged_data.csv` and change the datasci command below.  


## Commands to run spark

### Linux
`spark-submit --class ca.uwaterloo.cs451.project.TweetCount target/assignments-1.0.jar --input data/trunc-2020-03-12.csv --output output`

### Datasci
`spark-submit --class ca.uwaterloo.cs451.project.TweetCount --num-executors 2 --executor-cores 4 --executor-memory 24G target/assignments-1.0.jar --input /user/ky2shin/merged_data.csv --output output`  
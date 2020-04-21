# CS451 Project

CS451 Project

## Download dataset

1. `source cs451/bin/activate`  

2. `kaggle datasets download -d smid80/coronavirus-covid19-tweets`  

3. `mkdir data`  

4. `unzip coronavirus-covid19-tweets.zip -d data`  

5. Combine all files together. (ex. `cat file1 file2 file3 > merged_data.csv`). Then put them inside data directory.  


## Commands to run spark

### Linux
`spark-submit --class ca.uwaterloo.cs451.project.TweetCount target/assignments-1.0.jar --input data/trunc-2020-03-12.csv --output output`

### Datasci

Put File into HDFS

`hadoop fs -put <file>`

Run Task

`spark-submit --class ca.uwaterloo.cs451.project.TweetCount --num-executors 2 --executor-cores 4 --executor-memory 24G target/assignments-1.0.jar --input /user/<username>/merged_data.csv --output output`  


Print Output

`hadoop fs -cat output/*`

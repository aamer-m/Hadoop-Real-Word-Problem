#!/bin/bash
hadoop fs -rm -r mapsome.py
hadoop fs -rm -r reducesome.py
hadoop fs -put mapsome.py
hadoop fs -put reducesome.py
hadoop fs -chmod 777 mapsome.py
hadoop fs -chmod 777 reducesome.py
#dT="$(date --rfc-3339=seconds)"
dT="$(date)"
dirName="${dT//[-,+: ]/}"
fileName="log_"$dirName
time hadoop jar /root/hadoop-2.7.1/share/hadoop/tools/lib/hadoop-streaming-2.7.1.jar -input /data/twitter -output $dirName -file *.py -mapper mapsome.py -reducer reducesome.py > $fileName 2>&1
mkdir $dirName
mv $fileName $dirName
mkdir $dirName/input
mkdir $dirName/output
hadoop fs -get mapsome.py "$dirName"/input/
hadoop fs -get reducesome.py "$dirName"/input/
hadoop fs -get $dirName "$dirName"/output/


#!/bin/bash
for i in {6..10}
do
python write_json.py $i
mkdir "./simulation_${i}"
mv config.json "./simulation_${i}" 
cp namelist.py "./simulation_${i}" 
(cd ./simulation_${i} && ../../../Smilei/smilei namelist.py)
done

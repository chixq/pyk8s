#!/bin/bash

for file in `ls |grep '.json'`
do
    echo $file
    #$file = $file%\.json
    perl gen_py_source.pl ${file%\.json}  
done

#!/bin/bash
cp endpoints_org.py endpoints.py 
for file in `ls |grep '.json'`
do
    echo $file
    #$file = $file%\.json
    #perl gen_py_source.pl ${file%\.json} 
    perl gen_con.pl ${file%\.json} 
    perl gen_endpoints.pl ${file%\.json} 
done

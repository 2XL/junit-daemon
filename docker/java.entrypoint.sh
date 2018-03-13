#!/bin/bash
set -eu



function nameko {
    echo "Start nameko service"
    invoke wait -h='mq' -p=5673


    # wait until broker url is available
    echo $BROKER_URL

    exec nameko run --config ./nameko.yml namekos
}


for var in "$@"
do
case $var in
nameko) shift
    nameko
    ;;
*)
    break # break the for loop
	;;
esac
done


exec "$@"
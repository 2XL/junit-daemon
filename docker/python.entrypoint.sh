#!/bin/bash
set -eu

function nameko {
    echo "Start nameko service"
    invoke wait-amqp -h='mq' -p=5673 -m ${BROKER_URL}

    # wait until broker url is available
    echo $BROKER_URL

    exec nameko run --config ./nameko.yml workload_generator
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
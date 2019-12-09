#!/bin/bash

IMAGENAME="tp3" # Nome da imagem
CONTAINERNAME="ctp3"    #Nome do container

# build and play
docker build -t $IMAGENAME .
docker run --rm --name $CONTAINERNAME -d $IMAGENAME
docker exec $CONTAINERNAME chmod +x setup.sh 
docker exec $CONTAINERNAME ./setup.sh
docker exec $CONTAINERNAME rm setup.sh
docker exec $IMAGENAME su postgres
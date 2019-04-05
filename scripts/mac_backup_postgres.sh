#!/usr/bin/env bash
CONTAINER=pmp_shield_acp_postgres_1
ONE_DRIVE_FOLDER=/Users/imontilla/OneDrive\ -\ Autoridad\ del\ Canal\ de\ Panama/pmp_shield

CONTAINER_ID=$(docker ps | grep postgres | awk '{print $1;}' | tr -d '\r\n')
FILENAME=$(docker container exec -it $CONTAINER backup | awk '{print $4;}' | tr -d '\r\n')

echo "Backup created $FILENAME"
echo "Container id $CONTAINER_ID"

docker cp $CONTAINER_ID:/backups/$FILENAME ./backups/

if [ "$?" -eq "0" ]
then
    echo "Copied backup $FILENAME to ./backups"
    cp "./backups/$FILENAME" "$ONE_DRIVE_FOLDER/$FILENAME"

    if [ "$?" -eq "0" ]
    then
        echo "Copied backup $FILENAME to $ONE_DRIVE_FOLDER"
    else
        echo "Could not copy file to One Drive ($ONE_DRIVE_FOLDER)"
    fi
else
    echo "Could not copy file"
fi



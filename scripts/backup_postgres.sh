#!/usr/bin/env bash
CONTAINER=pmp_shield_postgres_1
ONE_DRIVE_FOLDER='/c/Users/lberrocal/ONEDRI~1/pmp_shield'


FILENAME=$(docker container exec -it $CONTAINER backup | awk '{print $4;}' | tr -d '\n')

echo "Backup created  $FILENAME"

docker cp $CONTAINER:/backups/$FILENAME ./backups/

if [ "$?" -eq "0" ]
then
    echo "Copied backup $FILENAME to ./backups"
else
    echo "Could not copy file"
fi

cp ./backups/$FILENAME $ONE_DRIVE_FOLDER/$FILENAME

if [ "$?" -eq "0" ]
then
    echo "Copied backup $FILENAME to $ONE_DRIVE_FOLDER"
else
    echo "Could not copy file to One Drive ($ONE_DRIVE_FOLDER)"
fi

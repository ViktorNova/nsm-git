#!/usr/bin/env bash

echo "Usage: stagepatch-gui.sh saveFile pid"
echo "Where saveFile is the aj-snapshot file, and pid is the process ID of the running aj-snapshot instance"

saveFile = $0
pid = $1

echo "Patchbay save file is: $saveFile"
echo "aj-snapshot pid is: $pid"


#!/usr/bin/env bash
echo "Stagepatch GUI"
echo "By Viktor Nova, 2019"
echo "Usage: stagepatch-gui.sh SAVEFILE PID"
echo "Where SAVEFILE is the aj-snapshot file, and PID is the process ID of the running aj-snapshot instance"

SAVEFILE=$1
PID=$2

echo "Patchbay save file is: $SAVEFILE"
echo "aj-snapshot pid is: $PID"

RESPONSE=`echo -e "\
Save JACK and ALSA connections\n\
Save JACK connections only\n\
Save ALSA connections only\n\
Revert to saved patchbay\n\
Disconnect all\n\
Cancel" \
| rofi -dmenu -mesg "Save current JACK/ALSA connections to $SAVEFILE?" \
-theme-str '#prompt { enabled: false; }' -show`

if [ "$RESPONSE" = "Save JACK and ALSA connections" ];
    then
        aj-snapshot -f "$SAVEFILE"
        kill -HUP $PID
elif [ "$RESPONSE" = "Save JACK connections only" ];
    then
        aj-snapshot -j -f "$SAVEFILE"
        kill -HUP $PID
elif [ "$RESPONSE" = "Save ALSA connections only" ];
    then
        aj-snapshot -a -f "$SAVEFILE"
        kill -HUP $PID
elif [ "$RESPONSE" = "Revert to saved patchbay" ];
    then
        aj-snapshot -x
        kill -HUP $PID
elif [ "$RESPONSE" = "Disconnect all" ];
    then
        aj-snapshot -x
else
    echo "Cancelled"
    exit 1
fi

notify-send "$RESPONSE" "DONE!"

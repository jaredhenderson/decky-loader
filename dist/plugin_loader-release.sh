#!/bin/bash

logfile=/tmp/decky-loader-log.txt

USER_DIR="/userdata/system"
HOMEBREW_FOLDER="${USER_DIR}/homebrew"
     
case "$1" in
    start)
        echo "Starting Decky Loader"
        export UNPRIVILEGED_PATH=${HOMEBREW_FOLDER}
        export PRIVILEGED_PATH=${HOMEBREW_FOLDER}
        export LOG_LEVEL=INFO
        cd ${HOMEBREW_FOLDER}/services
        PluginLoader
        ;;
    stop)
        echo "Stopping Decky Loader"
        ;;
    status)
        echo "Decky Loader status"
        ;;
esac

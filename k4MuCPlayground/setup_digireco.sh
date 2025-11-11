
if [ $# -ne 0 ] && [ $# -ne 1 ]; then
    echo "usage: $0 [mucoll-benchmarks]"
    return 1
fi
if [ $# -eq 1 ]; then
    # If a relative path is given, convert to absolute path
    if [[ "$1" != /* ]]; then
        MYBUILD="$(realpath "$1")"
    else
        MYBUILD="$1"
    fi
else
    MYBUILD="$(realpath "mucoll-benchmarks")"
fi

if [ ! -d "${MYBUILD}/reconstruction" ]; then
    echo "Steering File directory ${MYBUILD} does not exist"
    echo "Please correctly provide its path to setup"
else
    export PYTHONPATH="${MYBUILD}/digitization:$PYTHONPATH"
    export PYTHONPATH="${MYBUILD}/reconstruction:$PYTHONPATH"
fi


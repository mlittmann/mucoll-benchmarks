
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
    MYBUILD="$(realpath "build")"
fi

if [ ! -d "${MYBUILD}" ]; then
    echo "Install directory ${MYBUILD} does not exist - creating it..."
    mkdir -p "${MYBUILD}" || { echo "Failed to create ${MYBUILD}"; exit 1; }
fi

export PYTHONPATH="${MYBUILD}/digitization:$PYTHONPATH"
export PYTHONPATH="${MYBUILD}/reconstruction:$PYTHONPATH"

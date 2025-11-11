
if [ $# -gt 2 ]; then
    echo "usage: $0 [mucoll-benchmarks] [Geometry Name]"
    return 1
fi
if [ $# -ge 1 ]; then
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

box_width=46
echo "   ╭──────────────────────────────────────────────╮"
echo "   │    Setting Geometry Environment Variables    │"
echo "   ╰──────────────────────────────────────────────╯"

# Set Environment variables for Geometry
if [ $# -eq 2 ]; then
    GEOM_NAME="$2"
else
    GEOM_NAME="MAIA_v0"
fi
if [[ "$GEOM_NAME" == *MAIA* ]]; then
    GEOM_TYPE="MAIA"
elif [[ "$GEOM_NAME" == *MuSIC* ]]; then
    GEOM_TYPE="MuSIC"
elif [[ "$GEOM_NAME" == *MuColl* ]]; then
    GEOM_TYPE="MuColl"
else
    echo "   ╭──────────────────────────────────────────────╮"
    echo "   │      Unknown geometry type in argument:      │"
    name_len=${#GEOM_NAME}
    pad=$(( (box_width - name_len) / 2 ))
    printf "   │%*s%s%*s│\n" "$pad" "" "$GEOM_NAME" "$((box_width - pad - name_len))" ""
    echo "   │     Must contain MAIA, MuSIC, or MuColl      │"
    echo "   ╰──────────────────────────────────────────────╯"
    return 1
fi

GEO_BASE="/opt/spack/opt/spack"

# MUCOLL_GEO
GEO_DIR=$(find $GEO_BASE/*/*/*/*/linux-x86_64/k4geo*/share/k4geo/MuColl/$GEOM_TYPE/compact/$GEOM_NAME/ 2>/dev/null | head -n 1)
if [ -n "$GEO_DIR" ]; then
    # For MuColl, strip version after '.' for xml file name
    if [[ "$GEOM_TYPE" == "MuColl" ]]; then
        XML_NAME="${GEOM_NAME%%.*}.xml"
    else
        XML_NAME="${GEOM_NAME}.xml"
    fi
    GEO_PATH="$GEO_DIR/$XML_NAME"
    if [ ! -f "$GEO_PATH" ]; then
        GEO_PATH=""
    fi
else
    GEO_PATH=""
fi
if [ ! -f "$GEO_PATH" ]; then
    echo "   ╭──────────────────────────────────────────────╮"
    echo "   │         Geometry file not found for:         │"
    name_len=${#GEOM_NAME}
    pad=$(( (box_width - name_len) / 2 ))
    printf "   │%*s%s%*s│\n" "$pad" "" "$GEOM_NAME" "$((box_width - pad - name_len))" ""
    echo "   ╰──────────────────────────────────────────────╯"
    return 1
fi

# k4ActsTracking Geometry
k4AT_DIR=$(find find $GEO_BASE/*/*/*/*/linux-x86_64/k4actstracking*/share/k4ActsTracking/data/ 2>/dev/null | head -n 1)
if [[ "$GEOM_TYPE" == "MuColl" ]]; then
    START_NAME="${GEOM_NAME%%.*}"
else
    START_NAME="${GEOM_NAME}"
fi
# TGeo
if [ ! -f "$k4AT_DIR/${START_NAME}.root" ]; then
    echo "   ╭──────────────────────────────────────────────╮"
    echo "   │           TGeo file not found for:           │"
    name_len=${#GEOM_NAME}
    pad=$(( (box_width - name_len) / 2 ))
    printf "   │%*s%s%*s│\n" "$pad" "" "$GEOM_NAME" "$((box_width - pad - name_len))" ""
    echo "   ╰──────────────────────────────────────────────╯"
    return 1
fi
# Subdetector JSON
if [ ! -f "$k4AT_DIR/${START_NAME}.json" ]; then
    echo "   ╭──────────────────────────────────────────────╮"
    echo "   │     Subdetector JSON file not found for:     │"
    name_len=${#GEOM_NAME}
    pad=$(( (box_width - name_len) / 2 ))
    printf "   │%*s%s%*s│\n" "$pad" "" "$GEOM_NAME" "$((box_width - pad - name_len))" ""
    echo "   ╰──────────────────────────────────────────────╯"
    return 1
fi

# Set all Environment Variables
if  [[ "$GEOM_TYPE" == "MAIA" ]]; then
    export MUCOLL_MATMAP="$k4AT_DIR/MAIA_v0_material.json"
else
    export MUCOLL_MATMAP="$k4AT_DIR/material-maps.json"
fi
export MUCOLL_GEOM_NAME="$GEOM_NAME"
export MUCOLL_GEO="$GEO_PATH"
export MUCOLL_TGEO="$k4AT_DIR/${START_NAME}.root"
export MUCOLL_TGEO_DESC="$k4AT_DIR/${START_NAME}.json"

# List them out
echo "   ╭──────────────────────────────────────────────╮"
echo "   │      Setting All Environment Variables:      │"
echo "   │  Geo from k4geo, others from k4actstracking  │"
echo "   ├──────────────────────────────────────────────┤"
for var in MUCOLL_GEOM_NAME MUCOLL_GEO MUCOLL_TGEO MUCOLL_MATMAP MUCOLL_TGEO_DESC; do
    value="${!var}"
    # Strip path, keep only filename
    filename="$(basename "$value")"
    line="${var} = ${filename}"
    name_len=${#line}
    pad=$(( (box_width - name_len) / 2 ))
    printf "   │%*s%s%*s│\n" "$pad" "" "$line" "$((box_width - pad - name_len))" ""
done
echo "   ╰──────────────────────────────────────────────╯"
echo ""


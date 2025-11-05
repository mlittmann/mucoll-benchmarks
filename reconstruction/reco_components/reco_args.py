import os
from Gaudi.Configuration import *
from k4FWCore.parseArgs import parser

def get_reco_args():
    """
    Parse command line arguments for the reconstruction steering.
    """
    parser.add_argument(
        "--DD4hepXMLFile",
        help="Compact detector description file",
        type=str,
        default=os.environ.get("MUCOLL_GEO", ""),
    )

    parser.add_argument(
        "--MatFile",
        help="Material maps file for tracking",
        type=str,
        default="/opt/spack/opt/spack/__spack_path_placeholder__/__spack_path_placeholder__/__spack_path_placeholder__/__spack_path_placeholder__/linux-x86_64/k4actstracking-main-etl5olmhzcrfyt44xfj3kmabw5bfnspw/share/ACTSTracking/data/material-maps.json",
    )

    parser.add_argument(
        "--TGeoFile",
        help="TGeometry file for tracking",
        type=str,
        default="/opt/spack/opt/spack/__spack_path_placeholder__/__spack_path_placeholder__/__spack_path_placeholder__/__spack_path_placeholder__/linux-x86_64/k4actstracking-main-etl5olmhzcrfyt44xfj3kmabw5bfnspw/share/ACTSTracking/data/MAIA_v0.root",
    )

    parser.add_argument(
        "--TGeoDescFile",
        help="TGeometry Subdetector JSON file for tracking",
        type=str,
        default="/opt/spack/opt/spack/__spack_path_placeholder__/__spack_path_placeholder__/__spack_path_placeholder__/__spack_path_placeholder__/linux-x86_64/k4actstracking-main-etl5olmhzcrfyt44xfj3kmabw5bfnspw/share/ACTSTracking/data/MAIA_v0.json",
    )

    parser.add_argument(
        "--doTrackPerf",
        help="Run Performance Analysis on Tracking",
        action="store_true",
        default=False
    )

    return parser.parse_known_args()[0]

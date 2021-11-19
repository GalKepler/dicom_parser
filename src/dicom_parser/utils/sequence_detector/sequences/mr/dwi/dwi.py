from dicom_parser.utils.sequence_detector.sequences.mr.dwi.derived import \
    DWI_DERIVED_RULES
from dicom_parser.utils.sequence_detector.sequences.mr.dwi.diffusion import \
    DWI_RULES
from dicom_parser.utils.sequence_detector.sequences.mr.dwi.sbref import \
    DWI_SBREF_RULES

MR_DIFFUSION_SEQUENCES = {
    "dwi": DWI_RULES,
    "dwi_sbref": DWI_SBREF_RULES,
    "dwi_derived": DWI_DERIVED_RULES,
}

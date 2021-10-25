"""
Known sequences defined by the expected (parsed) data element values from the
header.
"""

#: Sequences used in Magnetic Resonance (MR) imaging and their associated
#: definitions.
MR_SEQUENCES = {
    "mprage": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": ("Gradient Recalled", "Inversion Recovery"),
                "lookup": "exact",
            },
            {
                "key": "SequenceVariant",
                "value": ("Segmented k-Space", "Spoiled", "MAG Prepared"),
                "lookup": "exact",
            },
            {
                "key": "ScanOptions",
                "value": ["IR", "WE"],
                "lookup": "in",
            },
        ]
    },
    "t2w": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": {"Spin Echo"},
                "lookup": "exact",
            },
            {
                "key": "SequenceVariant",
                "value": ("Segmented k-Space", "Spoiled"),
                "lookup": "exact",
            },
        ]
    },
    "flair": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": ("Spin Echo", "Inversion Recovery"),
                "lookup": "exact",
            },
            {
                "key": "SequenceVariant",
                "value": ("Segmented k-Space", "Spoiled", "MAG Prepared"),
                "lookup": "exact",
            },
        ]
    },
    "bold": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": {"Echo Planar"},
                "lookup": "exact",
            },
            {
                "key": "ImageType",
                "value": ("ORIGINAL", "PRIMARY", "M", "MB", "ND", "MOSAIC"),
                "lookup": "exact",
            },
        ],
    },
    "func_sbref": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": {"Echo Planar"},
                "lookup": "exact",
            },
            {
                "key": "ImageType",
                "value": ("ORIGINAL", "PRIMARY", "M", "ND", "MOSAIC"),
                "lookup": "exact",
            },
            {
                "key": "ScanOptions",
                "value": ("PFP", "FS"),
                "lookup": "exact",
            },
        ],
    },
    "func_fieldmap": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": {"Echo Planar"},
                "lookup": "exact",
            },
            {
                "key": "SequenceVariant",
                "value": ("Segmented k-Space", "Oversampling Phase"),
                "lookup": "exact",
            },
            {
                "key": "ImageType",
                "value": ("ORIGINAL", "PRIMARY", "M", "ND", "MOSAIC"),
                "lookup": "exact",
            },
            {
                "key": "ScanOptions",
                "value": ("PFP", "FS"),
                "lookup": "exact",
            },
        ],
    },
    "dwi": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": {"Echo Planar"},
                "lookup": "exact",
            },
            {
                "key": "ImageType",
                "value": (
                    "ORIGINAL",
                    "PRIMARY",
                    "DIFFUSION",
                    "NONE",
                    "MB",
                    "ND",
                    "MOSAIC",
                ),
                "lookup": "exact",
            },
            {
                "key": "ScanOptions",
                "value": {"PFP"},
                "lookup": "exact",
            },
        ],
    },
    "dwi_fieldmap": {
        "rules": [
            {
                "key": "ScanningSequence",
                "value": {"Echo Planar"},
                "lookup": "exact",
            },
            {
                "key": "ImageType",
                "value": ("ORIGINAL", "PRIMARY", "M", "ND", "MOSAIC"),
                "lookup": "exact",
            },
            {
                "key": "ScanOptions",
                "value": {"PFP"},
                "lookup": "exact",
            },
        ],
    },
}


#: Known sequences by modality.
SEQUENCES = {"Magnetic Resonance": MR_SEQUENCES}

Machine-readable definitions of iPod hardware and software
===

This repository aims to be the single source of truth for hardware/software
information about the iPod (clickwheel) ecosystem.

The data is kept in Python files as either constants or results of evaluation
pure functions. This can then be used to generate different files in other
formats, or can be consumed by Python-based tools directly.

Databases / Definitions
---

| File            | Info                      |
|-----------------|---------------------------|
| `clockgates.py` | Hardware clock gates      |
| `memmap.py`     | Hardware memory map       |
| `efi.py`        | EFI drivers and protocols |
| `rtxc.py`       | RetailOS RTXC objects     |

API stability
---

Currently _not_ stable and subject to change as we have more findings and
document more devices.

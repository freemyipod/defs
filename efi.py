# Machine-readable documentation of the EFI modules present in iPods.

# All boot components of the iPod firmware are packed in Image1 images. These
# images are designed to be loaded at some implicit address (based on what's
# loading them), and have an entrypoint that starts their execution.
#
# Some of these Image1 boot components are internally laid out as EFI firmware:
#
#  .--------------------------------------------.
#  | Img1 Header                                |
#  | 0x600 or 0x800 bytes, depending on device. |
#  |                                            |
#  | entrypoint --------------------------------------.
#  |============================================|     |
#  |                                            |     |
#  | Interrupt Vectors (0x100 bytes)            |     |
#  |--------------------------------------------|     |
#  | BuildID (0x200 bytes, 0xFF-filled)         |     |
#  |--------------------------------------------|     |
#  | EFI Firmware Volume                        |     |
#  |                                            |     |
#  | .----------------------------------------. |     |
#  | | File (GUID-matched)                    | |     |
#  | | .------------------------------------. | |     |
#  | | | Compressed Section                 | | |     |
#  | | | .--------------------------------. | | |     |
#  | | | | GUID Section (CRC32)           | | | |     |
#  | | | | .----------------------------. | | | |     |
#  | | | | | PE32 Image                 | | | | |     |
#  | | | | | Driver, eg. Lcd.efi        | | | | |     |
#  | | | | '----------------------------' | | | |     |
#  | | | '--------------------------------' | | |     |
#  | | '------------------------------------' | |     |
#  | '----------------------------------------' |     |
#  |                                            |     |
#  |  ... more files here ....                  |     |
#  |                                            |     |
#  | .----------------------------------------. |     |
#  | | File (GUID-matched)                    | |     |
#  | | .------------------------------------. | |     |
#  | | | TE Section                         | | |     |
#  | | | SecCore (loader stub) <----------------------'
#  | | '------------------------------------' | |
#  | '----------------------------------------' |
#  |                                            |
#  |============================================|
#  | Image1 signature, certificates, etc.       |
#  '--------------------------------------------'
#
# These EFI-based components are, for example, the second-stage bootloader
# (loaded from NAND by the bootrom), the diagnostics tool (loaded from NAND by
# the bootloader on demand) or the WTF (loaded over DFU by the bootrom).
#
# The EFI drivers are contained in separate top-level files identified by GUID,
# but also each driver contains a build path that gives it a human-readable
# name.

"""
Maping device generation -> boot component name -> file GUID -> driver name.
"""
efi_drivers = {
    "n5g": {
        "wtf": {
            "98a6-4ef2-8879-7e7daac0ee86": "DxeStatusCode",
            "3f71-4dd6-bd63-0c9840fb758d": "Timer",
            "2063-4919-8002-6d2e0c947e60": "ROMBootValidator",
            "1c73-4747-83d8-06db24d9fb09": "SerialTextInOut",
            "3da4-462c-b201-7c557027a5ba": "Bds",
            "c17f-4dbf-82c3-f90928238e20": "BoardId",
            "a61f-4576-a4fa-19b6df27c772": "DxeD1759",
            "91b6-427f-b512-56851970a5ea": "Lcd",
            "45ca-4902-b188-c9bd64bfee68": "Cpu",
            "69ad-4e13-addb-f52f18fc1a54": "NandReadOnly",
            "c01b-4010-8aea-aa24235c0c97": "SystemConfig",
            "6e34-4f7e-a55c-43c5f2f3a1e2": "InterruptController",
            "b860-4e39-9614-c79685060159": "ClockAndReset",
            "81ab-4d29-827a-d48550b5c69f": "DmaLight",
            "8658-4573-a8aa-a8bd6277360d": "DxeSmbus",
            "4424-46a1-a4be-045294fc2a48": "SoftwareVersion",
            "c07a-4bfe-b121-9d708e3ca073": "Nand",
            "3a57-4529-be43-dfa8c2d33f76": "Restore",
            "37fa-4d06-bd0e-941d5698846a": "RestoreDFU",
            "9815-45a9-80c2-28d1412b498b": "MemoryAllocator",
            "2fad-4f07-a018-8ce939c3e43f": "Variable",
            "c654-4062-82d3-872b4f0e0e8b": "AppleImageValidationManager",
            "8a73-4ff1-98f1-455b97d4d480": "Aes",
            "f449-4669-8c6a-8fb59c441051": "Usb",
            "62d0-4672-aae6-c5313cb12aa6": "Spi",
            "6e7e-45ca-b450-57c046bdfddc": "BmpConvert",
            "841e-491b-8a67-d5fa805841aa": "Prng",
            "93cd-42c2-aa85-d0f892f4a990": "UsbDeviceController",
            "2e14-40c6-86aa-11566f8c479c": "DisplayPlatform",
            "c82a-4992-97c2-2ac01428b070": "PKE",
            "bb45-4a55-9c2b-5834f812fe44": "Sha1",
            "952f-4837-9f0d-2f5fa9f08065": "ChipId",
            "bfbe-4b42-8b25-2a0e95bb437d": "UsbHAL",
            "dc4e-482b-9d2e-d5940cc4897b": "Gpio",
        },
    },
}

# The EFI drivers each register EFI Protocols and load other EFI Protocols. This modularity 

"""
Mapping device generation -> protocol nickname -> (protocol GUID, driver name).

Some drivers register more than one protocol. But currently the list below has
a 1:1 mapping protocol nickname <-> driver name.

We currently assume that for every boot component within a generation the
protocol nickname <-> (protocol GUID, driver name) mapping is constant.
"""
efi_protocols = {
    "n5g": {
        "AES": ("c8906621-cf6f-ae4d-b750-128e4de659da", "Aes"),
        "BDS": ("f63f5e66-cc46-d411-9a38-0090273fc14d", "Bds"),
        "ClockAndReset": ("65306e3a-91cb-b14d-9ae1-d0ee9b990043", "ClockAndReset"),
        "AppleImageValidationManager": ("3909986b-0bc7-794e-b8b5-a6cf0739bc7b", "AppleImageValidationManager"),
        "SystemConfig": ("bdee7fca-5f93-1f4c-b526-446c41360342", "SystemConfig"),
        "ROMBootValidator": ("7d6e5cf2-557f-294f-9246-219d80e6282e", "ROMBootValidator"),
        "RestoreDFU": ("1506464c-224d-894a-8d52-eaf81fe17b29", "RestoreDFU"),
        "MemoryAllocator": ("872e601d-08c7-d34e-964d-dbb0b1462b1d", "MemoryAllocator"),
        "InterruptController": ("8be1280d-a305-8642-8aa7-defe6884bad0", "InterrruptController"),
        "UsbDeviceController": ("f0ab54f3-79e1-e841-87a8-f12a52624a23", "UsbDeviceController"),
        "Cpu": ("b1ccba26-426f-d411-bce7-0080c73c8881", "Cpu"),
        "Sha1": ("f0be64f3-7fc8-c04c-a38d-1fdeef1f3168", "Sha1"),
        "ChipId": ("f21eeedd-49dc-9947-90e6-4b0c8bd36810", "ChipId"),
    },
}

# Each protocol is a 'vtable' with methods. We do not specify the arguments /
# types here, that should be kept in some other format (C header? is there any
# other IDL for EFI protocols?).

efi_protocol_methods = {
    "n5g": {
        # 'Shim' around different validation methods. Currently the only known
        # method is '5', which is ROMBootValidator.
        "AppleImageValidationManager": [
            # Validate an in-memory IMG1 file (calls Validate).
            "ValidateInMemory",
            # Validate an IMG1 retrieved from a Reader (eg. NAND) (calls Validate).
            "ValidateFromReader",
            # Low-level function for validation. Takes a list of validators
            # supported, with either expected kind (5 for ROMBootValidator) or
            # -1 for any. Each validator in the list contains either a pointer
            # to an IMG1 or a pointer to an IMG1 reader.
            "Validate",
        ],

        # Boot device selection. Needs further research.
        "BDS": [
            "Run",
        ],

        # Module to access information form the CHIPID peripheral. Not very
        # well researched, as not much is known about the N5G CHIPID data. This
        # should be researched further.
        "ChipId": [
            # 1 for production devices, 0 for developer devices. Production
            # firmware will refuse to work on developer devices.
            "GetProductionMode",
            "Unk4",
            "Unk8",
            "Unk12",
            # Possibly Chip/Die ID? Concatenated from two registers into a
            # 64-bit value.
            "Unk16",
            "Unk20",
            "Unk24",
        ],

        # Thin shim around standard EFI pool allocator. Provides malloc/free
        # like functionality.
        "MemoryAllocator": [
            "Unk0",
            "Unk4",
            # malloc()-ish.
            "Allocate",
            # malloc()-ish, but panics(?) on allocation failure.
            "MustAllocate",
            # free()-ish.
            "Free",
        ],

        # Implements IMG1 header and body signature/certificate checking and
        # decryption.  Called by AppleImageValidationManager.
        #
        # Pretty much the same logic as the one used in the BootROM, so likely
        # the same codebase.
        #
        # All IMG1 parsed by this code must either ASYMMETRIC or
        # ASYMMETRIC_ENCRYPTED.
        "ROMBootValidator": [
            # Returns '5', used to identify requested validators by
            # AppleImageValidationManager.
            "GetID",
            # Checks an IMG1 header (verifies signature, sizes, etc).
            "CheckHeader",
            # Same as CheckHeader, but from a Reader (eg. NAND).
            "ReadCheckHeader",
            # Checks an IMG1 header (as CheckHeader), but also checks body (ie.
            # certificates/signature) and decrypts it if necessary.
            "CheckHeaderBody",
            # Same as CheckHeaderBody, but from a Reader (eg. NAND).
            "ReadCheckHeaderBody",
        ],
    },
}

if __name__ == '__main__':
    print('= Nano5G EFI =')
    print('{| class="wikitable prettytable sortable"')
    print('|-')
    print('! GUID !! Name || Source !! Function')
    print('|-')
    for module, registrations in efi_protocols['n5g'].items():
        for registration in [registrations]:
            methods = efi_protocol_methods['n5g'].get(registration[1], ["''TODO''"])
            print(f'| rowspan={len(methods)} | {registration[0]} || rowspan={len(methods)} | {registration[1]} || rowspan={len(methods)} | {module}.efi || {methods[0]}')
            for method in methods[1:]:
                print('|-')
                print(f'| {method}')
            print('|-')
    print('|}')


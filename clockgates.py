nano5g_order = [9, 13, 12, 34, 2, 1, 0, 33, 55, 54, 70, 10, 58, 57, 72, 69, 5,
                4, 59, 7, 35, 11, 37, 65, 66, 48, 47, 45, 44, 43, 71, 15, 61,
                60, 62, 32, 67, 64, 36, 31, 51, 53, 63, 8, 16, 46, 42, 41, 40,
                39, 38, 52, 30, 29, 28, 27, 26, 25, 24, 23, 22, 6, 50, 21, 20,
                19, 18, 17, 14, 49, 68, 3, 56]

nano5g_names = [u'ARM-sleep', u'ARM-icu', u'ARM-core', u'VROM', u'DMAC1',
                u'DMAC0', u'TVOUT', u'ECC', u'SDIO', u'AES', u'CEATA', u'FMC',
                u'AMC-core', u'AMC', u'USB-OTG', u'LCD', u'SHA1', u'UART4',
                u'UART3', u'UART2', u'UART1', u'UART0', u'TIMER8', u'TIMER7',
                u'TIMER6', u'TIMER5', u'TIMER4', u'TIMER3', u'TIMER2',
                u'TIMER1', u'TIMER0', u'PL301MPVD', u'MIPI-link', u'AXI-bus',
                u'AMCSS', u'ECID', u'PKE', u'GPIO', u'SPI4', u'SPI3', u'SPI2',
                u'SPI1', u'SPI0', u'IIS2', u'IIS1', u'IIS0', u'SPD', u'IIC1',
                u'IIC0', u'USB2-PHY', u'TW', u'PRNG', u'SWI', u'RINGOSC',
                u'AXI-video', u'AXI-spine', u'XMC', u'CLCD-OTF', u'CLCD',
                u'DMAX', u'MBX-bus', u'MBX-3D', u'MBX-core', u'SCALER',
                u'MPVD', u'H264', u'H264ENC', u'MIXER', u'VP', u'DDR-MIU',
                u'CAMIF', u'JPEG', u'CSIS', u'All']

nano5g_sets = [
    (1048576, 0, 0, 0, 0),
    (65536, 0, 0, 0, 0),
    (32768, 0, 0, 0, 0),
    (8192, 0, 0, 0, 0),
    (4096, 0, 0, 0, 0),
    (2048, 0, 0, 0, 0),
    (1024, 0, 0, 0, 0),
    (512, 0, 0, 0, 0),
    (256, 0, 0, 0, 0),
    (128, 0, 0, 0, 0),
    (64, 0, 0, 0, 0),
    (32, 0, 0, 0, 0),
    (16, 0, 0, 0, 0),
    (8, 0, 0, 0, 0),
    (4, 0, 0, 0, 0),
    (2, 0, 0, 0, 65536),
    (1, 0, 0, 0, 0),
    (0, 0, 256, 0, 67108864),
    (0, 2147483648, 0, 0, 1024),
    (0, 1073741824, 0, 0, 512),
    (0, 536870912, 0, 0, 256),
    (0, 512, 0, 0, 128),
    (0, 0, 64, 0, 8388608),
    (0, 0, 32, 0, 4194304),
    (0, 268435456, 0, 0, 64),
    (0, 134217728, 0, 0, 32),
    (0, 67108864, 0, 0, 16),
    (0, 33554432, 0, 0, 8),
    (0, 16777216, 0, 0, 4),
    (0, 8388608, 0, 0, 2),
    (0, 32, 0, 0, 1),
    (0, 2097152, 0, 0, 0),
    (0, 524288, 0, 0, 0),
    (0, 262144, 0, 0, 0),
    (0, 131072, 0, 0, 0),
    (0, 16384, 0, 0, 0),
    (0, 8192, 0, 0, 0),
    (0, 4096, 0, 0, 0),
    (0, 0, 16, 0, 1048576),
    (0, 0, 2, 0, 524288),
    (0, 32768, 0, 0, 32768),
    (0, 2048, 0, 0, 16384),
    (0, 4, 0, 0, 8192),
    (0, 65536, 0, 0, 0),
    (0, 1024, 0, 0, 0),
    (0, 128, 0, 0, 0),
    (0, 256, 0, 0, 0),
    (0, 64, 0, 0, 4096),
    (0, 16, 0, 0, 2048),
    (0, 8, 0, 0, 0),
    (0, 2, 0, 0, 0),
    (0, 1, 0, 0, 0),
    (0, 0, 4, 0, 2097152),
    (0, 0, 1, 0, 0),
    (0, 0, 0, 16384, 0),
    (0, 0, 0, 8192, 0),
    (0, 0, 0, 4096, 0),
    (0, 0, 0, 1024, 0),
    (0, 0, 0, 512, 0),
    (0, 0, 0, 256, 0),
    (0, 0, 0, 128, 0),
    (0, 0, 0, 64, 0),
    (0, 0, 0, 32, 0),
    (0, 0, 0, 16, 33554432),
    (0, 0, 0, 8, 0),
    (0, 0, 0, 4, 262144),
    (0, 0, 128, 196608, 0),
    (0, 0, 0, 2, 0),
    (0, 0, 0, 1, 0),
    (0, 0, 0, 0, 131072),
    (131072, 0, 0, 32768, 0),
    (524288, 0, 0, 0, 0),
    (262144, 0, 0, 0, 0),
    (2097151, 4287627263, 503, 262143, 134217727),
    (0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0),
    (262144, 524288, 0, 2097152, 4194304),
    (0, 0, 4096, 4096, 4096),
    (8192, 12288, 16384, 20480, 24576),
    (0, 0, 0, 32768, 32768),
]

if __name__ == '__main__':
    for cgs in nano5g_order:
        print("|-")
        print("|", nano5g_names[cgs])
        gates = nano5g_sets[cgs]
        gatenames = []
        bootnums = []
        for gatereg, bits in zip([0,1,4,8,9], gates):
            for bit in range(32):
                mask = 1 << bit
                if (bits & mask) > 0:
                    bootrom = {
                        0: 0,
                        1: 21,
                        4: 53,
                        8: 50,
                        9: 72,
                    }[gatereg] + bit
                    gatenames.append(f"GATE[{gatereg}][{bit}]")
                    bootnums.append(str(bootrom))
                    #print(f"  GATES[{gatereg}][{bit}], bootrom {bootrom}")
        print("|", ', '.join(gatenames))
        print("|", ', '.join(bootnums))

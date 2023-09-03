nano5g = {
    # AHB/AXI
    0x38000000: "sha1",
    0x38100000: "ahb",
    0x38200000: "dmac0",
    0x38300000: "lcdcon",
    0x38400000: "usb",
    0x38400000: "amc", # apple memory controller? per s5l8720/touch2g device tree.
    0x38700000: "dmac0",
    0x38900000: "lcdc",
    0x38c00000: "aes",
    0x38e00000: "vic0",
    0x38e01000: "vic1",
    #0x39660000: # read causes lockup?
    0x39700000: "gpio", # unverified

    # APB
    #0x3c000000: # read causes lockup?
    0x3c100000: "prng",
    0x3c300000: "spi0",
    0x3c400000: "otgphy",
    0x3c500000: "syscon",
    0x3c700000: "timer",
    0x3c800000: "wdt",
    0x3cc00000: "uart0",
    0x3ce00000: "spi1",
    0x3cf00000: "gpio", # unverified
    0x3d100000: "chipid",
    0x3d200000: "spi2", # from n3g aupd
    0x3d500000: "axi",
    0x3d700000: "drex",
    0x3e000000: "miu",
    0x3ff00000: "pl301",
}



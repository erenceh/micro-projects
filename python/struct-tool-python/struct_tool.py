import time
import struct

HEADER_FORMAT = ">HHIHQ"


class PacketHeader:
    def __init__(self, packet_id, packet_type, length, checksum, timestamp):
        self.packet_id = packet_id
        self.packet_type = packet_type
        self.length = length
        self.checksum = checksum
        self.timestamp = timestamp

    def pack(self) -> bytes:
        return struct.pack(
            HEADER_FORMAT,
            self.packet_id,
            self.packet_type,
            self.length,
            self.checksum,
            self.timestamp,
        )

    @classmethod
    def unpack(cls, buffer: bytes) -> "PacketHeader":
        unpacked_header = struct.unpack(HEADER_FORMAT, buffer)
        return PacketHeader(
            unpacked_header[0],
            unpacked_header[1],
            unpacked_header[2],
            unpacked_header[3],
            unpacked_header[4],
        )


if __name__ == "__main__":
    current_time = int(time.time())
    packet_header = PacketHeader(1, 0, 256, 0, current_time)

    print(f"(Before) Packet Header ID: {packet_header.packet_id}")
    print(f"(Before) Packet Header Type: {packet_header.packet_type}")
    print(f"(Before) Packet Header Length: {packet_header.length}")
    print(f"(Before) Packet Header Checksum: {packet_header.checksum}")
    print(f"(Before) Packet Header Timestamp: {packet_header.timestamp}")

    data = packet_header.pack()

    with open("packed.bin", "wb") as f:
        f.write(data)

    with open("packed.bin", "rb") as f:
        read_data = f.read()

    unpacked_header = packet_header.unpack(read_data)

    print(f"(After) Packet Header ID: {unpacked_header.packet_id}")
    print(f"(After) Packet Header Type: {unpacked_header.packet_type}")
    print(f"(After) Packet Header Length: {unpacked_header.length}")
    print(f"(After) Packet Header Checksum: {unpacked_header.checksum}")
    print(f"(After) Packet Header Timestamp: {unpacked_header.timestamp}")

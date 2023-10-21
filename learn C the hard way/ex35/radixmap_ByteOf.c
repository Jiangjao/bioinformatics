#include <stdio.h>
#include <stdint.h>

#define ByteOf(x, y) (((uint8_t *)x)[(y)])


int get_max_bit_uint8(int byte) {
    int max_bit = -1;
    int digit = 0;

    // if (sizeof(byte) == sizeof(uint8_t)) digit = 1
    if (byte == 0) return 0;

    while (byte != 0) {
        byte >>= 8;  // right shift the byte by 1 bit
        max_bit++;
    }

    return max_bit;
}


int main() {
    // uint32_t value = 0x12345678;  // A 32-bit unsigned integer
    uint32_t value = 0x0;  // A 32-bit unsigned integer

    uint8_t byte0 = ByteOf(&value, 0);  // Gets the first byte of the value
    uint8_t byte1 = ByteOf(&value, 1);  // Gets the second byte of the value
    uint8_t byte2 = ByteOf(&value, 2);  // Gets the third byte of the value
    uint8_t byte3 = ByteOf(&value, 3);  // Gets the fourth byte of the value

    printf("Value: %d\n", value);
    printf("Value: 0x%08X\n", value);
    printf("Byte 0: 0x%02X\n", byte0);
    printf("Byte 1: 0x%02X\n", byte1);
    printf("Byte 2: 0x%02X\n", byte2);
    printf("Byte 3: 0x%02X\n", byte3);

    int max_bit = get_max_bit_uint8(value);

    printf("Max Bit: %d\n", max_bit);

    return 0;
}
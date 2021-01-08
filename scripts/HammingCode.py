import logging

class HammingCode:
    input_len = None
    redundant_bit = 0
    def __init__(self, input=None):
        self.logger = logging.getLogger(__name__)
        if input:
            self.input = input
            self.input_len = len(self.input)
            self.redundant_bit = self.calc_no_of_redundant_bits()
        else:
            self.logger.error('No input Found')

    def calc_no_of_redundant_bits(self):
        # Use the formula 2 ^ r >= m + r + 1
        # to calculate the no of redundant bits.
        # Iterate over 0 .. m and return the value
        # that satisfies the equation
        for i in range(self.input_len):
            if (2 ** i >= self.input_len + i + 1):
                return i

    def get_redundant_bits_position(self):
        # Redundancy bits are placed at the positions
        # which correspond to the power of 2.
        j = 0
        k = 1
        res = ''
        # If position is power of 2 then insert '0'
        # Else append the data
        for i in range(1, self.input_len + self.redundant_bit + 1):
            if (i == 2 ** j):
                res = res + '0'
                j += 1
            else:
                res = res + self.input[-1 * k]
                k += 1
        # The result is reversed since positions are
        # counted backwards. (m + r+1 ... 1)
        return res[::-1]


    def calc_parity_bits(self):
        arr = self.get_redundant_bits_position()
        n = len(arr)
        # For finding rth parity bit, iterate over
        # 0 to r - 1
        for i in range(self.redundant_bit):
            val = 0
            for j in range(1, n + 1):
                # If position has 1 in ith significant
                # position then Bitwise OR the array value
                # to find parity bit value.
                if (j & (2 ** i) == (2 ** i)):
                    val = val ^ int(arr[-1 * j])
                    # -1 * j is given since array is reversed
            # String Concatenation
            # (0 to n - 2^r) + parity bit + (n - 2^r + 1 to n)
            arr = arr[:n - (2 ** i)] + str(val) + arr[n - (2 ** i) + 1:]
        return arr


    def detect_error(self, arr):
        n = len(arr)
        res = 0
        # Calculate parity bits again
        for i in range(self.redundant_bit):
            val = 0
            for j in range(1, n + 1):
                if (j & (2 ** i) == (2 ** i)):
                    val = val ^ int(arr[-1 * j])
                    # Create a binary no by appending
            # parity bits together.
            res = res + val * (10 ** i)
            # Convert binary to decimal
        return int(str(res), 2)

'''
data = '1011001'
h = HammingCode(data)
hc = h.calc_parity_bits()
print("Hamming code generated would be:", hc)
print("The position of error  " + str(h.detect_error(hc)))
'''
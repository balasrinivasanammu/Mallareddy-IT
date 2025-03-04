def count_zeros_in_binary(a):

#     negation = a  
    count_ones_in_negation = bin(a).count('1')
   # print(count_ones_in_negation)
    
    total_bits = a.bit_length() # 101
    #print(total_bits)
    count_zeros = total_bits - count_ones_in_negation  
    
    print(2**count_zeros)

# Example usage
a = 35  # Example number
count_zeros_in_binary(a)

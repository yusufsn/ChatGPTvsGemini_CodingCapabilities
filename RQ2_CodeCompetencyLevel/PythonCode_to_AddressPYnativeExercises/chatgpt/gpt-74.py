# Given list
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Calculate the chunk size (length of list divided by 3)
chunk_size = len(sample_list) // 3

# Slice the list into 3 equal chunks
chunk1 = sample_list[:chunk_size]
chunk2 = sample_list[chunk_size:2*chunk_size]
chunk3 = sample_list[2*chunk_size:]

# Reverse each chunk
reversed_chunk1 = chunk1[::-1]
reversed_chunk2 = chunk2[::-1]
reversed_chunk3 = chunk3[::-1]

# Output the chunks and their reversed versions
print("Chunk 1", chunk1)
print("After reversing it", reversed_chunk1)
print("Chunk 2", chunk2)
print("After reversing it", reversed_chunk2)
print("Chunk 3", chunk3)
print("After reversing it", reversed_chunk3)

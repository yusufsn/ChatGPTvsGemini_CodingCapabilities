def slice_and_reverse(sample_list):
  """Slices a list into 3 equal chunks and reverses each chunk.

  Args:
    sample_list: The input list.

  Returns:
    A list of reversed chunks.
  """

  chunk_size = len(sample_list) // 3
  chunks = [sample_list[i:i+chunk_size] for i in range(0, len(sample_list), chunk_size)]

  for chunk in chunks:
    chunk.reverse()

  return chunks

# Example usage
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

reversed_chunks = slice_and_reverse(sample_list)

for i, chunk in enumerate(reversed_chunks):
  print(f"Chunk {i+1}: {chunk}")

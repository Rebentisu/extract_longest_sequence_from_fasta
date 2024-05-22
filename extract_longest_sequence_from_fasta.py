def read_fasta(file_path):
    sequences = {}
    with open(file_path, 'r') as f:
        current_sequence = ''
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_sequence:
                    sequences[header] = current_sequence
                    current_sequence = ''
                header = line[1:]
            else:
                current_sequence += line
        if current_sequence:
            sequences[header] = current_sequence
    return sequences

def find_longest_sequence(sequences):
    max_length = 0
    longest_sequence_header = None
    for header, sequence in sequences.items():
        sequence_length = len(sequence)
        if sequence_length > max_length:
            max_length = sequence_length
            longest_sequence_header = header
    return longest_sequence_header, max_length

if __name__ == "__main__":
    file_path = input("Enter the path to the FASTA file: ")
    sequences = read_fasta(file_path)
    longest_sequence_header, max_length = find_longest_sequence(sequences)
    print("Longest sequence header:", longest_sequence_header)
    print("Length of longest sequence:", max_length)


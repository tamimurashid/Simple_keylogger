# clean_output.py

def clean_keylog(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        output_text = ""
        for line in infile:
            # Extract the key from each line by splitting on ': ' and taking the second part
            if ': ' in line:
                key_data = line.split(': ')[1].strip()
                cleaned_key = key_data.replace("'", "")
                
                # Replace special keys with their respective characters
                if cleaned_key == "Key.space":
                    cleaned_key = " "
                elif cleaned_key == "Key.enter":
                    cleaned_key = "\n"
                elif "Key" in cleaned_key:
                    cleaned_key = ""  # Remove other special keys
                
                output_text += cleaned_key

        outfile.write(output_text)

if __name__ == "__main__":
    input_file = 'keylog.txt'
    output_file = 'cleaned_keylog.txt'
    clean_keylog(input_file, output_file)
    print(f"Cleaned keylog saved to {output_file}")

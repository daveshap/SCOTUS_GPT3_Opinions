import os
import re

def deduplicate_characters(input_folder, output_folder):
    # create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # iterate through all the files in the input folder
    for file in os.listdir(input_folder):
        # skip files with the specified string in the name
        if 'service-ll-usrep-usrep542-usrep542155-usrep542155' not in file:
            continue

        # open the file and read its contents
        with open(os.path.join(input_folder, file), 'r', encoding='utf-8') as f:
            contents = f.read()

        # use regular expressions to remove duplicate characters
        deduped_text = re.sub(r'(.)\1+', r'\1', contents)

        # create the output file path
        output_path = os.path.join(output_folder, file)

        # open the output file and write the deduped text to it
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(deduped_text)

# example usage
deduplicate_characters('chunks_txt', 'deduped_txt')
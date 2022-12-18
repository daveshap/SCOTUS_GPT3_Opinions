import os


def split_text_files(input_folder, output_folder, pages_per_chunk):
    # create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # iterate through all the files in the input folder
    for file in os.listdir(input_folder):
        # open the file and read its contents
        with open(os.path.join(input_folder, file), 'r', encoding='utf-8', errors='ignore') as f:
            contents = f.read()

        # split the contents into a list of pages
        pages = contents.split('NEW PAGE')

        # split the pages into chunks
        for i, chunk in enumerate(range(0, len(pages), pages_per_chunk)):
            # create the output file name and path
            output_file = f'{file.split(".")[0]}_{i+1}.txt'
            output_path = os.path.join(output_folder, output_file)

            # open the output file and write the chunk to it
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write('NEW PAGE'.join(pages[chunk:chunk+pages_per_chunk]))


# example usage
split_text_files('opinions_txt', 'chunks_txt', 3)
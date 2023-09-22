import json
import csv


def jsonl_to_csv(input_filename, output_filename):
    """Convert a JSONL file to CSV."""

    # Open the input file for reading and the output file for writing
    with open(input_filename, 'r', encoding='utf-8') as jsonl_file, \
            open(output_filename, 'w', newline='', encoding='utf-8') as csv_file:

        # Initialize the CSV writer
        csv_writer = None

        # Iterate over each line in the JSONL file
        for line in jsonl_file:
            # Parse the JSON line into a Python dictionary
            data = json.loads(line)

            # If the CSV writer hasn't been initialized yet, do so using the keys of the current JSON object as the header
            if csv_writer is None:
                csv_writer = csv.DictWriter(csv_file, fieldnames=data.keys())
                csv_writer.writeheader()

            # Write the current JSON object to the CSV file
            csv_writer.writerow(data)


if __name__ == '__main__':
    input_file = input("Please enter the path to your JSONL input file: ").strip()
    output_file = input("Please enter the path where you'd like to save the CSV output: ").strip()
    jsonl_to_csv(input_file, output_file)

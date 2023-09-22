
# JSONL to CSV Converter

A simple Python script to convert JSONL (or NDJSON) files to CSV format.

## Description

This script is designed to read each line of a JSONL file (where each line contains a valid JSON object) and write it to a CSV file. It assumes that:

1. Each JSON object in the JSONL file has the same structure, using the keys of the first JSON object as the CSV header.
2. The JSON objects do not have nested objects or arrays. If they do, they will be written to the CSV as string representations.

## Prerequisites

- Python 3.x

## Usage

1. Clone this repository or download the script.
2. Run the script using the command:

   ```bash
   python jsonl_to_csv.py
   ```

3. The script will prompt you to enter the path to the input JSONL file and the desired path for the output CSV file.
4. Follow the prompts, and the script will handle the conversion.

## Limitations

This script is a basic converter and may not handle all edge cases, especially for JSON objects with nested structures or arrays. You may need to further process or flatten the data to fit a CSV format in such cases.

## Contributions

Feel free to submit pull requests or raise issues if you find any bugs or have suggestions for improvements.

---

Copy the above README and place it in the root of your GitHub repository alongside the Python script. This will provide guidance for users or contributors who come across your script on GitHub.
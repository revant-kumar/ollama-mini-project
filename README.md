
# Summarizer

This is a command-line tool that summarizes text content. It can take either a text file or a text string as input and returns the summary of the provided content. The tool leverages the Qwen-2-0.5B language model API for generating summaries.

## Prerequisites

- Python 3.8 or higher
- `requests` library (install via `pip install requests`)
- `argparse` library (included in Python standard library)

## Installation

1. Clone this repository or download the `summarizer.py` script.
2. Ensure you have Python 3.6 or higher installed.
3. Install the `requests` library if not already installed:

    ```bash
    pip install requests
    ```

## Usage

The script can be used to summarize the content of a text file or a direct text string provided via the command line.

### Summarize a Text File

To summarize the content of a text file, use the `-t` or `--textfile` argument followed by the path to the text file:

```bash
python summarizer.py -t path/to/your/file.txt
```

### Summarize a Text String

To summarize a direct text string, use the `-s` or `--string` argument followed by the text string:

```bash
python summarizer.py -s "The quick brown fox jumped over the lazy dog."
```

### Example

Summarize a text file:

```bash
python summarizer.py -t example.txt
```

Summarize a text string:

```bash
python summarizer.py -s "Artificial intelligence is transforming the world."
```

## Script Details

### Functions

- `send_prompt(content)`: Sends the provided content to the Qwen-2 model API to generate a summary.
- `main()`: Parses command-line arguments, reads input (from a file or string), and prints the summary.

### Command-Line Arguments

- `-t` or `--textfile`: Specifies the path to the text file to be summarized.
- `-s` or `--string`: Specifies the text string to be summarized.

### Error Handling

The script includes basic error handling for file not found errors and missing arguments.

## API Configuration

The script is configured to send requests to a local server running at `http://localhost:8000/api/chat`. Ensure the server is running and accessible before using the script.


## Acknowledgments

- The Qwen-2 language model by Alibaba Cloud for text summarization capabilities.

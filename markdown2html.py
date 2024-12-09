#!/usr/bin/python3
"""
Markdown to HTML conversion script with basic argument validation
"""
import sys
import os

def main():
    """
    Main function to convert markdown to HTML
    """
    if len(sys.argv) < 3:
        # Check if the number of arguments is less than 3
        sys.stderr.write('Usahe: ./markdown2html.py README.md README.html\n')
        sys.exit(1)

    # Get input and output file names from cmd line args
    markdown_file = sys.argv[1]
    html_file = sys.argv[2]

    if not os.path.exists(markdown_file):
        # Check if the markdown file exists
        sys.stderr.write(f"Missing {markdown_file}\n")
        sys.exit(1)

        sys.exit(0)

if __name__ == "__main__":
    main()
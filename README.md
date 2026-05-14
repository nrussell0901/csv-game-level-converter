# Game Level CSV-to-JSON Converter

##What this tool does?
Automatically converts game level data from **CSV spreedsheet** to **engine-ready JSON** formats
with one command. Perfect for:

- Tilemap level designs
- Entity/object placement data
- Game configuration tables

##Installation
1. **Requires Python 3.6+**
   Download: [python.org/downloads] or (https://www.python.org/downloads/)

2. **Download the script**
   Place `level_converter.py` in your project folder.

##How to use
##Basic Conversion:
```bash
python level_converter.py input.csv output.json

##Troubleshooting
Error/Solution
-`ImportError: No module named 'csv'`| Use Python 3.6+ (not Python 2) |
-`CSV file has wrong delimiter`| Use `-d` flag (e.g., `-d ";"` for semicolon-delimiter)
-`JSON output empty`| Check CSV headers match sample format |
-`PermissionError`| Run as admin or move files out of protected folders|

**Still Stuck?**
Contact support at [najasimone2003@gmail.com] or vist [https://gumroad.com/help]
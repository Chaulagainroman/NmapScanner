
# Nmap Automate

A simple Python script to automate basic Nmap scanning tasks. This tool allows you to quickly scan a target IP or hostname with customizable port ranges and scan types.

## Features

- Performs Nmap scans using the `python-nmap` library.
- Supports TCP SYN (`-sS`) and UDP (`-sU`) scans.
- Allows custom port ranges.
- Displays scan results including protocol, port state, and service.

## Requirements

- Python 3.x
- `python-nmap` module (wrapper around Nmap)

### Install dependencies

```bash
pip install python-nmap
```

You also need to have **Nmap** installed on your system. You can install it using:

**Ubuntu/Debian:**

```bash
sudo apt install nmap
```

**Windows:**  
Download from [https://nmap.org/download.html](https://nmap.org/download.html) and ensure it's added to your system path.

## Usage

You can run the script either by providing the target via command line or interactively.

### Command Line Example

```bash
python nmap_automate.py 192.168.1.1
```

You will then be prompted for:
- Port range (e.g., `1-1000`, default is `1-1000`)
- Scan type (e.g., `-sS`, `-sU`, default is `-sS`)

### Interactive Example

If no target is passed as an argument:

```bash
python nmap_automate.py
```

You'll be prompted to enter:
- Target IP or hostname
- Port range
- Scan type

## Example Output

```
Scanning 192.168.1.1 on ports 1-1000 with -sS scan...

Protocol: tcp
Port: 22   State: open   Service: ssh
Port: 80   State: open   Service: http
```

## Disclaimer

Use this tool responsibly. Scanning networks without permission is illegal and unethical.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

# Port Scanner

This program is used to scan open ports on a host.

## Requirements

Make sure you have Python 3.x installed on your system.

You also need to install the required Python packages. You can do this by running:

```sh
pip install -r requirements.txt,

edit max_threads=100/200/500/1000 line 13
```

## How to Run

1. Clone this repository (https://github.com/Muhammadkafaby/Port-Scanner.git) or download the `port_scanner.py` file.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `port_scanner.py` file is located.
4. Run the following command:

   ```sh
   python port_scanner.py
   ```

5. Enter the host you want to scan when prompted.
6. Enter the range of ports you want to scan (e.g., 1 to 1024).

The program will scan the ports in the specified range and display the open ports.

## Example

```sh
Enter the host to scan: www.example.com
Enter the start port: 1
Enter the end port: 1024
Enter the number of threads (default 100): 200
Enter the timeout in seconds (default 1): 0.5
Scanning www.example.com from port 1 to 1024 with 200 threads and 0.5 seconds timeout...
Open ports: [80, 443]
```

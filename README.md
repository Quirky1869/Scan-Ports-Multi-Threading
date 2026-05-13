# Scan-Ports-Multi-Threading

![](./_images/tux.png)  

![Static Badge](https://img.shields.io/badge/Version-1.0-lime)
![Static Badge](https://img.shields.io/badge/Python-3.13-blue)
![Static Badge](https://img.shields.io/badge/Multi-Threading-orange)
[![License](https://img.shields.io/github/license/Quirky1869/Scan-Ports-Multi-Threading?color=8A2BE2)](https://github.com/Quirky1869/Scan-Ports-Multi-Threading/blob/python/LICENSE)


## Disclaimer

> [!CAUTION]
Use this script only in an environment that you own or for which you have explicit permission

## Introduction

The `Scan-Ports-Multi-Threading.py` script allows you to scan the ports of a multi-threaded IP address

## Dependencies
> [!IMPORTANT]

> Make sure you have [python](https://www.python.org/downloads/) installed on your PC

## Utilisation

Create a clone of the repository :
```bash
git clone https://github.com/Quirky1869/Scan-Ports-Multi-Threading.git
cd Scan-Ports-Multi-Threading
chmod u+x Scan-Ports-Multi-Threading.py
```

Once in the git directory, you can run the script with :
```bash
./Scan-Ports-Multi-Threading.py <ip-address>
```

## Release

> [!TIP]
A [release](https://github.com/Quirky1869/Scan-Ports-Multi-Threading/releases) is available

Once you have downloaded the release, you can, for example, place it in `/otp` and create a symbolic link to use it from anywhere :
```bash
chmod u+x Scan-Ports-Multi-Threading
mv Scan-Ports-Multi-Threading /otp
ln -s /otp/Scan-Ports-Multi-Threading /usr/local/bin/Scan-Ports-Multi-Threading
```

> [!WARNING]
> Make sure you have the necessary permissions on `/otp/Scan-Ports-Multi-Threading`
> If not, you will need to change the file owner.
> ```bash
> chown $USER:$USER Scan-Ports-Multi-Threading
> ```

## Parameters

Help is available to learn about the possible parameters of the script:
```bash

./Scan-Ports-Multi-Threading.py -h

./Scan-Ports-Multi-Threading.py --help
```

The available parameters are:
```bash

-p, --ports Specifies the port range (format: start-end, e.g., 80-443)
-t, --threads Number of threads to use (default: 500)
-s, --settimeout Timeout in seconds for each connection (default: 0.5)
```

## Examples

Allows you to scan ports from an IP address using default settings (65535 ports scanned):
```bash
./Scan_Ports-Multi-Threading.py 45.86.97.8
```

![tape](./_images/gif/Scan-Ports-Multi-Threading.gif)

Allows you to scan ports 20 to 80 with a thread of 100 from an IP address:
```bash
./Scan_Ports-Multi-Threading.py -p 20-80 -t 100 45.86.97.8
```

Allows you to scan ports 80 to 443 with a timeout of 1 second and a thread of 200 from an IP address:
```bash
./Scan_Ports-Multi-Threading.py -p 80-443 -s 1.0 -t 200 45.86.97.8

This allows you to scan all 65,535 ports with a 2-second timeout and 100 threads for a given IP address:

```bash
./Scan_Ports-Multi-Threading.py --settimeout 2 --threads 100 45.86.97.8
```

# yellowkangaroo
Automated sample collector based on twitter #opendir hashtag written on python3.

## Prerequisites
To be able to run this tool you need to do following steps:
1. Make sure you have **python3**.
2. Clone the repository.
3. Install needed dependencies with pip. Recommended to use virtualenv.<br />
```pip install -r requirements.txt```
4. For best experience and opssec I recommend to use tor.
   * Install required packages. Polipo is proxy which we can use as bridge between scrapy and tor.<br />
    ```sudo apt install tor polipo```
   * Configure pilipo to use tor. Add next line to the file **/etc/polipo/config**.<br />
    ```socksParentProxy = localhost:9050```
   * Restart polipo and make sure tor and polipo are running.<br />
    ```curl https://ipinfo.io/ip```<br />
     With proxy<br />
    ```curl -x http://127.0.0.1:8123 https://ipinfo.io/ip```

## Usage
```python3 yellowkangaroo.py```

## Output example
```Downloading:samples/<malicious IP>/windows-kernel-exploits/MS17-017/ms17-017.jpg
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-034/README.md
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-075/potato.exe
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-034/FillRgn_BSoD.cpp
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-075/ms16-075.rb
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-034/MS16-034-exp.cpp
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-075/img/index.html
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-075/README.md
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-075/Tater.ps1
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-098/win8_1.png
Downloading:samples/<malicious IP>/windows-kernel-exploits/MS16-098/main.c
```

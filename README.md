# Usage

```
dave@18263c1723d3:/frida-gadgetify# ./frida-gadgetify -i ./sleep
You insert data in the section .dynstr whose the size it bigger (664 > 648). It may lead to overaly

Injected binary successfully written to sleep.out!

frida-gadget.so must be in your LD_LIBRARY_PATH.
Example:
LD_LIBRARY_PATH=/home/dave/libs/ ./sleep.out

dave@18263c1723d3:/frida-gadgetify# LD_LIBRARY_PATH=/home/dave/libs/ ./sleep.out
[Frida INFO] Listening on 127.0.0.1 TCP port 27042
```

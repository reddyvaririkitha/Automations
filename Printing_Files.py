import os, sys

''' Doubts about the code:
    - Don't understand the code.
    - Don't know how to print a complete file.
    - May be we have to print text files by looping every line.
    - In case of printer name, may be we have to enter the device location in our system.
    
    Note that:
    - In windows system, only text would be printed
    - But in linux or ios systems, a text file can be printed.
'''


def windows_system_printer(text, printer_name):
    import win32print as w
    p = w.OpenPrinter(printer_name)
    # printer name is the actual name of the printer.
    job = w.StartDocPrinter(p, 1, (text, None, "RAW"))
    w.StartPagePrinter(p)
    w.WritePrinter(p, "data to print")
    w.EndPagePrinter(p)
    # Here "data to print" represents the raw text to send to the printer


def ios_and_linux_system_printer(text, printer_name):
    # ! /usr/bin/python
    os.system(f"lpr -P {printer_name} {text}.txt")
    # "text.txt" is the name of the text file used for printing and will also vary.


def os_selector(system_os, text, p_name):
    if lower(system_os) == 'windows':
        windows_system_printer(text, p_name)
    elif lower(system_os) in ['ios', 'linux']:
        ios_and_linux_system_printer(text, p_name)
    else:
        print("Please connect your device to the printer and print it manually. Thank you!")


# os_selector("windows", "I am happy", "printer_name")
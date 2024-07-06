import os, string

def available_drives():
    available_drives = ['%s:' % d for d in string.ascii_uppercase if os.path.exists('%s:' % d)]
    return available_drives

if __name__ == '__main__':
    print(available_drives())

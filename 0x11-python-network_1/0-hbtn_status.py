#!/usr/bin/python3
""" Script that fetches https://intranet.hbtn.io/status
with the usage of the package urllib"""

if __name__ == "__main__":
    import urllib.request
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as r:
        html = r.read()
        print('Body response:')
        print('    - type: {}'.format(type(html)))
        print('    - content: {}'.format(html))
        print('    - utf8 content: OK')

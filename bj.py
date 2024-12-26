import platform, os, sys
import urllib.request, urllib.parse
import http.cookiejar
import threading
import mechanize
import re

def print_message(x, e=0):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '\033[%s;1m' % str(31 + j))
    x += '\033[0m'
    x = x.replace('!0', '\033[0m')
    if e != 0:
        sys.stdout.write(x)
    else:
        sys.stdout.write(x + '\n')

def install_browser():
    global br
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.set_handle_equiv(True)
    br.set_handle_referer(True)
    br.set_cookiejar(http.cookiejar.LWPCookieJar())
    br.set_handle_redirect(True)
    br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def login():
    us = input('[?] Email/Phone: ')
    pa = input('[?] Password: ')
    print_message('!h[*] Logging in....')
    try:
        br.open('https://m.facebook.com')
        br.select_form(nr=0)
        br.form['email'] = us
        br.form['pass'] = pa
        br.submit()
        url = br.geturl()
        if 'save-device' in url or 'm_sess' in url:
            br.open('https://mobile.facebook.com/home.php')
            name = br.find_link(url_regex='logout.php').text
            name = re.findall(r'(.*a?)', name)[0]
            print_message(f'!h[*] Welcome !k{name}')
            print_message('!h[*] Hope this is your lucky day...')
        elif 'checkpoint' in url:
            print_message('!m[!] Account is at checkpoint\n!k[!]Try logging in with Opera Mini')
        else:
            print_message('!m[!] Login failed')
    except Exception as e:
        print_message(f"Error: {str(e)}")

def inputD(x, v=0):
    while True:
        try:
            a = input(f'\x1b[32;1m{x}\x1b[31;1m:\x1b[33;1m')
        except:
            print_message('\n!m[!] Canceled')
            sys.exit()
        if v:
            if a.upper() in v:
                break
            else:
                print_message('!m[!] Enter a valid option...')
                continue
        else:
            if len(a) == 0:
                print_message('!m[!] Enter a valid input')
                continue
            else:
                break
    return a

def inputM(x, d):
    while True:
        try:
            i = int(inputD(x))
        except:
            print_message('!m[!] Invalid option')
            continue
        if i in d:
            break
        else:
            print_message('!m[!] Invalid option')
    return i

def fetch_group_data():
    try:
        with open('group_ids.txt', 'r') as file:
            group_ids = file.readlines()
        print_message(f'Found {len(group_ids)} group IDs.')
        return group_ids
    except FileNotFoundError:
        print_message('!m[!] File not found: group_ids.txt')
        return []

def main():
    install_browser()
    login()

    group_ids = fetch_group_data()
    if not group_ids:
        print_message('No group data available. Exiting.')
        sys.exit()

    print_message('Proceeding with group ID cracking...')
    # Further operations can be added here for cracking process, if needed.

if __name__ == "__main__":
    main()

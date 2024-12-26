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
    us = input('[?] Email/HP: ')
    pa = input('[?] Kata Sandi: ')
    print_message('!h[*] Sedang Login....')
    try:
        br.open('https://m.facebook.com')
        br.select_form(nr=0)
        br.form['email'] = us
        br.form['pass'] = pa
        br.submit()
        url = br.geturl()
        if 'save-device' in url or 'm_sess' in url:
            br.open('https://mobile.facebook.com/home.php')
            nama = br.find_link(url_regex='logout.php').text
            nama = re.findall(r'(.*a?)', nama)[0]
            print_message(f'!h[*] Selamat datang !k{nama}')
            print_message('!h[*] Semoga ini adalah hari keberuntungan mu...')
        elif 'checkpoint' in url:
            print_message('!m[!] Akun kena checkpoint\n!k[!]Coba Login dengan opera mini')
        else:
            print_message('!m[!] Login Gagal')
    except mechanize.URLError as e:
        print_message(f"Error: URL Error: {str(e)}")
    except mechanize.HTTPError as e:
        print_message(f"Error: HTTP Error: {str(e)}")
    except Exception as e:
        print_message(f"Error: {str(e)}")

def inputD(x, v=0):
    while True:
        try:
            a = input(f'\x1b[32;1m{x}\x1b[31;1m:\x1b[33;1m')
        except KeyboardInterrupt:
            print_message('\n!m[!] Batal')
            sys.exit()
        if v:
            if a.upper() in v:
                break
            else:
                print_message('!m[!] Masukan Opsinya Bro...')
                continue
        else:
            if len(a) == 0:
                print_message('!m[!] Masukan dengan benar')
                continue
            else:
                break
    return a

def inputM(x, d):
    while True:
        try:
            i = int(inputD(x))
        except ValueError:
            print_message('!m[!] Pilihan tidak ada')
            continue
        if i in d:
            break
        else:
            print_message('!m[!] Pilihan tidak ada')
    return i

# Test the functions
install_browser()
login()

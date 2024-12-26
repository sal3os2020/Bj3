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

        # تحقق مما إذا كان المحتوى هو HTML
        content_type = br.response().get_header('Content-Type')
        if 'text/html' not in content_type:
            print_message('!m[!] Konten bukan HTML.')
            return

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

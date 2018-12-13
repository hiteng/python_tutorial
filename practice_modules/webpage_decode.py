


import requests




def web_decoder():


    url = 'http://github.com'
    r = requests.get(url)
    r_html = r.text
    return r_html

    



print web_decoder()
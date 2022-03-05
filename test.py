import json
import uuid

import requests


def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Exceptional"

def download_file(url, store_path):
    r = requests.get(url)
    with open(store_path, "wb") as code:
        code.write(r.content)

if __name__ == "__main__":
    url = "https://s1-cdn.eqxiu.com/eqs/s/page/240572673?code=023je64B&time=1642213964000"
    data = getHTMLText(url)
    # Load JSON string into a dictionary
    json_dicti = json.loads(data)

    # Loop along dictionary keys
    for arr in json_dicti['list']:
        download_file(('https://asset.eqh5.com/' + arr['elements'][0]['properties']['originSrc']),
                      '/Users/vinson/Desktop/images/' + uuid.uuid4().hex + '.jpg')

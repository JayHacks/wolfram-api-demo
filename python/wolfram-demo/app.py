from flask import Flask
from lxml import etree
from io import BytesIO, StringIO
import requests
app = Flask(__name__)

# Put your app ID here
wolfram_app_id = ''
wolfram_base_url = 'http://api.wolframalpha.com/v2/query'

@app.route("/")
def hello():
    payload = { 'input': 'pi', 'appid': wolfram_app_id }
    r = requests.get(wolfram_base_url, params = payload)
    parser = etree.XMLParser(ns_clean=True)
    tree = etree.parse(BytesIO(str.encode(r.text)), parser)
    pods = tree.getroot().findall('pod')

    input_pods = [pod for pod in pods if pod.attrib['title'] == 'Input']
    approximation_pods = [pod for pod in pods if pod.attrib['title'] == 'Decimal approximation']

    input_pod = None
    approximation_pod = None

    if len(input_pods) > 0 and len(approximation_pods) > 0:
        input_image = input_pods[0].find('subpod').find('img')
        approximation_image = approximation_pods[0].find('subpod').find('img')

        html = etree.tostring(input_image).decode("utf-8")\
                + "<p>   =    </p>"\
                + etree.tostring(approximation_image).decode("utf-8")

        return html
    else:
        return "<p> Couldn't parse the XML. :( </p>"


if __name__ == "__main__":
    app.run()

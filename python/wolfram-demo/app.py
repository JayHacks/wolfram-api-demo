from flask import Flask, make_response, render_template, request
app = Flask(__name__)

import wolframalpha

# Enter your Wolfram API app ID here
wolfram_app_id = ''

client = wolframalpha.Client(wolfram_app_id)

@app.route("/")
def hello():
    try:
        query = request.args.get('input', '')
        wolfram_response = client.query(query)
        result = next(wolfram_response.results).text
        return query + " = " + result
    except KeyError as err:
        return render_template('./error.html'), 400
    except Exception as err:
        return render_template('./error.html'), 500

if __name__ == "__main__":
    app.run()

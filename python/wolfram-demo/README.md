# Wolfram API Python Demo

This was written using Python 3.x

First you should get your app ID and copy it into the app.py file.

To get an app ID, visit the Wolfram Developer site: https://developer.wolframalpha.com/portal/signin.html

This line:
```
payload = { 'input': 'pi', 'appid': wolfram_app_id }
```
represents the query parameters for the URL you're building. For example,
with the base URL as `http://api.wolframalpha.com/v2/query`, the above will build out the following URL:

`http://api.wolframalpha.com/v2/query?input=pi&appid=xxxx`


To get started, follow these steps:

1. `$ pyvenv venv`
2. `$ source venv/bin/activate`
3. `$ pip install -r requirements.txt`
4. `$ python app.js`
5. Go to the URL listed in your command prompt. This is where the local server is running.
6. When you're done, `Ctrl + C` and then `$ deactivate`

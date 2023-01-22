from flask import Flask, request, render_template
import redis

app = Flask(__name__)

def_key = '1'
cache = redis.StrictRedis(host='redis', port=6379, db=0)
cache.set(def_key, "one")


@app.route('/', methods=['GET', 'POST'])
def mainpage():

    key = def_key
    if 'key' in request.form:
        key = request.form['key']

    if request.method == 'POST' and request.form['submit'] == 'save':
        cache[key] = request.form['cahce_value']

    cache_value = None
    if key in cache:
        cache_value = cache[key]
    
    return render_template('index.html', key=key, cache_value=cache_value)


if __name__ == '__main__':
    app.run()
from flask import Flask, redirect,  render_template, request, url_for

app = Flask(__name__)

bot = None

def start_app(bot_instance, debug=False):
    global bot
    bot = bot_instance
    app.run(debug=debug, host="0.0.0.0", port=8080)


@app.route('/')
def index():
    return render_template('dashboard.html', bot=bot[0])

@app.route('/prefix', methods=['POST'])
def prefix():
    prefix = request.form['prefix']
    bot[0].command_prefix = prefix
    return redirect(url_for('index'))


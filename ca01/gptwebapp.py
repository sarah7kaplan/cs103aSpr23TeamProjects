'''
gptwebapp shows how to create a web app which ask the user for a prompt
and then sends it to openai's GPT API to get a response. You can use this
as your own GPT interface and not have to go through openai's web pages.

We assume that the APIKEY has been put into the shell environment.
Run this server as follows:

On Mac
% pip3 install openai
% pip3 install flask
% export APIKEY="......."  # in bash
% python3 gptwebapp.py

On Windows:
% pip install openai
% pip install flask
% $env:APIKEY="....." # in powershell
% python gptwebapp.py
'''
from flask import request,redirect,url_for,Flask
from gpt import GPT
import os

app = Flask(__name__)
gptAPI = GPT(os.environ.get('APIKEY'))

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q789789uioujkkljkl...8z\n\xec]/'

@app.route('/')
def index():
    ''' display a link to the general query page '''
    print('processing / route')
    return f'''
        <h1>Team</h1>
        <a href="{url_for('team_index')}">Check out our team!</a>
        <br>
        <h1>About</h1>
        <a href="{url_for('about')}">Check out what we are doing for this project!</a>
        <br>
        <h1>GPT Demo</h1>
        <a href="{url_for('gptdemo')}">Ask questions to GPT</a>
        <br>
        <a href="{url_for('summarization')}">Summarize an article with GPT</a>
        <br>
        <a href="{url_for('Simplification')}">Rewrite a given article with simpler vocabulary</a>
        <br>
        <a href="{url_for('shakespearify')}">Rewrite a given chunk of text in Shakespearean English!</a>
    '''

@app.route('/about')
def about():
    return "Our program specializes in transforming articles into different text types based on prompts \
    specified by the user. For example, we have a tool that summarizes an article to a fewer words \
    based on its main ideas, and another method that rewrites the article while still including \
    all details but with vocabulary a grade-schooler can understand."

    
@app.route('/index')
def team_index():
    '''display an index of team members'''
    return f'''
    <h1>Team Members</h1>
        <a href="{url_for('sarah_kaplan')}">View Sarah Kaplan's bio!</a>
        <br>
        <a href="{url_for('michael_pyrdol')}">View Michael Pyrdol's bio!</a>
        <br>
        <a href="{url_for('xinyi_shang')}">View Xinyi Shang's bio!</a>
        <br>
        <a href="{url_for('james_yu')}">View James Yu's bio!</a>
    '''

@app.route('/sarah_kaplan')
def sarah_kaplan():
    return '''
    <h1>Sarah Kaplan</h1>
    Sarah Kaplan is a junior at Brandeis majoring in Computer Science \
    and minoring in Linguistics. In her free time, she is the treasurer \
    for Hold Thy Peace and the Guitar and Bass Club. In this project, \
    she created the index page, some of the about page, her own bio page, and the \
    Shakespearify method.
    '''

@app.route('/michael_pyrdol')
def michael_pyrdol():
    return "Michael Pyrdol is a junior at Brandeis majoring in Computer Science \
        and minoring in Anthropology. He plays the clarinet in various ensembles \
        on campus, and he is also a music director for Top Score, \
        the student-led orchestra."

@app.route('/xinyi_shang')
def xinyi_shang():
     return '''
    <h1>Xinyi Shang</h1>
    Xinyi Shang is a senior at Brandeis majoing in Biology \
    and minoring in computer science. She enjoys reading and painting when she's free.\
    Definitely a dog person. 
    '''

@app.route('/james_yu')
def james_yu():
     return '''
    <h1>James Yu</h1>
    James Yu is a junior at Brandeis University majoring in Physics and \
    minoring in Computer Science. He likes to listen to and make music with his guitar \
    and cello, and run in his free time. He also likes applying his computer science skills \
    to an on-campus research group in the physics department.
    '''

@app.route('/shakespearify', methods=['GET', 'POST'])
def shakespearify():
    '''send a chunk of text and turn it into iambic pentameter'''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.get_shakespearify(prompt)
        return f'''
        <h1>Shakespearify</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the Shakespearified text in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the Shakespearified text in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('shakespearify')}> make another query?</a>
        '''
    else:
        return '''
        <h1>Shakespearify</h1>
        Enter your text below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="Shakespearify!">
        </form>
        '''

@app.route('/gptdemo', methods=['GET', 'POST'])
def gptdemo():
    ''' handle a get request by sending a form 
        and a post request by returning the GPT response
    '''
    if request.method == 'POST':
        prompt = request.form['prompt']
        answer = gptAPI.getResponse(prompt)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{prompt}</pre>
        <hr>
        Here is the answer in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the answer in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('gptdemo')}> make another query</a>
        '''
    else:
        return '''
        <h1>GPT Demo App</h1>
        Enter your query below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get response">
        </form>
        '''

@app.route('/summarization', methods=['GET', 'POST'])
def summarization():
    #Method: get summarization of an article. 
    ''' handle a get request by sending a form 
        and a post request by returning the GPT summary
    '''
    if request.method == 'POST':
        article = request.form['article']
        summary = gptAPI.get_summarization(article)
        return f'''
        <h1>Summarization Demo</h1>
        <pre style="bgcolor:yellow">{article}</pre>
        <hr>
        Here is the summarys:
        <div style="border:thin solid black">{summary}</div>
        <a href={url_for('summarization')}> summarize another article</a>
        '''
    else:
        return '''
        <h1>Summarization Demo App</h1>
        Enter your article below
        <form method="post">
            <textarea name="article"></textarea>
            <p><input type=submit value="get summary">
        </form>
        '''
@app.route('/Simplification', methods=['GET', 'POST'])
def Simplification():
    ''' handle a get request by sending an article returning the simplified version of text
    '''
    if request.method == 'POST':
        article = request.form['article']
        answer = gptAPI.getSimplification(article)
        return f'''
        <h1>GPT Demo</h1>
        <pre style="bgcolor:yellow">{article}</pre>
        <hr>
        Here is the simplified text in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the simplified text in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('Simplification')}> make another query</a>
        '''
    else:
        return '''
        <h1>Simplification</h1>
        Enter your article below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get simplified article">
        </form>
        '''

@app.route('/rhymification', methods=['GET', 'POST'])
def rhymification():
    '''handle a get request by sending an article returning a poem that rhymes'''
    if request.method == 'POST':
        article = request.form['prompt']
        answer = gptAPI.get_poem(article)
        return f'''
        <h1>Rhymify</h1>
        <pre style="bgcolor:yellow">{article}</pre>
        <hr>
        Here is the rhyming poem text in text mode:
        <div style="border:thin solid black">{answer}</div>
        Here is the rhyming poem text in "pre" mode:
        <pre style="border:thin solid black">{answer}</pre>
        <a href={url_for('rhymify')}> make another query?</a>
        '''
    else:
        return '''
        <h1>Rhymification</h1>
        Enter your text below
        <form method="post">
            <textarea name="prompt"></textarea>
            <p><input type=submit value="get article in the form of a rhyming poem">
        </form>
        '''

if __name__=='__main__':
    # run the code on port 5001, MacOS uses port 5000 for its own service :(
    app.run(debug=True,port=5001)

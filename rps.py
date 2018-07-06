from flask import Flask, render_template, session, redirect, request
from random import randint
app = Flask(__name__)  

app.secret_key = 'ourGame'

@app.route('/')         
def index():

    if 'win' not in session:
        session['win'] = 0
    if 'lose' not in session:
        session['lose'] = 0
    if 'tie' not in session:
        session['tie'] = 0

    win = session['win']
    lose = session['lose']
    tie = session['tie']

    if 'computer' in session:
        print(session)
        computer = session['computer']
        print(computer)
        p1 = session['p1']
        print(p1)
        state = session['state']
        print(state)

    if 'computer' not in session:
        session['computer'] = 'computer I'
    if 'p1' not in session:
        session['p1'] = 'p1 I'
    if 'state' not in session:
        session['state'] = 'state I'

    return render_template('index.html', wins=win, loses=lose, ties=tie, computer=session['computer'], p1=session['p1'], state=session['state'])

@app.route('/process_play', methods=['POST'])
def result():

    game = ['Rock', 'Paper', 'Scissors']
    p2 = randint(0,2)
    computer = game[p2]

    for key in request.form:
        if (key == 'rock'):
            p1 = request.form['rock']
        if (key == 'scissors'):
            p1 = request.form['scissors']
        if (key == 'paper'):
            p1 = request.form['paper']

    print(request.form)

    outcomes = {
        'RockPaper' : 'lose',
        'RockScissors' : 'win',
        'RockRock' : 'tie',
        'PaperRock' : 'win',
        'PaperScissors' : 'lose',
        'PaperPaper' : 'tie',
        'ScissorsPaper' : 'win',
        'ScissorsRock' : 'lose',
        'ScissorsScissors' : 'tie'
    }
    print(p1 + computer)
    print(outcomes[p1 + computer])
    state = outcomes[p1 + computer]

    session['p1'] = p1
    session['computer'] = computer

    session['state'] = state

    session[state] += 1

    return redirect('/')


if __name__=="__main__":

    app.run(debug=True)    
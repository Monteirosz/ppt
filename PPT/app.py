from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = 'cdg'  # Chave secreta para usar sessões

@app.route('/', methods=['GET', 'POST'])
def jogo():
    # Recupera o placar da sessão (se não existir, começa com 0)
    session.setdefault('placar1', 0)
    session.setdefault('placar2', 0)
    
    placar1 = session['placar1']
    placar2 = session['placar2']
    
    resultado = ""
    jogador1_escolha = None
    jogador2_escolha = None

    if request.method == 'POST' and "ver_resultado" in request.form:
        jogador1_escolha = request.form.get('jogador1_escolha')
        jogador2_escolha = request.form.get('jogador2_escolha')

        if jogador1_escolha == jogador2_escolha:
            resultado = "Empate!"
        elif (jogador1_escolha == "pedra" and jogador2_escolha == "tesoura") or \
             (jogador1_escolha == "papel" and jogador2_escolha == "pedra") or \
             (jogador1_escolha == "tesoura" and jogador2_escolha == "papel"):
            resultado = "Jogador 1 venceu!"
            session['placar1'] += 1
        else:
            resultado = "Jogador 2 venceu!"
            session['placar2'] += 1
        
        # Garante que a sessão foi modificada
        session.modified = True

    return render_template("index.html", res=resultado, jogador1_escolha=jogador1_escolha, jogador2_escolha=jogador2_escolha, placar1=session['placar1'], placar2=session['placar2'])

if __name__ == '__main__':
    app.run(debug=True, port=2237)

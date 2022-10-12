import pickle

from flask import Flask, render_template, request

 
app = Flask(__name__)

modelo = pickle.load(open('MDD_Tblinal\models\modelo.pkl','rb'))
 
 
@app.route('/')
def home():
    return render_template('form.html',titulo="Previsão de Rotatividade em Banco")

 
@app.route('/soma/<int:valor>')
def soma(valor):
    return "Resultado: {}".format(valor+5)
 
@app.route('/predicao/<int:v1>/<int:v2>/<int:v3>/<int:v4>/<int:v5>/<int:v6>/<int:v7>/<int:v8>/<int:v9>')
def predicao(v1, v2, v3, v4, v5, v6, v7, v8, v9,):
    resultado = modelo.predict([[v1, v2, v3, v4, v5, v6, v7, v8, v9]])
    return "Classe: {}".format(resultado)
 

# criar uma chamada com método POST
@app.route('/predicao2', methods=['POST'])
def predicao2():
    dados = request.get_json()
    colunas = ["pontuacao_credito", "genero", "idade", "idade_conta", "saldo", "numero_produtos", "cartao_credito", "membro_ativo", "salario_estimado"]
    dados_input = [dados[col] for col in colunas]
    print(dados_input)
    resultado = modelo.predict([dados_input])
    return "Classe: {}".format(resultado)
    
@app.route('/predicaoform',methods=['POST'])
def form():
    pontuacao_credito = request.form['pontuacao_credito']    
    genero  = request.form['genero']
    idade  = request.form['idade']
    idade_conta = request.form['idade_conta']
    saldo = request.form['saldo']
    numero_produtos = request.form['numero_produtos']
    cartao_credito = request.form['cartao_credito']
    membro_ativo = request.form['membro_ativo']
    salario_estimado = request.form['salario_estimado']

    result = modelo.predict([[pontuacao_credito, genero, idade, idade_conta, saldo, numero_produtos, cartao_credito, membro_ativo, salario_estimado]])
    

    
    if result[0]== 1:
        resultado="Cliente deixará o Banco em algum período"
    else:
        resultado="Cliente não deixará o Banco"
 
    return render_template('resultado.html',titulo="Previsão", resultado=resultado)

app.run(debug=True)


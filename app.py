from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('search.html')

@app.route('/result', methods=['GET'])
def result():
    # Collegamento al database
    import pandas as pd
    import pymssql
    import matplotlib.pyplot as plt
    conn = pymssql.connect(server='213.140.22.237\SQLEXPRESS', user='ahmed.nahim', password='xxx123##', database='ahmed.nahim')
    # Invio query al database e ricezioni informazioni
    nomeProdotto = request.args['NomeProdotto']
    query = f"SELECT * FROM production.products WHERE product_name LIKE '{nomeProdotto}%' "
    dfProdotti = pd.read_sql(query,conn)
    # Visualizzare informazioni
    #return render_template('result.html',table = dfProdotti.to_html())
    if request.args['NomeProdotto'] == 'SAAS':
        return render_template('saas.html')
    else:
        return render_template('result.html', nomiColonne = dfProdotti.columns.values, dati = list(dfProdotti.values.tolist()))

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
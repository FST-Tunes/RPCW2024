from flask import Flask, render_template, url_for
from datetime import datetime
import requests

app = Flask(__name__)

#data do sistema em formato ISO
data_hora_atual = datetime.now()
data_iso_formatada = data_hora_atual.strftime('%Y-%m-%dT%H:%M:%S')

#GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/tab_periodica"

@app.route('/')
def index():
    return render_template('index.html', data = {"Data":data_iso_formatada})

@app.route('/elementos')
def elementos():
    sparql_query = """
prefix tp: <http://www.daml.org/2003/01/periodictable/PeriodicTable#>
select * where {
    ?s a tp:Element;
       tp:name ?nome;
       tp:symbol ?simb;
       tp:atomicNumber ?n.

}
order by ?n
"""
    resposta = requests.get(graphdb_endpoint, 
                            params={"query": sparql_query}, 
                            headers={'Accept': 'application/sparql-results+json'})
    if resposta.status_code == 200:
        dados = resposta.json()['results']['bindings']
        return render_template('elementos.html', data = dados)
    else:
        return render_template('empty.html', data = data_iso_formatada)

if __name__ == '__main__':
    app.run(debug=True)

import requests

#GraphDB endpoint
graphdb_endpoint = "http://localhost:7200/repositories/tab_periodica"

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
print(resposta.json())
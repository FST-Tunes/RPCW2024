import json

f = open("escola_musica_clean.json")
bd = json.load(f)
f.close()

ttl = ""

ttl += """
@prefix : <http://rpcw.di.uminho.pt/2024/escola-musica/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xml: <http://www.w3.org/XML/1998/namespace> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@base <http://rpcw.di.uminho.pt/2024/escola-musica/> .

<http://rpcw.di.uminho.pt/2024/escola-musica> rdf:type owl:Ontology .

#################################################################
#    Object Properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/escola-musica#aluno_estuda_curso
:aluno_estuda_curso rdf:type owl:ObjectProperty ;
                    owl:inverseOf :curso_estudado_por_aluno ;
                    rdfs:domain :Aluno ;
                    rdfs:range :Curso .


###  http://rpcw.di.uminho.pt/2024/escola-musica#curso_ensina_instrumento
:curso_ensina_instrumento rdf:type owl:ObjectProperty ;
                          owl:inverseOf :instrumento_ensinado_por_curso ;
                          rdfs:domain :Curso .


###  http://rpcw.di.uminho.pt/2024/escola-musica#curso_estudado_por_aluno
:curso_estudado_por_aluno rdf:type owl:ObjectProperty ;
                          rdfs:domain :Curso .


###  http://rpcw.di.uminho.pt/2024/escola-musica#instrumento_ensinado_por_curso
:instrumento_ensinado_por_curso rdf:type owl:ObjectProperty ;
                                rdfs:domain :Instrumento .


#################################################################
#    Data properties
#################################################################

###  http://rpcw.di.uminho.pt/2024/escola-musica#aluno_ano_curso
:aluno_ano_curso rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Aluno ;
                 rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/escola-musica#aluno_data_nasc
:aluno_data_nasc rdf:type owl:DatatypeProperty ;
                 rdfs:domain :Aluno ;
                 rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/escola-musica#aluno_id
:aluno_id rdf:type owl:DatatypeProperty ;
          rdfs:domain :Aluno ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/escola-musica#aluno_nome
:aluno_nome rdf:type owl:DatatypeProperty ;
            rdfs:domain :Aluno ;
            rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/escola-musica#curso_designacao
:curso_designacao rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Curso ;
                  rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/escola-musica#curso_duracao
:curso_duracao rdf:type owl:DatatypeProperty ;
               rdfs:domain :Curso ;
               rdfs:range xsd:int .


###  http://rpcw.di.uminho.pt/2024/escola-musica#curso_id
:curso_id rdf:type owl:DatatypeProperty ;
          rdfs:domain :Curso ;
          rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/escola-musica#instrumento_id
:instrumento_id rdf:type owl:DatatypeProperty ;
                rdfs:domain :Instrumento ;
                rdfs:range xsd:string .


###  http://rpcw.di.uminho.pt/2024/escola-musica#instrumento_nome
:instrumento_nome rdf:type owl:DatatypeProperty ;
                  rdfs:domain :Instrumento ;
                  rdfs:range xsd:string .


#################################################################
#    Classes
#################################################################

###  http://rpcw.di.uminho.pt/2024/escola-musica#Aluno
:Aluno rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/escola-musica#Curso
:Curso rdf:type owl:Class .


###  http://rpcw.di.uminho.pt/2024/escola-musica#Instrumento
:Instrumento rdf:type owl:Class .


#################################################################
#    Individuals
#################################################################

"""

for aluno in bd["alunos"]:
    registo = (f"""
###  http://rpcw.di.uminho.pt/2024/escola-musica#{aluno["id"]}
:{aluno["id"]} rdf:type owl:NamedIndividual ,
                :Aluno ;
       :aluno_estuda_curso :{aluno["curso"]} ;
       :aluno_ano_curso "{aluno["anoCurso"]}"^^xsd:int ;
       :aluno_data_nasc "{aluno["dataNasc"]}" ;
       :aluno_id "{aluno["id"]}" ;
       :aluno_nome "{aluno["nome"].replace(" ", "_")}" .
       """)
    ttl += registo
    
for curso in bd["cursos"]:
    registo = (f"""
###  http://rpcw.di.uminho.pt/2024/escola-musica#{curso["id"]}
:{curso["id"]} rdf:type owl:NamedIndividual ,
              :Curso ;
     :curso_ensina_instrumento :{curso["instrumento"]["id"]} ;
     :curso_designacao "{curso["designacao"].replace(" ", "_")}" ;
     :curso_duracao "{curso["duracao"]}"^^xsd:int ;
     :curso_id "{curso["id"]}" .
""")
    ttl += registo

for instrumento in bd["instrumentos"]:
    registo = (f"""
###  http://rpcw.di.uminho.pt/2024/escola-musica#{instrumento["id"]}
:{instrumento["id"]} rdf:type owl:NamedIndividual ,
             :Instrumento ;
    :instrumento_id "{instrumento["id"]}" ;
    :instrumento_nome "{instrumento["#text"].replace(" ", "_")}" .
""")
    ttl += registo


with open('output.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)
# TPC2

### Resumo

Após uma primeira análise do dataset, foram encontrados alguns possíveis erros, sendo que alguns dos alunos estavam a frequentar cursos que não existiam. Sendo assim, foi criado o script [`cleaner.py`](cleaner.py), usado para corrigir o campo "curso" nos alunos que frequentavam os cursos "CS1" até ao "CS22", substituindo estes por "CB1" até "CB22". Esta decisão foi feita, pois, por exemplo, o suposto curso "CS1" era para alunos de Clarinete, assim como o curso "CB1", sendo assim estes seriam typos.

## Ontologia

Existem 3 classes, com as seguintes data properties:

 - Aluno:
    - aluno_id
    - aluno_nome
    - aluno_ano_curso
    - aluno_data_nasc

 - Curso: 
    - curso_id
    - curso_designacao
    - curso_duracao

 - Instrumento:
    - instrumento_id
    - instrumento_nome

Foram criadas ainda 4 object properties, cada uma com respetivo domain e range:

 - aluno_estuda_curso: 
    - Domain: Aluno
    - Range: Curso

 - curso_ensina_instrumento: 
    - Domain: Curso
    - Range: Instrumento

 - curso_estudado-por-aluno: Inverso de aluno_estuda_curso

 - instrumento_ensinado_por_curso: Inverso de curso_ensina_instrumento


### Ficheiros

 - [`escola_musica.json`](escola_musica.json): Dados fornecidos pelo professor;

 - [`cleaner.py`](cleaner.py): Scrip para "limpar" os dados em [`escola_musica.json`](escola_musica.json);

 - [`escola_musica_clean.json`](escola_musica_clean.json): Dados depois de corrido o script com o [`cleaner.py`](cleaner.py);

 - [`escola_musica.ttl`](escola_musica.ttl): Estrutura da Ontologia e a exemplo de um indivíduo para cada classe;

 - [`geraTTL.py`](geraTTL.py): Script para povoar a Ontologia com os dados fornecidos e limpos;

 - [`output.ttl`](output.ttl): Ontologia já povoada.
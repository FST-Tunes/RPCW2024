import json

# Load JSON data from file
with open('escola_musica.json', 'r') as file:
    data = json.load(file)

# Mapping of curso replacements
curso_replacements = {
    f"CS{i}": f"CB{i}" for i in range(1, 23)
}

# Iterate over alunos and update curso field
for aluno in data['alunos']:
    curso = aluno['curso']
    if curso in curso_replacements:
        aluno['curso'] = curso_replacements[curso]

# Write updated data back to file
with open('escola_musica_clean.json', 'w') as file:
    json.dump(data, file, indent=4)

print("Data updated successfully.")
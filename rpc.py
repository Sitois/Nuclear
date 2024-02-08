import json

file_name = "./rpc.json"

def read_variable_json(nom_variable):
    global file_name
    try:
        with open(file_name, "r") as file:
            data = json.load(file)

        if nom_variable in data:
            return data[nom_variable]
    except Exception as e:
        print(f"Erreur while trying to read the rpc.json: {e}")
        return None


def edit_variable_json(nom_variable, nouvelle_valeur):
    global file_name
    with open(file_name, "r") as file:
        data = json.load(file)

    if nom_variable in data:
        data[nom_variable] = nouvelle_valeur

        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)
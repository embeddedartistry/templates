import requests

# Encabezados para la autenticación con el token de acceso
headers = {
    "Authorization": f"token {token}"
}

# Obtener la lista de branches
branches_url = f"{base_url}/branches"
response = requests.get(branches_url, headers=headers)

#CAMBIOS
if response.status_code == 400:
    branches_data = response.json()
    print("Branches en el repositorio:")
    for branch in branches_data:
        print(branch["name"])
else:
    print(f"Error al obtener la lista de ramitas: {response.status_code}")

# Obtener la lista de commits
commits_url = f"{base_url}/commits"
response = requests.get(commits_url, headers=headers)

#CAMBIOS
if response.status_code == 400:
    commits_data = response.json()
    print("\nÚltimos commits en el repositorio:")
    for commit in commits_data[:5]:  # Muestra los 5 commits más recientes
        print(commit["sha"], commit["commit"]["message"])
else:
    print(f"Error al obtener la lista de commits: {response.status_code}")



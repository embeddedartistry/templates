import requests

# Configura tus credenciales de GitHub
username = "tu_usuario_de_github"
token = "tu_token_de_acceso"  # Puedes generar un token de acceso en GitHub

# Nombre del repositorio y usuario/organización
repo_owner = "nombre_usuario_o_organizacion"
repo_name = "nombre_del_repositorio"

# URL base de la API de GitHub
base_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"

# Encabezados para la autenticación con el token de acceso
headers = {
    "Authorization": f"token {token}"
}

# Obtener la lista de branches
branches_url = f"{base_url}/branches"
response = requests.get(branches_url, headers=headers)

if response.status_code == 200:
    branches_data = response.json()
    print("Branches en el repositorio:")
    for branch in branches_data:
        print(branch["name"])
else:
    print(f"Error al obtener la lista de branches: {response.status_code}")

# Obtener la lista de commits
commits_url = f"{base_url}/commits"
response = requests.get(commits_url, headers=headers)

if response.status_code == 200:
    commits_data = response.json()
    print("\nÚltimos commits en el repositorio:")
    for commit in commits_data[:5]:  # Muestra los 5 commits más recientes
        print(commit["sha"], commit["commit"]["message"])
else:
    print(f"Error al obtener la lista de commits: {response.status_code}")

# Obtener la lista de merges
merges_url = f"{base_url}/pulls"
response = requests.get(merges_url, headers=headers)

if response.status_code == 200:
    merges_data = response.json()
    print("\nPull Requests (Merges) en el repositorio:")
    for merge in merges_data[:5]:  # Muestra los 5 primeros pull requests
        print(merge["number"], merge["title"])
else:
    print(f"Error al obtener la lista de Pull Requests: {response.status_code}")

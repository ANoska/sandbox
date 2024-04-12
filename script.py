from git import Repo

repo_url = 'https://github.com/ANoska/sandbox.git'
repo_abs_path = '{placeholder}'
branch_name = 'fix/junit-upgrade'
commit_message = 'Upgrade junit version'

input_file_abs_path = '{placeholder}'
output_file_abs_path = '{placeholder}'
output_file_rel_path = 'pom.xml'

sandbox_repo = Repo.clone_from(repo_url, repo_abs_path)

sandbox_repo.create_head(branch_name)
sandbox_repo.git.checkout(branch_name)

with open(input_file_abs_path, 'r') as file:
    lines = file.readlines()

with open(output_file_abs_path, 'w') as file:
    file.writelines(lines)

sandbox_repo.index.add([output_file_rel_path])
sandbox_repo.index.commit(commit_message)

origin = sandbox_repo.remote(name='origin')
origin.push(branch_name)

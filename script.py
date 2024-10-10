import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e.stderr.strip()}")
        exit(1)

def rename_and_push_branch():
    # Check if the current branch is ui-enhancement
    current_branch = run_command(['git', 'branch', '--show-current'])
    if current_branch != 'ui-enhancement':
        print(f"Error: Not on 'ui-enhancement' branch. You are on '{current_branch}' branch.")
        return

    # Rename the branch to ui-redesign
    print("Renaming branch to 'ui-redesign'...")
    run_command(['git', 'branch', '-m', 'ui-redesign'])

    # Push the new branch to the remote repository and delete the old one
    print("Pushing 'ui-redesign' to remote and deleting 'ui-enhancement'...")
    run_command(['git', 'push', 'origin', 'ui-redesign'])
    run_command(['git', 'push', 'origin', '--delete', 'ui-enhancement'])

    print("Branch renamed and pushed successfully.")

if __name__ == "__main__":
    rename_and_push_branch()
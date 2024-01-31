print("\n\n------------------ INITIATE GITTING ------------------\n")

# Import required modules
import subprocess
import sys

# Define function for running git commands.
def runGit(command):
    try:
        result = subprocess.run(command, check=True, text=True, capture_output=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running git command: {e}")
        return None

# Initial check of git status.
git_status = runGit(["git", "status"])
print("\nMESSAGE\n" + "From command 'git status':\n" + git_status)
print()
print("------------------------------------------------------")

# INPUT SECTION: Selection of program, for whether to perform step-by-step or automated cycles.
print('INSTRUCTIONS:\n- Gitting can perform pre-set programs for \n  synchronizing with your Git repository.\n- Git messages are checked and printed for every step \n  and after completion if verification or \n  troubleshooting is needed.\n- If you want to select the precise actions and \n  verify git status, select the stepwise program ("1").\n- If you are confident about the changes and the \n  script you can use an automated cycle.\n- Program "2" performs steps: add, commit, and push. \n  Program "3" also does a pull beforehand. \n  These require manual naming of the commit.\n- In a hurry? Use "q" or "Q" for a quick program, \n  it will be named "Quick commit".\n\nThe git commands run by this script include: \n- status\n- branch -vv\n- pull\n- add.\n- commit -m "[name]"\n- push\n\n')
actionCue = input("Select procedure for synchronizing Git:\n   1) Stepwise procedure\n   2) Add-to-push\n   3) Full pull'n'push\n   q) QUICK PROGRAM (automatic naming)\n   Exit: any other key\n   Selection:")
print()


# Response for 3: initial push.
if actionCue == "3":
    print("\n- PULLING")
    git_pull = runGit(["git", "pull", "origin", "main"])
    print("\nMESSAGE\n" + "From command 'git pull':\n" + git_pull)


# Response program for automated cycles (2, 3, and q/Q).
automatedAction = ("2", "3", "q", "Q")  # List of accepted selection input for program.
if actionCue in automatedAction:
    print("\n- ADDING CHANGES")
    git_add = runGit(["git", "add", "."])
    print("\n- COMMITTING CHANGES")
    if actionCue == "q" or actionCue == "Q":    # Automated naming of commit for quick program.
        commitName = "Quick commit"
    else:
        commitName = input("Name commit: ")     # INPUT SECTION: Manual naming.
    git_commit = runGit(["git", "commit", "-m", commitName])
    print("\nMESSAGE\n" + "From command 'git commit':\n" + git_commit)
    print("\n- PUSHING CHANGES\n")
    git_push = runGit(["git", "push", "origin", "main"])
    print("\nMESSAGE\n" + "From command 'git push':\n" + git_push)
    print("\n- SYSTEM STATUS")
    git_status = runGit(["git", "status"])
    print("\nMESSAGE\n" + "From command 'git status':\n" + git_status)
    git_upstream = runGit(["git", "branch", "-vv"])
    print("\nMESSAGE\n" + "From command 'git upstream':\n" + git_upstream, "\n")
    print("DONE")
    print("\n------------------ END GITTING ------------------\n\n")
    sys.exit()
elif actionCue == "1":  # Response for 1 (stepwise procedure), i.e. skip cycle.
    pass
else:   # Response for invalid entry .
    print("\n------------------ GITTING EXITED ------------------\n\n")
    sys.exit()
print("------------------------------------------------------")


# Response steps for 1 (stepwise procedure).
# Pull
pullCue = input("Execute pull?\n   1) Yes\n   2) No\n   Else) Exit\n   Selection:")     # INPUT SECTION: do or don't perform "pull".
if pullCue == "1":
    git_pull = runGit(["git", "pull", "origin", "main"])
    print(git_pull)
    git_status = runGit(["git", "status"])
    print(git_status)
elif pullCue == "2":
    print("Pull not performed.")
else:
    print("\n------------------ GITTING EXITED ------------------\n\n")
    sys.exit()
print("------------------------------------------------------")


# Add
if "Untracked files" in git_status or "Changes not staged for commit" in git_status:
    print("Untracked or changed files: Yes")
    print()
    print("FILE DETAILS:")
    print("\nMESSAGE\n" + "From command 'git status':\n" + git_status)
    print()
    addCue = input("Add changes?\n   1) Yes\n   2) No\n   Else) Exit\n   Selection:")   # INPUT SECTION: do or don't perform "add".
    if addCue == "1":
        git_add = runGit(["git", "add", "."])
        print("------------------------------------------------------")
    elif addCue == "2":
        print("Changes not added.")
    else:
        print("\n------------------ GITTING EXITED ------------------\n\n")
        sys.exit()
else:
    print("Untracked or changed files: No")
git_status = runGit(["git", "status"])


# Commit
if "Changes to be committed" in git_status:
    print("Non-committed changes: Yes")
    print()
    print("ADDED CHANGES:")
    print("\nMESSAGE\n" + "From command 'git status':\n" + git_status, "\n")
    commitCue = input("Commit changes?\n   1) Yes\n   2) No\n   Else) Exit\n   Selection:")     # INPUT SECTION: do or don't perform "commit".
    if commitCue == "1":
        commitName = input("Name commit: ")                                                     # INPUT SECTION: Manual naming.
        git_commit = runGit(["git", "commit", "-m", commitName])
        print("\nMESSAGE\n" + "From command 'git commit':\n" + git_commit)
        print("------------------------------------------------------")
    elif commitCue == "2":
        print("Changes not committed.")
    else:
        print("\n------------------ GITTING EXITED ------------------\n\n")
        sys.exit()
else:
    print("Non-committed changes: No")
    commitCue = "n"
git_status = runGit(["git", "status"])


# Push
git_upstream = runGit(["git", "branch", "-vv"])
if "ahead" in git_upstream:
    print("Files to push: Yes")
    print()
    print("COMMITTED CHANGES:")
    print("\nMESSAGE\n" + "From command 'git status':\n" + git_status, "\n")
    pushCue = input("Push files?\n   1) Yes\n   2) No\n   Else) Exit\n   Selection:")       # INPUT SECTION: do or don't perform "push".
    if pushCue == "1":
        git_push = runGit(["git", "push", "origin", "main"])
        print("\nMESSAGE\n" + "From command 'git push':\n" + git_push)
        print("------------------------------------------------------")
    elif pushCue == "2":
        print("Files not pushed.")
    else:
        print("\n------------------ GITTING EXITED ------------------\n\n")
        sys.exit()
else:
    print("Files to push: No\n")


# Final status check
git_status = runGit(["git", "status"])
print("\nMESSAGE\n" + "From command 'git status':\n" + git_status)
print()
print("DONE")
print("\n------------------ END GITTING ------------------\n\n")

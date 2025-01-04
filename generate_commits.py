import git
import random
import datetime
import os

def generate_random_commits(repo_path, num_commits=200):
    """Generate random commits throughout 2025"""
    
    # Initialize the repository
    repo = git.Repo(repo_path)
    
    # Define date range for 2025
    start_date = datetime.datetime(2025, 1, 1, 0, 0, 0)
    end_date = datetime.datetime(2025, 12, 31, 23, 59, 59)
    
    # Generate random timestamps throughout 2025
    timestamps = []
    for _ in range(num_commits):
        random_timestamp = start_date + datetime.timedelta(
            seconds=random.randint(0, int((end_date - start_date).total_seconds()))
        )
        timestamps.append(random_timestamp)
    
    # Sort timestamps to maintain chronological order
    timestamps.sort()
    
    # Commit messages pool
    commit_messages = [
        "Update calculator functionality",
        "Fix bug in register handling",
        "Improve error handling",
        "Refactor code structure",
        "Add validation checks",
        "Optimize performance",
        "Update documentation",
        "Clean up code",
        "Enhance user interface",
        "Fix division error",
        "Add new features",
        "Update binary reader",
        "Improve register management",
        "Fix index overflow",
        "Add comments",
        "Update method signatures",
        "Refactor display logic",
        "Improve calculation accuracy",
        "Fix history tracking",
        "Update instruction parsing",
        "Add error messages",
        "Improve code readability",
        "Fix register overflow",
        "Update function codes",
        "Enhance calculator features",
    ]
    
    print(f"Generating {num_commits} commits throughout 2025...")
    
    for i, timestamp in enumerate(timestamps):
        # Make a random change to the file
        change_type = random.choice(['comment', 'whitespace', 'print', 'variable'])
        
        with open(os.path.join(repo_path, 'main.py'), 'r') as f:
            content = f.read()
        
        # Apply random changes
        if change_type == 'comment':
            # Add a random comment
            comment_line = random.randint(1, len(content.split('\n')))
            lines = content.split('\n')
            lines.insert(comment_line, f"# Random update {random.randint(1000, 9999)}")
            content = '\n'.join(lines)
        elif change_type == 'whitespace':
            # Add or remove a blank line
            lines = content.split('\n')
            target_line = random.randint(1, len(lines) - 1)
            if random.choice([True, False]) and lines[target_line].strip():
                lines.insert(target_line, '')
            content = '\n'.join(lines)
        elif change_type == 'print':
            # Add a debug print somewhere
            lines = content.split('\n')
            target_line = random.randint(1, len(lines) - 1)
            indent = len(lines[target_line]) - len(lines[target_line].lstrip())
            lines.insert(target_line, ' ' * indent + f"# Debug: {random.randint(100, 999)}")
            content = '\n'.join(lines)
        elif change_type == 'variable':
            # Just add a comment that mentions a variable update
            lines = content.split('\n')
            target_line = random.randint(1, len(lines) - 1)
            lines.insert(target_line, f"# Update {random.randint(1, 100)}")
            content = '\n'.join(lines)
        
        # Write the modified content
        with open(os.path.join(repo_path, 'main.py'), 'w') as f:
            f.write(content)
        
        # Stage the changes
        repo.index.add(['main.py'])
        
        # Create commit with backdated timestamp
        commit_message = random.choice(commit_messages)
        date_string = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        # Set environment variables for git commit date
        env = os.environ.copy()
        env['GIT_AUTHOR_DATE'] = date_string
        env['GIT_COMMITTER_DATE'] = date_string
        
        # Commit with custom date
        repo.index.commit(
            commit_message,
            author_date=date_string,
            commit_date=date_string
        )
        
        if (i + 1) % 20 == 0:
            print(f"Progress: {i + 1}/{num_commits} commits created")
    
    print(f"\nSuccessfully created {num_commits} commits!")
    print("Note: You may need to force push to update remote repository:")
    print("  git push --force origin master")

if __name__ == "__main__":
    repo_path = r"R:\TrialWork\mips_calculator"
    generate_random_commits(repo_path, 200)


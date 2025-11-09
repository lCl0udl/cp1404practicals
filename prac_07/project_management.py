
from project import Project
from datetime import datetime


MENU = """
- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date  
- (A)dd new project  
- (U)pdate project  
- (Q)uit
"""


def main():
    """Manage projects using menu-driven interface."""
    filename = "projects.txt"
    projects = load_projects(filename)
    print(f"Loaded {len(projects)} projects from {filename}")

    while True:
        print(MENU)
        choice = input(">>> ").strip().upper()

        if choice == "L":
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")

        elif choice == "S":
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
            print(f"Projects saved to {filename}")

        elif choice == "D":
            display_projects(projects)

        elif choice == "F":
            filter_projects_by_date(projects)

        elif choice == "A":
            add_project(projects)

        elif choice == "U":
            update_project(projects)

        elif choice == "Q":
            save_choice = input("Save to default file before quitting? (Y/N): ").strip().upper()
            if save_choice == "Y":
                save_projects("projects.txt", projects)
                print("Projects saved. Goodbye!")
            else:
                print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


def load_projects(filename):
    """Load projects from a tab-delimited file."""
    projects = []
    with open(filename, "r") as in_file:
        in_file.readline()  # Skip header
        for line in in_file:
            parts = line.strip().split('\t')
            if len(parts) == 5:
                name, start_date, priority, cost, completion = parts
                projects.append(Project(name, start_date, priority, cost, completion))
    return projects


def save_projects(filename, projects):
    """Save all projects to a tab-delimited file."""
    with open(filename, "w") as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                  f"{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display incomplete and completed projects separately, sorted by priority."""
    incomplete = sorted([p for p in projects if not p.is_complete()])
    complete = sorted([p for p in projects if p.is_complete()])

    print("Incomplete projects:")
    for p in incomplete:
        print(f"  {p}")

    print("Completed projects:")
    for p in complete:
        print(f"  {p}")


def filter_projects_by_date(projects):
    """Display projects that start after a given date."""
    date_str = input("Show projects that start after date (dd/mm/yyyy): ")
    filter_date = datetime.strptime(date_str, "%d/%m/%Y").date()
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=lambda p: p.start_date)

    print(f"Projects starting after {filter_date}:")
    for p in filtered:
        print(f"  {p}")


def add_project(projects):
    """Add a new project from user input."""
    print("Let's add a new project:")
    name = input("Name: ").strip()
    start_date = input("Start date (dd/mm/yyyy): ").strip()
    priority = int(input("Priority: "))
    cost = float(input("Cost estimate: "))
    completion = int(input("Percent complete: "))
    projects.append(Project(name, start_date, priority, cost, completion))


def update_project(projects):
    """Update an existing project's completion and/or priority."""
    display_projects(projects)
    index = int(input("Project choice (number): ")) - 1
    if 0 <= index < len(projects):
        project = projects[index]
        print(f"Selected: {project}")

        new_completion = input("New completion percentage (leave blank to keep current): ")
        new_priority = input("New priority (leave blank to keep current): ")

        if new_completion:
            project.completion_percentage = int(new_completion)
        if new_priority:
            project.priority = int(new_priority)
        print("Project updated.")
    else:
        print("Invalid project number.")


if __name__ == "__main__":
    main()

arch_name = input()
projects = int(input())


def information_project(architech, proj):
    print(f"The architect {architech} will need {3 * proj} hours to complete "
          f"{proj} project/s.")


information_project(arch_name, projects)

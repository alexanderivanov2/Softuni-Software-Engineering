class Company {
    // Departments stored employees for  depatment.
    depatments = {};
    // departmentsSalaryInfo store total salary average salary and employees for depatment.
    departmentsSalaryInfo = []

    addEmployee(name, salary, position, department) {
        const employeeInput = [name, salary, position, department];
        this.checkParametersForEmptyString(employeeInput);
        this.checkSalary(salary);
        const newEmployee = this.createEmployee(employeeInput);
        this.addToDepartments(newEmployee, department);
        this.addToDepartmentsSalaryInfo(newEmployee, department);

        return `New employee is hired. Name: ${name}. Position: ${position}`
    }

    checkParametersForEmptyString(parameters) {
        parameters.forEach(parameter => {
            if (parameter === '' || parameter === undefined || parameter === null) {
                throw new Error('Invalid input!');
            }
        });
    }

    checkSalary(salary) {
        if (salary < 0) {
            throw new Error('Invalid input!');
        }
    }

    createEmployee(employeeInput) {
        const [name, salary, position] = employeeInput;
        const employee = {
            name: name,
            salary: salary,
            position: position
        }
        return employee;
    }

    addToDepartments(employee, department) {
        if (this.depatments.hasOwnProperty(department)) {
            this.depatments[department].push(employee);
        } else {
            this.depatments[department] = [employee];
        }
    }

    addToDepartmentsSalaryInfo(employee, department) {
        if (!this.departmentsSalaryInfo.hasOwnProperty(department)) {
            this.departmentsSalaryInfo[department] = {
                totalSalary: 0,
                averageSalary: 0,
                size: 0
            }
        }
            
            this.departmentsSalaryInfo[department].totalSalary += employee.salary;
            this.departmentsSalaryInfo[department].size += 1;
            this.departmentsSalaryInfo[department].averageSalary = this.departmentsSalaryInfo[department].totalSalary / this.departmentsSalaryInfo[department].size;
    }

    bestDepartment() {
        const result = []; 
        const bestAvgSalaryDepartment = this.findBestAvgSalaryDepartment(); 
        result.push(`Best Department is: ${bestAvgSalaryDepartment}`);
        result.push(`Average salary: ${this.departmentsSalaryInfo[bestAvgSalaryDepartment].averageSalary.toFixed(2)}`);
        const sortedEmployees = this.sortEmployeesBySalaryAndName(this.depatments[bestAvgSalaryDepartment]);
        sortedEmployees.forEach(({name, salary, position}) => {
            result.push(`${name} ${salary} ${position}`);
        })
        return result.join('\n');
    }

    findBestAvgSalaryDepartment() {
        const bestAvgSalary = Object.keys(this.departmentsSalaryInfo).sort((dep1, dep2) => this.departmentsSalaryInfo[dep2].averageSalary - this.departmentsSalaryInfo[dep1].averageSalary);
        
        return bestAvgSalary[0];
    }

    sortEmployeesBySalaryAndName(department) {
        const sortDepartmentEmployees = department.sort((emp1, emp2) => {
            if(emp2.salary > emp1.salary) {
                return 1;
            } else if (emp1.salary > emp2.salary) {
                return -1;
            } else {
                return emp1.name.localeCompare(emp2.name);
            }
        });

        return sortDepartmentEmployees;
    }
}


let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer","Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
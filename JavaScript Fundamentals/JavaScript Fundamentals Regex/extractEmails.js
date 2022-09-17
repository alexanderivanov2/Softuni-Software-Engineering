function solve(input) {
    let pattern = /(?<user>^|(?<=\s)[A-Za-z\d]+([\.\-_]*[A-Za-z\d]+)*)@(?<host>[A-Za-z]+(\-[A-Za-z]+)*(\.[a-z]+)+)(?:\b|(?=\s))/g;

    let match = pattern.exec(input);

    while (match !== null) {
        console.log(match[0]);
        match = pattern.exec(input);
    }

}

solve('Just send email to s.miller@mit.edu and j.hopking@york.ac.uk for more information.');
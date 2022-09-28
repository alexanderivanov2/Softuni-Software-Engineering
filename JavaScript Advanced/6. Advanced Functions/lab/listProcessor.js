function listProcessor(commands) {
    result = [];
    function processor() {
        for (let command of commands) {
            let [process, str] = command.split(' ');
            if (process == 'add') {
                result.push(str);
            } else if (process == 'remove') {
                let filter = result.filter(x => x != str);
                result = filter;
            } else if (process == 'print') {
                console.log(result.join(','))
            }
        }
    }
    processor();
}

listProcessor(['add hello', 'add again', 'remove hello', 'add again', 'print']);

listProcessor(['add pesho', 'add george', 'add peter', 'remove peter','print']);
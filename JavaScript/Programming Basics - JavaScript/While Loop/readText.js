function readWords(input){
    let i = 0;
    let command = input[1];
    while(command !== 'Stop'){
        console.log(command);
        i++;
        command = input[i];
    }
}

readWords(["Nakov",
"SoftUni",
"Sofia",
"Bulgaria",
"SomeText",
"Stop",
"AfterStop",
"Europe",
"HelloWorld"]);
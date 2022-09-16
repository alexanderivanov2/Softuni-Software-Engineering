function solve(directory) {
    let lastIndex = directory.lastIndexOf('\\');
    let [name, ...extension] = directory.slice(lastIndex + 1).split('.');
    if (extension.length > 1) { 
        lastExtension = extension.pop();
        name += '.' + extension.join('.');
        console.log(`File name: ${name}\nFile extension: ${lastExtension}`);
    } else {
        console.log(`File name: ${name}\nFile extension: ${extension}`);
    }
}

solve('C:\\Internal\\training-internal\\Template.bag.pptx');
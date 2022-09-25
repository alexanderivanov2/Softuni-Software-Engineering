function colorize() {
    let trElements = document.querySelectorAll('tr:nth-child(even)');
    for (let tr of trElements) {
        tr.style.background = "Teal"
    } 
}
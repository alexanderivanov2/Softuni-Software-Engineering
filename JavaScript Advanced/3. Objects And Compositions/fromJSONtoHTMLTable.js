function fromJSONToHTMLTable(input){
    function makeKeyRow(convertInput) {
        let row = "    <tr>";
        for (let key in convertInput[0]) {
            row += `<th>${escapeHtml(key)}</th>`;
        }
        row += "</tr>";
        result.push(row);
    }

    function makeKeyRowValue(convertInput) {
        
        for (let el of convertInput) {
            let rowValue = "    <tr>";
            for (key in el) {
                rowValue += `<td>${escapeHtml(el[key])}</td>`;
            }
            rowValue += "</tr>";
            result.push(rowValue);
        }
    }

    function escapeHtml(str) {
        // html escape from Underscore.js https://coderwall.com/p/ostduq/escape-html-with-javascript
        // let entityMap = {
        //     '&': '&amp;',
        //     '<': '&lt;',
        //     '>': '&gt;',
        //     '"': '&quot;',
        //     '\'': '&#39;',
        //     '/': '&#x2F;'
        // };
        // return str.toString().replace(/[&<>"'\/]/g, (s) => entityMap[s]);
        return str
            .toString()
            .replace(/&/g, '&amp;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;');
    }

    let convertInput = JSON.parse(input);
    let result = ["<table>"]
    makeKeyRow(convertInput);
    makeKeyRowValue(convertInput);
    result.push("</table>");

    console.log(result.join("\n"));
}


// <table>
//    <tr><th>Name</th><th>Score</th><th>Grade</th></tr>
//    <tr><td>Pesho</td><td>4</td><td>8</td></tr>
//    <tr><td>Gosho</td><td>5</td><td>8</td></tr>
//    <tr><td>Angel</td><td>5.5</td><td>10</td></tr>
// </table>

console.log(fromJSONToHTMLTable(`[{"Name":"Pesho",
    "Score":4,
    " Grade":8},
   {"Name":"Gosho",
    "Score":5,
    " Grade":8},
   {"Name":"Angel",
    "Score":5.50,
    " Grade":10}]`));
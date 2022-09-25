function solve() {
  let textElement = document.getElementById('text').value;
  let namingConvention = document.getElementById('naming-convention').value;
  textElement = textElement.split(' ');
  let result = '';
  if (namingConvention === 'Camel Case') {
    result = textElement.map((x, i) => {
      let convert = x.toLowerCase();
      if (i != 0) {
        convert = x[0].toUpperCase() + x.slice(1).toLowerCase();
        
      }
      return convert;
    }).join('');
  } else if (namingConvention === 'Pascal Case') {
    result = textElement.map(x => x[0].toUpperCase() + x.slice(1).toLowerCase()).join('');
  } else {
    result = 'Error!';
  }
  let spanResult = document.getElementById('result');
  spanResult.textContent = result;
}
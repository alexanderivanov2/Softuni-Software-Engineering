function search() {
   let inputElementValue = document.getElementById('searchText').value;
   let townsElements = document.querySelectorAll('li');
   let resultElement = document.getElementById('result');
   let counter = 0;

   for (let el of townsElements) {
      let town = el.textContent;
      
      if (town.includes(inputElementValue)){
         el.style.textDecoration = 'underline';
         el.style.fontWeight = 'bold';
         counter += 1;
      } else {
         el.style.textDecoration = 'none';
         el.style.fontWeight = 'normal';
      }
   }

   resultElement.textContent = `${counter} matches found`;
   resultElement.style.textAlign = 'center';
}

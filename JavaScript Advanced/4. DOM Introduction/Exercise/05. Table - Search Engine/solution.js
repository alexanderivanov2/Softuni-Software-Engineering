function solve() {
   document.querySelector('#searchBtn').addEventListener('click', onClick);

   function onClick() {
      let searchValue = document.getElementById('searchField').value;
      let tdElements = document.querySelectorAll('tbody tr td');
      console.log(searchValue);
      console.log(tdElements)
      for (let td of tdElements) {
         if (td.parentNode.className != 'select') {
            tdText = td.textContent.toLowerCase();
            searchValue = searchValue.toLowerCase();
            if (tdText.includes(searchValue)) {
               td.parentNode.style.backgroundColor = 'yellow';
               td.parentNode.className = 'select';
            }
         }
      }
   }
}
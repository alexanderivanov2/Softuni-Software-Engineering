function create(words) {
   let divWrapperElement = document.getElementById('content');

   for (let word of words) {
      let createDivElement = document.createElement('div');
      let createPElement = document.createElement('p');
     
      createPElement.textContent = word;
      createPElement.style.display = 'none';
     
      createDivElement.appendChild(createPElement);
      divWrapperElement.appendChild(createDivElement);
   }

   let  divChildrenElements = document.querySelectorAll('#content div');
   divChildrenElements = Array.from(divChildrenElements);
   
   divChildrenElements.forEach(div => {
      div.addEventListener('click', (e) => {
         let pElement = div.children[0];
         pElement.style.display = 'block'
      });
   });
}
function loadRepos() {
   let divResElement = document.getElementById('res');
   let request = new XMLHttpRequest();
   let method = 'GET';
   let url = 'https://api.github.com/users/testnakov/repos'

   request.addEventListener('readystatechange', event => {
      if (request.status === 200 && request.readyState == 4) {
         divResElement.textContent = request.responseText;
      }
   });

   request.open(method, url);
   request.send();
}
function solve(){
   const postSection = document.querySelector('main section');
   const form = document.querySelector('form');
   const archiveSection = document.querySelector('.archive-section ol');


   form.addEventListener('submit', (e) => {
      e.preventDefault();
      const creator = form.querySelector('#creator');
      const title = form.querySelector('#title');
      const category = form.querySelector('#category');
      const content = form.querySelector('#content');
      console.log(creator.value, title.value, category.value, content.value);
      if (creator.value && title.value && category.value && content.value) {
         
         createPost(creator.value, title.value, category.value, content.value);
         form.reset();
      }
   })

   function createPost(creator, title, category, content) {
      const article = createElement('article', postSection);
      const titleHeading = createElement('h1', article, title);
      const pCategory = createElement('p', article, 'Category: ');
      createElement('strong', pCategory, category);
      const pCreator = createElement('p', article, 'Creator: ');
      createElement('strong', pCreator, creator);
      createElement('p', article, content);
      const divButtons = createElement('div', article, '', ['class', 'buttons']);
      const deleteBtn = createElement('button', divButtons, 'Delete', ['class', 'btn delete']);
      const archiveBtn = createElement('button', divButtons, 'Archive', ['class', 'btn archive']);

      deleteBtn.addEventListener('click', (e) => deletePost(e, article));
      archiveBtn.addEventListener('click', (e) => archivePost(e,titleHeading, article));
   }

   function createElement(type, parent='', content='', attributes=[]) {
      const el = document.createElement(type);

      if (parent) {
         parent.appendChild(el);
      }

      if(content) {
         el.textContent = content;
      }

      for (let i = 0; i < attributes.length; i+=2) {
         el.setAttribute(attributes[i], attributes[i + 1]);
      }

      return el;
   }

   function deletePost(e, article) {
      e.preventDefault();
      article.remove();
   }

   function archivePost(e, titleHeading, article) {
      e.preventDefault();
      createElement('li', archiveSection, titleHeading.textContent);
      article.remove();

      const liElements = archiveSection.querySelectorAll('li');
      Array.from(liElements).sort((a, b) => a.textContent.localeCompare(b.textContent))
         .map(li => archiveSection.appendChild(li));
   }
}

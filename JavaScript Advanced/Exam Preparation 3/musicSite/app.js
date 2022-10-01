window.addEventListener('load', solve);

function solve() {
    let allHitsDivElement = document.querySelector('.all-hits-container');
    let savedDivElement = document.querySelector('.saved-container');
    let likesParagraphElement = document.querySelector('.likes p');
    // Form Inputs
    let inputElementGenre = document.getElementById('genre');
    let inputElementName = document.getElementById('name');
    let inputElementAuthor = document.getElementById('author');
    let inputElementDate = document.getElementById('date');
    // add Button
    let addBtnElement = document.getElementById('add-btn');

    addBtnElement.addEventListener('click', (e) => {
        e.preventDefault();
        let genreValue = inputElementGenre.value;
        let nameValue = inputElementName.value;
        let authorValue = inputElementAuthor.value;
        let dateValue = inputElementDate.value;

        if (genreValue && nameValue && authorValue && dateValue) {
            let divElement = document.createElement('div');
            divElement.className = 'hits-info';
            let imgElement = document.createElement('img');
            let genreH2Element = document.createElement('h2');
            let nameH2Element = document.createElement('h2');
            let authorH2Element = document.createElement('h2');
            let dateH3Element = document.createElement('h3');
            let btnSaveSong = document.createElement('button');
            btnSaveSong.className = 'save-btn';
            btnSaveSong.textContent = 'Save song';
            let btnLikeSong = document.createElement('button');
            btnLikeSong.className = 'like-btn';
            btnLikeSong.textContent = 'Like song';
            let btnDelete = document.createElement('button');
            btnDelete.className = 'delete-btn';
            btnDelete.textContent = 'Delete';

            btnSaveSong.addEventListener('click', moveToSavedSongs);
            btnLikeSong.addEventListener('click', voteToTotalLike);
            btnDelete.addEventListener('click', deleteSong);
            // add content
            imgElement.setAttribute('src', './static/img/img.png');
            genreH2Element.textContent = `Genre: ${genreValue}`;
            nameH2Element.textContent = `Name: ${nameValue}`;
            authorH2Element.textContent = `Author: ${authorValue}`;
            dateH3Element.textContent = `Date: ${dateValue}`;

            divElement.appendChild(imgElement);
            divElement.appendChild(genreH2Element);
            divElement.appendChild(nameH2Element);
            divElement.appendChild(authorH2Element);
            divElement.appendChild(dateH3Element);
            divElement.appendChild(btnSaveSong);
            divElement.appendChild(btnLikeSong);
            divElement.appendChild(btnDelete);
            allHitsDivElement.appendChild(divElement);
            
        }
        inputElementGenre.value = '';
        inputElementName.value = '';
        inputElementAuthor.value = '';
        inputElementDate.value = '';
    });

    function moveToSavedSongs(e) {
        let parent = e.currentTarget.parentNode;
        savedDivElement.appendChild(parent);
        let btnLike = e.currentTarget.nextElementSibling;
        btnLike.remove();
        e.currentTarget.remove();
    }

    function voteToTotalLike(e) {
        let btn = e.currentTarget;
        let [text, likes] = likesParagraphElement.textContent.split(': ');
        likesParagraphElement.textContent = `${text}: ${Number(likes) + 1}`;
        btn.disabled = true;
    }

    function deleteSong(e) {
        e.currentTarget.parentNode.remove();
    }
}



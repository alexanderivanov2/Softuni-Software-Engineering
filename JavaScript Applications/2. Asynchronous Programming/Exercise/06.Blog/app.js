let urlPosts = 'http://localhost:3030/jsonstore/blog/posts';
let urlCommentsPosts = 'http://localhost:3030/jsonstore/blog/comments';

let selectPosts = document.getElementById('posts');
let postTitleH1 = document.getElementById('post-title');
let ulPostBody = document.getElementById('post-body');
let ulPostComments = document.getElementById('post-comments');
// buttons
let btnLoad = document.getElementById('btnLoadPosts');
let btnView = document.getElementById('btnViewPost');


function attachEvents() {
    btnLoad.addEventListener('click', loadPosts);
    btnView.addEventListener('click', renderPostDetails);
}

function loadPosts(){
    fetch(urlPosts)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error');
            }
            return response.json();
        })
        .then(data => {
            Object.keys(data).forEach(key => {
                createOptionElement('option', selectPosts, data[key].title, key);
            })
        })
        .catch(err => {
            console.log(err);
        })
}

function renderPostDetails() {
    
    postTitleH1.textContent = '';
    ulPostBody.replaceChildren();
    ulPostComments.replaceChildren();

    renderBody()
    renderComments()
}

function renderBody() {
    let urlPost = `http://localhost:3030/jsonstore/blog/posts/${selectPosts.value}`;

    fetch(urlPost)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            postTitleH1.textContent = data.title;
            ulPostBody.textContent = data.body;
        })
        .catch(err => console.log(err.message));
}

function renderComments() {
    ulPostComments.replaceChildren();

   fetch(urlCommentsPosts)
    .then(response => {
        if (response.status != 200) {
            throw new Error('Error');
        }
        
        return response.json();
    })
    .then(data => {
        Object.keys(data)
            .filter(key => data[key].postId == selectPosts.value)
            .forEach(key => {
                let text = data[key]['text'];
                let commentID = data[key]['id'];
                createLiElement('li', ulPostComments, text, commentID);
            })
    })
}

function createLiElement(type, parentElement, content, commentID) {
    let liElement = document.createElement(type);
    parentElement.appendChild(liElement);

    if(content) {
        liElement.textContent = content
    }

    if (commentID) {
        liElement.id = commentID;
    }
}

function createOptionElement(type, parentElement, content, value) {
    let optionElement = document.createElement(type);
    parentElement.appendChild(optionElement);

    if (content) {
        optionElement.textContent = content;
    }

    if (value) {
        optionElement.setAttribute('value', value);
    }

}

attachEvents();
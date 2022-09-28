function getArticleGenerator(articles) {
    let arr = articles;

    function displayArticles() {
        let divElement = document.querySelector('#content');
        if (arr.length > 0) {
            let article = document.createElement('article');
            article.textContent = arr.shift();
            divElement.appendChild(article);
        }   
    }
    return displayArticles;
}
async function getRecipes() {
    let result;
     fetch('http://localhost:3030/jsonstore/cookbook/recipes')
        .then(response => {
            if (response.ok == false && response.status != 200) {
                throw new Error(`${response.status} ${response.statusText}`);
            }
            return response.json()
        })
        .then(data => { 
            Object.keys(data).map(key => {
                createRecipeArticle(data[key]);
            })
        })
        //         data.map(el => {
        //         console.log(el);
        //         return el;
        // }))
        .catch(error => console.log(error))
    console.log(result);
    return result;
}

window.addEventListener('load', async () => {
    const main = document.querySelector('main');

    const recipes = await getRecipes();
    // console.log(recipes);
    // const cards = recipes.map(createRecipePreview);
    main.innerHTML = '';
    // cards.forEach(c => main.appendChild(c));
});

function createRecipeArticle(jsonRecipe) {
    const main = document.querySelector('main');

    let createArticle = document.createElement('article');
    createArticle.classList.add('preview');
    let divElementTitle = document.createElement('div');
    divElementTitle.classList.add('title');
    let h2ElementTitle = document.createElement('h2');
    let divElementImg = document.createElement('div');
    divElementImg.classList.add('small');
    let imgElement = document.createElement('img');


    h2ElementTitle.textContent = jsonRecipe.name;
    divElementTitle.appendChild(h2ElementTitle);
    createArticle.appendChild(divElementTitle);

    imgElement.src = jsonRecipe.img;
    divElementImg.appendChild(imgElement);
    createArticle.appendChild(divElementImg);

    createArticle.addEventListener('click', toggleCard)
    main.appendChild(createArticle);

    async function toggleCard() {
        fullRecipe(jsonRecipe._id, createArticle);
    }
}

async function fullRecipe(recipe_id, article) {
    try {
        const response = await fetch(`http://localhost:3030/jsonstore/cookbook/details/${recipe_id}`);
        if (response.ok == false && response.status != 200) {
            throw new Error(`${response.status} ${response.statusText}`);
        }
        const data = await response.json();
        article.replaceWith(createFullRecipe(data));
    } catch (error) {
        return console.log(error);
    }
}


function createFullRecipe(data) {
    let createArticle = document.createElement('article');
    let h2Element = document.createElement('h2');
    let divElementBand = document.createElement('div');
    divElementBand.classList.add('band');
    let divElementThumb = document.createElement('div');
    divElementThumb.classList.add('thumb');
    let imgElement = document.createElement('img');
    let divElementIngredients = document.createElement('div');
    divElementIngredients.classList.add('ingredients');
    let h3Element = document.createElement('h3');
    let ulElement = document.createElement('ul');
    let divElementDescription = document.createElement('div');
    divElementDescription.classList.add('description');
    let h3ElementPreparation = document.createElement('h3');

    h2Element.textContent = data.name;
    createArticle.appendChild(h2Element);
    imgElement.src = data.img;
    divElementThumb.appendChild(imgElement);
    divElementBand.appendChild(divElementThumb);
    

    h3Element.textContent = 'Ingredients:';
    divElementIngredients.appendChild(h3Element);
    data.ingredients.forEach(el => {
        let liElement = document.createElement('li');
        liElement.textContent = el;
        ulElement.appendChild(liElement);
    });
    divElementIngredients.appendChild(ulElement);
    divElementBand.appendChild(divElementIngredients);
    createArticle.appendChild(divElementBand);

    h3ElementPreparation.textContent = 'Preparation:';
    divElementDescription.appendChild(h3ElementPreparation);
    data.steps.forEach(step => {
        let pElement = document.createElement('p');
        pElement.textContent = step;
        divElementDescription.appendChild(pElement);
    });

    createArticle.appendChild(divElementDescription);
    return createArticle;
}
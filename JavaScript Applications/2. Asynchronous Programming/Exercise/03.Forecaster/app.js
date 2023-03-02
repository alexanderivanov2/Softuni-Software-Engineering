const weatherSymbols = {
    Sunny: '&#x2600;',
    'Partly sunny': '&#x26C5;',
    Overcast: '&#x2601;',
    Rain: '&#x2614;',
    Degrees: '&#176;'
}

let code;
let urlLocations = 'http://localhost:3030/jsonstore/forecaster/locations';

function attachEvents() {
    let submitBtn = document.getElementById('submit');
    submitBtn.addEventListener('click', prepareForecast);
}

function prepareForecast() {
    let inputLocation = document.getElementById('location');
    fetch(urlLocations)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            let location = data.find(obj => obj.name == inputLocation.value);
            if (!location) {
                throw new Error('Error');
            }

            code = location.code
            getForecast();
            


        }).catch(error => {
            code = ''
            console.log(error.message);
            checkAndRemove();
            
        })
    
}


function getForecast() {
    let divForecast = document.getElementById('forecast');
    let divCurrent = document.getElementById('current');
    let divUpcoming = document.getElementById('upcoming');

    checkAndRemove();

    let currentUrl = `http://localhost:3030/jsonstore/forecaster/today/${code}`;
    let upcomingUrl = `http://localhost:3030/jsonstore/forecaster/upcoming/${code}`;

    // current
    fetch(currentUrl)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            let symbolKey = data.forecast.condition;
            let divForecast = createElement(divCurrent, 'div', ['forecasts']);
            createElement(divForecast, 'span', ['condition', 'symbol'], [weatherSymbols[symbolKey]]);
            let spanCondtiion = createElement(divForecast, 'span', ['condition']);

            createElement(spanCondtiion, 'span', ['forecast-data'], data.name);
            createElement(spanCondtiion, 'span', ['forecast-data'], `${data.forecast.low}&#176;/${data.forecast.high}&#176;`);
            createElement(spanCondtiion, 'span', ['forecast-data'], symbolKey);
        })
        .catch(error => { 
            console.log(error);
        });
    //  upcoming 
    fetch(upcomingUrl)
        .then(response => {
            if (response.status != 200) {
                throw new Error('Error')
            }

            return response.json()
        })
        .then(data => {
            let divForecastData = createElement(divUpcoming, 'div', ['forecast-info']);
            data.forecast.forEach(obj => {
                let symbolKey = obj.condition;
                let upcomingSpan = createElement(divForecastData, 'span', ['upcoming']);
                createElement(upcomingSpan, 'span', ['symbol'], weatherSymbols[symbolKey]);
                createElement(upcomingSpan, 'span', ['forecast-data'], `${obj.low}&#176;/${obj.high}&#176;`);
                createElement(upcomingSpan, 'span', ['forecast-data'], `${obj.condition}`);
            })
        })
        .catch(error => {
            console.log(error);
        });
    divForecast.style.display = 'block';
}


function createElement(parrent, type, classes, content) {
    let element = document.createElement(type);

    if (parrent) {
        parrent.appendChild(element);
    }

    if (content) {
        element.innerHTML = content;
    }

    while(classes.length > 0) {
        element.classList.add(classes.pop());
    }
    
    return element;
}

function checkAndRemove() {
    let divForecastExists = document.querySelector('.forecasts');
    let divForecastDataExists = document.querySelector('.forecast-info');

    if (divForecastExists && divForecastDataExists) {

        divForecastDataExists.remove();
        divForecastExists.remove();
    }
}

attachEvents();
function getInfo() {
    let stopID = document.getElementById('stopId');
    let url = `http://localhost:3030/jsonstore/bus/businfo/${stopID.value}`;

    let noID = stopID.value == '' ? true : false;
    stopID.value = '';

    let divStopName = document.getElementById('stopName');
    let ulBuses = document.getElementById('buses');
    ulBuses.innerHTML = '';
    
    fetch(url)
        .then(response => {
            
            if((response.ok == false && response.status != 200) || response.status == 204 || noID) {
                throw new Error('Error');
            }

            return response.json();
        })
        .then(data => {
            divStopName.textContent = data.name;
            for (let [key, value] of Object.entries(data.buses)) {
                let text = `Bus ${key} arrives in ${value} minutes`;
                createElement(ulBuses, 'li', text);
            }
        })
        .catch(error => {
            divStopName.textContent = error.message;
        })
    
    function createElement(parrent, type, text) {
        let element = document.createElement(type);

        if (parrent) {
            parrent.appendChild(element);
        }

        if(text) {
            element.textContent = text;
        }
    }

    
}
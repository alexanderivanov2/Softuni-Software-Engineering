function solve() {
    let stopId = 'depot';
    let stopName = ''
    let url = `http://localhost:3030/jsonstore/bus/schedule/`;
    
    let departBtn = document.getElementById('depart');
    let arriveBtn = document.getElementById('arrive');
    let infoDiv = document.querySelector('.info');

    function depart() {
        fetch(url + stopId)
            .then(response => {
                if (response.status != 200) {
                    throw new Error('Error');
                }    
                
                return response.json();
            })
            .then(data => {
                stopId = data.next;
                stopName = data.name;
                infoDiv.textContent =`Next Stop ${stopName}`;
                departBtn.disabled = 'true';
                arriveBtn.disabled = '';
            })
            .catch(error => {
                infoDiv.textContent = error.message;
                departBtn.disabled = 'true';
                arriveBtn.disabled = 'false';
            })
    }

    function arrive() {
        infoDiv.textContent = `Arriving at ${stopName}`;
        arriveBtn.disabled = 'true';
        departBtn.disabled = '';
    }

    return {
        depart,
        arrive
    };
}

let result = solve();
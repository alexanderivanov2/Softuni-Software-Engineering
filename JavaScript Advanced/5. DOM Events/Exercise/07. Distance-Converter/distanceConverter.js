function attachEventsListeners() {
    
    let buttonElement = document.querySelector('#convert')

    const unitsInMeters = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254
    }

    buttonElement.addEventListener('click', (e) => {
        let inputOpitonElement = document.querySelector('#inputUnits');
        let inputDistanceElement = document.querySelector('#inputDistance');
        let outputOpitonElement = document.querySelector('#outputUnits');
        let outputDistanceElement = document.querySelector('#outputDistance');
        
        let inputValue = Number(inputDistanceElement.value);
        let result = inputValue * unitsInMeters[inputOpitonElement.value] / unitsInMeters[outputOpitonElement.value];
        outputDistanceElement.value = result;
    });
}
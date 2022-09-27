function attachEventsListeners() {
    let daysToHours = ((days) => days * 24);
    let hoursToDays = ((hours) => hours / 24);
    let hoursToMinutes = ((hours) => hours * 60);
    let minutesToHours = ((minutes) => minutes / 60);
    let minutesToSeconds = ((minutes) => minutes * 60);
    let secondsToMinutes = ((seconds) => seconds / 60);

    let daysInputElement = document.getElementById('days');
    let hoursInputElement = document.getElementById('hours');
    let minutesInputElement = document.getElementById('minutes');
    let secondsInputElement = document.getElementById('seconds');

    let inputButtonElements = document.querySelectorAll('input[type="button"]')

    inputButtonElements = Array.from(inputButtonElements);

    inputButtonElements.forEach(btn => {
        btn.addEventListener('click', (e) => {
            let inputElementType = btn.previousElementSibling;
            let inputElementLabel = inputElementType.previousElementSibling;
    
            if (inputElementType.value !== ''){
                let inputEl = Number(inputElementType.value);
                let inputLabel = inputElementLabel.textContent;

                if (inputLabel.includes('Days')) {

                    hoursInputElement.value = daysToHours(inputEl);
                    minutesInputElement.value = hoursToMinutes(hoursInputElement.value);
                    secondsInputElement.value = minutesToSeconds(minutesInputElement.value);

                } else if (inputLabel.includes('Hours')) {

                    daysInputElement.value = hoursToDays(inputEl);
                    minutesInputElement.value = hoursToMinutes(inputEl);
                    secondsInputElement.value = minutesToSeconds(minutesInputElement.value);

                } else if (inputLabel.includes('Minutes')) {

                   hoursInputElement.value = minutesToHours(inputEl);
                   daysInputElement.value = hoursToDays(hoursInputElement.value);
                   secondsInputElement.value = minutesToSeconds(inputEl); 

                } else if (inputLabel.includes('Seconds')) {

                    minutesInputElement.value = secondsToMinutes(inputEl);
                    hoursInputElement.value = minutesToHours(minutesInputElement.value);
                    daysInputElement.value = hoursToDays(hoursInputElement.value);
                }
            }
        });
    });
}
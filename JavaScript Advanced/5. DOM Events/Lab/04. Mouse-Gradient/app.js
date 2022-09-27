function attachGradientEvents() {
    let gradientBoxDivElement = document.getElementById('gradient');
    let resultElement = document.getElementById('result');

    // let width = gradientBoxDivElement.scrollWidth;
    // console.log(width);
    gradientBoxDivElement.addEventListener('mousemove', (e) => {
        let cursorPlaceX = e.offsetX;
        let percentage = Math.trunc(cursorPlaceX / (e.target.clientWidth - 1) * 100);
        resultElement.textContent = `${percentage}%`;   
    })
}

// function attachGradientEvents() {
//     let gradient = document.getElementById('gradient');
//     gradient.addEventListener('mousemove', gradientMove);
//     gradient.addEventListener('mouseout', gradientOut);
//     function gradientMove(event) {
//       let power = event.offsetX / (event.target.clientWidth - 1);
//       power = Math.trunc(power * 100);
//       document.getElementById('result').textContent = power + "%";
//     }
//     function gradientOut(event) {
//       document.getElementById('result').textContent = "";
//     }
// }
  
function getPrice (input) {
    let product = input[0];
    let day = input[1];
    let quantity = input[2];
    let price = 0;
    if (day === 'Sunday' || day === "Saturday") {
        switch(product){
            case 'banana': price = 2.70; break;
            case 'apple': price = 1.25; break;
            case 'orange': price = 0.90; break;
            case 'grapefruit': price = 1.60; break;
            case 'kiwi': price = 3.00; break;
            case 'pineapple': price = 5.60; break;
            case 'grapes': price = 4.20; break;
            default: price = 'error'; break;
        }
    }else if (day === 'Monday' || day === 'Tuesday' || day === 'Wednesday' || day === 'Thursday' || day === 'Friday'){
        switch(product){
            case 'banana': price = 2.50; break;
            case 'apple': price = 1.20; break;
            case 'orange': price = 0.85; break;
            case 'grapefruit': price = 1.45; break;
            case 'kiwi': price = 2.70; break;
            case 'pineapple': price = 5.50; break;
            case 'grapes': price = 3.85; break;   
            default: price = 'error'; break;
        } 
    } else {
        price = 'error';
    }
    if (price === 'error') {
        console.log(price)
    } else {
        console.log((price * quantity).toFixed(2));
    }
}
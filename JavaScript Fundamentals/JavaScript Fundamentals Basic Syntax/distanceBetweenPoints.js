function getDistance(x1, y1, x2, y2){
    x = x2 - x1;
    y = y2 - y1;
    formula = Math.sqrt(Math.pow(x, 2) + Math.pow(y, 2));
    console.log(formula);
}


getDistance(2, 4, 5, 0);
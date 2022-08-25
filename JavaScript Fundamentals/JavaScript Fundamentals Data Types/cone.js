function calculateCone(radius, height){
    let volume = ((Math.PI * radius * radius) *  height)/ 3;
    let s = Math.sqrt(radius * radius + height * height);
    let area = Math.PI * radius * (radius + s);
    console.log(`volume = ${volume.toFixed(4)}`);
    console.log(`area = ${area.toFixed(4)}`);
}


calculateCone(3, 5);
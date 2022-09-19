function calcGreatestCommonDivisor(a, b) {
    function gdc(a, b) {
        if (b == 0){
            return a;
        } else {
            return gdc(b, (a % b));
        }
    }    

    console.log(gdc(a, b));
}

calcGreatestCommonDivisor(15, 5);
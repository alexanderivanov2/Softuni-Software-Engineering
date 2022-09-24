function createAssemblyLine() {
    let objects = {};
    objects.hasClima = (object) => {
        object.temp = 21;
        object.tempSettings = 21;
        object.adjustTemp = () => {
            if (object.temp < object.tempSettings) {
                object.temp += 1;
            } else if (object.temp > object.tempSettings) {
                object.temp -= 1;
            }
        }
    }

    objects.hasAudio = (object) => {
        object.currentTrack = {
            name: null,
            artist: null,
        };
        object.nowPlaying = () => {
            if (object.currentTrack.name) {
                console.log(`Now playing '${object.currentTrack.name}' by ${object.currentTrack.artist}`);
            }
        }
    }

    objects.hasParktronic = (object) => {
        object.checkDistance = (distance) => {
            if (distance < 0.1) {
                console.log('Beep! Beep! Beep!');
            } else if (distance < 0.25) {
                console.log('Beep! Beep!');
            } else {
                console.log('Beep!');
            }
        }
    }
    return objects;
}




const assemblyLine = createAssemblyLine();

const myCar = {
    make: 'Toyota',
    model: 'Avensis'
};  

/Clima case/
assemblyLine.hasClima(myCar);
console.log(myCar);
console.log(myCar.temp);
myCar.tempSettings = 18;
myCar.adjustTemp();
console.log(myCar.temp);

/Audio case/
assemblyLine.hasAudio(myCar);
myCar.currentTrack = {
    name: 'Never Gonna Give You Up',
    artist: 'Rick Astley'
};
myCar.nowPlaying(); 

/Parktronic/
assemblyLine.hasParktronic(myCar);
myCar.checkDistance(0.4);
myCar.checkDistance(0.2);
console.log(myCar);

let jsonTry = JSON.stringify(myCar);
console.log(jsonTry);
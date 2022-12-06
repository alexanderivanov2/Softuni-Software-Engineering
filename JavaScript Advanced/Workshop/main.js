// select game screens
const gameStart = document.querySelector('.game-start');
const gameArea = document.querySelector('.game-area');
const gameOver = document.querySelector('.game-over');
const gameScore = document.querySelector('.game-score');
const gamePoints = gameScore.querySelector('.points');
const gameLevel = gameScore.querySelector('.level');

gameStart.addEventListener('click', onGameStart);

let keys = {};

let player = {
    x: 150,
    y: 100,
    width: 0,
    height: 0,
    lastTimeFiredFireball: 0,

};

let game = {
    speed: 2,
    movingMultiplier: 4,
    fireBallMultiplier: 5,
    bugMultiplier: 3,
    fireInterval: 1000,
    cloudSpawnInterval: 3000,
    bugsSpawnInterval: 1000,
    bugKillBonus: 2000,
    nextLevel: 5000,
    multiplierAdd: 0.75,
};

let scene = {
    level: 1,
    score: 0,
    point: 1,
    lastCloudSpawn: 0,
    lastBugSpawn: 0,
    isActiveGame: true,
}
function onGameStart() {
    gameStart.classList.add('hide');

    // render Wizard
    const wizard = document.createElement('div');
    wizard.classList.add('wizard');
    wizard.style.top = player.y + 'px';
    wizard.style.left = player.x + 'px';
    gameArea.appendChild(wizard);
    
    player.width = wizard.offsetWidth;
    player.height = wizard.offsetHeight;

    // game infinite loop
    window.requestAnimationFrame(gameAction);
}

// global key listeners
document.addEventListener('keydown', onKeyDown);
document.addEventListener('keyup', onKeyUp);



//key handlers
function onKeyDown(e) {
    keys[e.code] = true;
}

function onKeyUp(e) {
    keys[e.code] = false;
}


function gameAction(timestamp) {
    const wizard = document.querySelector('.wizard');

    // Apply gravitation
    let isInAir = player.y <= gameArea.offsetHeight - player.height;
    if (isInAir) {
        player.y += game.speed;
    }

    // Register user input
    if (keys.KeyW && player.y > 0) {
        player.y -= game.speed * game.movingMultiplier;
    }

    if (keys.KeyS && isInAir) {
        player.y += game.speed * game.movingMultiplier;
    }

    if (keys.KeyA && player.x > 0) {
        player.x -= game.speed * game.movingMultiplier;
    }

    if (keys.KeyD && player.x < gameArea.offsetWidth - player.width) {
        player.x += game.speed * game.movingMultiplier;
    }

    wizard.style.top = player.y + 'px';
    wizard.style.left = player.x + 'px';

    // Wizzard fireballs 
    if (keys.Space && timestamp - player.lastTimeFiredFireball > game.fireInterval) {
        wizard.classList.add('wizard-fire');
        addFireBall(player);
        player.lastTimeFiredFireball = timestamp;

    } else {
        wizard.classList.remove('wizard-fire');
    }

    let fireballs = document.querySelectorAll('.fire-ball');

    fireballs.forEach(fireball => {
        fireball.x += game.speed * game.fireBallMultiplier;
        fireball.style.left = fireball.x + 'px';

        if (fireball.x > gameArea.offsetWidth - fireball.offsetWidth) {
            fireball.remove();
        }
    });

    // Add clounds
    if (timestamp - scene.lastCloudSpawn > game.cloudSpawnInterval + 20000 * Math.random()) {
        let cloud = document.createElement('div');
        cloud.classList.add('cloud');
        cloud.x = gameArea.offsetWidth - 200;
        cloud.style.left = cloud.x + 'px';
        cloud.style.top = (gameArea.offsetHeight - 200) * Math.random() + 'px';
    
        gameArea.appendChild(cloud);
        scene.lastCloudSpawn = timestamp;
    }


    // Modify cloud positions
    let clouds = document.querySelectorAll('.cloud');
    clouds.forEach(cloud => {
        cloud.x -= game.speed;
        cloud.style.left = cloud.x + 'px';

        if (cloud.x <= 0) {
            cloud.remove();
        }
    });

    // Add bugs
    if (timestamp - scene.lastBugSpawn > game.bugsSpawnInterval + 5000 * Math.random()) {
        let bug = document.createElement('div');
        bug.classList.add('bug');
        bug.x = gameArea.offsetWidth - 60;
        bug.style.left = bug.x + 'px';
        bug.style.top = (gameArea.offsetHeight - 60) * Math.random() + 'px';
        gameArea.appendChild(bug);
        scene.lastBugSpawn = timestamp;
    }

    let bugs = document.querySelectorAll('.bug');
    
    bugs.forEach(bug => {
        if (isCollision(wizard, bug)) {
            gameOverAction();
        }

        fireballs.forEach(fireball => {
            if (isCollision(fireball, bug)) {
                fireball.remove();
                bug.remove();
                scene.score += game.bugKillBonus;
            }
        });

        bug.x -= game.speed * game.bugMultiplier;
        bug.style.left = bug.x + 'px';

        if (bug.x <= 0) {
            bug.remove();
        }
    })

    // console.log(`Bugs: ${bugs.length}; Fireballs: ${fireballs.length}; Clouds: ${clouds.length}`)


    scene.score += scene.point;
    gamePoints.textContent = scene.score;

    if (scene.score >= game.nextLevel) {
        game.nextLevel *= 2;
        scene.level += 1;
        gameLevel.textContent = scene.level;
        game.bugMultiplier += game.multiplierAdd;
        game.movingMultiplier += game.multiplierAdd / 3;
    }

    if(scene.isActiveGame) {
        window.requestAnimationFrame(gameAction);
    }
    // window.requestAnimationFrame(gameAction);
}

function addFireBall() {
    let fireBall = document.createElement('div');
    fireBall.classList.add('fire-ball');
    fireBall.style.top = (player.y + player.height / 3 - 5) + 'px';
    fireBall.x = player.x + player.width;
    fireBall.style.left = fireBall.x + 'px';

    gameArea.appendChild(fireBall);
}

function isCollision(firstElement, secondElement) {
    let firstRect = firstElement.getBoundingClientRect();
    let secondRect = secondElement.getBoundingClientRect();

    return !(firstRect.top > secondRect.bottom || firstRect.bottom < secondRect.top || firstRect.right < secondRect.left || firstRect.left > secondRect.right);
}

function gameOverAction() {
    scene.isActiveGame = false;
    gameOver.classList.remove('hide');
}

gameOver.addEventListener('click', (e) => {
    console.log('hi');
    location.reload();
});
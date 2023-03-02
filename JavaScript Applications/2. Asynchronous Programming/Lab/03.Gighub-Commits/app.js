function loadCommits() {
    let username = document.getElementById('username').value;
    let repo = document.getElementById('repo').value;
    let commitsUlElement = document.getElementById('commits');
    commitsUlElement.innerHTML = '';
    
    fetch(`https://api.github.com/repos/${username}/${repo}/commits`)
        .then(response => {
            if (response.ok && response.status == 200) {
                return response.json();
            }
            throw new Error(`Error: ${response.status} (Not Found)`);
        })
        .then(data => data.map(obj => {
            console.log(obj);
            let liElement = document.createElement('li');
            liElement.textContent = `${obj.commit.author.name}: ${obj.commit.message}`
            commitsUlElement.appendChild(liElement);
        }))
        .catch(error => {
            let liElement = document.createElement('li');
            liElement.textContent = `${error.message}`;
            commitsUlElement.appendChild(liElement);
        })
}
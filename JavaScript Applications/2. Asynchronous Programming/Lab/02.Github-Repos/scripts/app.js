function loadRepos() {
	let user = document.getElementById('username').value;
	let ulReposElement = document.getElementById('repos');
	ulReposElement.innerHTML = '';
	fetch(`https://api.github.com/users/${user}/repos`)
		.then(response => {
			if (response.ok == false) {
				throw new Error(`${response.status} ${response.statusText}`)
			}
			return response.json()})
		.then(data => data.map(repo => {
			let liElement = document.createElement('li');
			let aElement = document.createElement('a');
			aElement.href = repo.html_url;
			aElement.target = '_blank';
			aElement.textContent = repo.full_name;
			liElement.appendChild(aElement);
			ulReposElement.appendChild(liElement);
		}))
		.catch(error => {
			let liElement = document.createElement('li');
			console.log(error.message);
			liElement.textContent = `${error}`;
			ulReposElement.appendChild(liElement);
		});
}
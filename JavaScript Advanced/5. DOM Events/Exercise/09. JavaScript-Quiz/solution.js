function solve() {
	const answers = {
		'1': 'onclick',
		'2': 'JSON.stringify()',
		'3': 'A programming API for HTML and XML documents'
	}

	let rightAnswers = 0;
	let questionsAsked = 1;
	let sectionElement = document.querySelector('section');
	let buttonsElements = document.querySelectorAll('.answer-wrap');
	buttonsElements = Array.from(buttonsElements);
	let resultElement = document.getElementById('results')

	console.log(buttonsElements);
	buttonsElements.forEach(btn => {

		btn.addEventListener('click', (e) => {
			let answer = btn.children[0].textContent;
			if (answer === answers[`${questionsAsked}`]) {
				rightAnswers += 1;
			}
			questionsAsked += 1;
			sectionElement.style.display = 'none';

			if (questionsAsked < 4) {
				sectionElement = sectionElement.nextElementSibling;
				sectionElement.style.display = 'block'
			} else {
				resultElement.style.display = 'block';
				let h1Element = resultElement.querySelector('h1');

				h1Element.textContent = rightAnswers == 3 ? "You are recognized as top JavaScript fan!" : `You have ${rightAnswers} right answers`
			
			}		
		});
	})
}

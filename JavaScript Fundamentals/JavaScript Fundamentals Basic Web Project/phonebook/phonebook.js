/* TODO: 
	create phonebook array
	add methods for adding in the phonebook and getting it
	export the methods
*/

const Contact = require("./models/Contact");

let contacts = [
	new Contact('Peter', '+359555111222'),
	new Contact('John', '+359-222-777-111'),
	new Contact('Merry', '+359007002005')
];

function getContacts() {
	return contacts;
}

function addContact (name, phone) {
	let contact = new Contact(name, phone);
	contacts.push(contact);
}


module.exports = {
	getContacts,
	addContact
};
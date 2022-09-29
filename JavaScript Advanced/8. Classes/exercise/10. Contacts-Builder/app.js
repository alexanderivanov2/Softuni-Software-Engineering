class Contact {
    constructor(firstName, lastName, phone, email) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.phone = phone;
        this.email = email;
        this._online = false;
    }

    get online() {
        return this._online; 
    }

    set online(value) {
        this._online = value;
        
        if (this.divTitle) {
            if (!value) {
                this.divTitle.classList.remove('online');
            } else {
                this.divTitle.classList.add('online');
            }
        }   
        
        
    }

    render(id) {
        // debugger
        // if (!domElementById) {
        //     return
        // }
        // Create article
        let articleElement = document.createElement('article');
        // Create DivTitle
        this.divTitle = document.createElement('div');
        this.divTitle.className = 'title';
        let buttonElement = document.createElement('button');
        buttonElement.textContent = '\u2139';
        this.divTitle.textContent = `${this.firstName} ${this.lastName}`;
        this.divTitle.appendChild(buttonElement);
        
        if (this.online) {this.divTitle.classList.add('online');}

        let divElementInfo = document.createElement('div');
        divElementInfo.style.display = 'none'
        divElementInfo.className = 'info';
        let spanPhone = document.createElement('span');
        spanPhone.style.display = 'block';
        let spanEmail = document.createElement('span');
        spanPhone.textContent = `\u260E ${this.phone}`;
        spanEmail.textContent = `\u2709 ${this.email}`;
        divElementInfo.appendChild(spanPhone);
        divElementInfo.appendChild(spanEmail);

        articleElement.appendChild(this.divTitle);
        articleElement.appendChild(divElementInfo);

        buttonElement.addEventListener('click', (e) => {
            
            if (divElementInfo.style.display == 'block'){
                divElementInfo.style.display = 'none';
            } else {
                divElementInfo.style.display = 'block';
            }      
        });

        document.getElementById(id).appendChild(articleElement); 
    }
}

document.body.innerHTML = `
<div id="main"></div>
`;
// let contacts = [
//     new Contact("Ivan", "Ivanov", "0888 123 456", "i.ivanov@gmail.com"),
//     new Contact("Maria", "Petrova", "0899 987 654", "mar4eto@abv.bg"),
//     new Contact("Jordan", "Kirov", "0988 456 789", "jordk@gmail.com")
// ];



// console.log(contacts);
// contacts.forEach(c => c.render('mains'));




// // After 1 second, change the online status to true
// setTimeout(() => contacts[1].online = true, 2000);
// // contacts[1].online = true;
// // contacts[1].online = false;

let contact = new Contact(data.firstName, data.lastName, data.phone, data.email);

contact.online = true;
contact.render('holder');
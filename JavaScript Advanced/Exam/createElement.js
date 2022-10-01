function createElement(type, parent='', context='', attributes=[]){
    const el = document.createElement(type);

    if(context) {
        el.textContent = context;
    }

    for(let i = 0; i < attributes.length; i+=2) {
        el.setAttribute(attributes[i], attributes[i + 1]);
    }

    if(parent) {
        parent.appendChild(el);
    }

    return el;
}
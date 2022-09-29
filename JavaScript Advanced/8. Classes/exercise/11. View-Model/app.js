class Textbox {
    constructor(selector, regex) {
        this._value = '';
        this._elements = document.querySelectorAll(selector);
        this._invalidSymbols = regex;
        
    }

    get value() {
        return this._value;
    }

    set value(v) {
        this._value = v;
        for (let item of this.elements) {
            item.value = v;
        }
    }

    get elements() {
        return this._elements;
    }

    isValid() {
        return !this.value.match(this._invalidSymbols);
    }
}

let textbox = new Textbox(".textbox",/[^a-zA-Z0-9]/);
let inputs = document.getElementsByClassName('.textbox');

inputs.addEventListener('click',function(){console.log(textbox.value);});

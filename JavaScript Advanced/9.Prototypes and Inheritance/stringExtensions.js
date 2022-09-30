(function extenseString() {
    String.prototype.ensureStart = function (str) {
        if (!this.startsWith(str)) {
            return str.concat(this); 
        };
        return this.toString();
    }

    String.prototype.ensureEnd = function(str) {
        if (!this.endsWith(str)) {
            return this.concat(str);
        } 
        return this.toString();
    }

    String.prototype.isEmpty = function() {
        if (this.length == 0) {
            return true;
        } else {
            return false;
        }
    }

    String.prototype.truncate = function(n) {
        let len = this.length;
        if (n < 4){
            return '.'.repeat(n);
        }
         if (len <= n) {
            return this.toString();
        }
        
        console.log(this.toString().substring(0, n-2).lastIndexOf(' '));
        let lastSpace = this.toString().substring(0, n - 2).lastIndexOf(' ');

        if (lastSpace != -1) {
            return `${this.toString().substring(0, lastSpace)}...`;
        } else {
            return `${this.toString().substring(0, n-3)}...`;
        }
    }

    String.format = function (str, ...params) {
        let regExp = /\{\d+\}/gm;
        let parameters = params;
        str = str.split(' ');
        let txtArr = [];
        for (let i = 0; i < str.length; i++) {
            if (str[i].match(regExp) && parameters.length > 0) {
                txtArr.push(parameters.shift());
            } else {
                txtArr.push(str[i]);
            }
        }
        return txtArr.join(' ');
    }
})()




let str = 'my string';
str = str.ensureStart('my');
str = str.ensureStart('hello ');
console.log(str);
// str = str.ensureEnd('string');
// console.log(str);
// str = str.ensureEnd('add');
// console.log(str);
// console.log(str.isEmpty());
// str = '';
// console.log(str.isEmpty());
// str = 'my string';
str = str.truncate(16);
console.log(str);
str = str.truncate(14);
console.log(str);
str = str.truncate(8);
console.log(str);
str = str.truncate(4);
console.log(str);
str = str.truncate(2);
console.log(str);
str = String.format('The {0} {1} fox',
  'quick', 'brown');
console.log(str);
str = String.format('jumps {0} {1}',
  'dog');
console.log(str);
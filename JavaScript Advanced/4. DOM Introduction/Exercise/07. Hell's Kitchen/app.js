// SPAGETI CODE NEEED REFACTORING !!!!!!!!!!

function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function convertTextToArr(textareaElement) {
      let regExp = /(?<=\")[A-Za-z\d\-\s\,]+(?=\")/gm;
      let resultArr = textareaElement.match(regExp).filter(x => x.length > 3);
      return resultArr;
   }

   function returnWorkers(workersText) {
      let obj = {
         workers: {},
      };
      
      let totalSalary = 0;
      let bestSalary = 0;

      for (let workerText of workersText) {
         let [name, salary] = workerText.split(' ');
         salary = Number(salary);
         obj.workers[name] = salary;
         totalSalary += salary;
         bestSalary = salary > bestSalary ? salary : bestSalary;
      }

      obj['totalSalary'] = totalSalary;
      obj['bestSalary'] = bestSalary;
      // Return Second Results
      obj['sortBestWorkers'] = () => {
         sortedWorkers = Object.entries(obj.workers).sort((a, b) => b[1] - a[1]);
         let workersRanklist = `Name: ${sortedWorkers[0][0]} With Salary: ${sortedWorkers[0][1]}`;
         for (let i = 1; i < sortedWorkers.length; i++) {
         workersRanklist += ` Name: ${sortedWorkers[i][0]} With Salary: ${sortedWorkers[i][1]}`;
         }
         return workersRanklist;
      }
   
      obj['getAverageSalary'] = () => {
         let average = obj.totalSalary / Object.keys(obj.workers).length;
         
         return average
      }
      return obj
   }

   function addMoreWorkers(workersText, restaurant) {
      let obj = restaurant;
      for (let workerText of workersText) {
         let [name, salary] = workerText.split(' ');
         salary = Number(salary);
         obj.workers[name] = salary;
         obj.totalSalary += salary;
         obj.bestSalary = salary > obj.bestSalary ? salary : obj.bestSalary;
      }
      console.log(obj);
      console.log(obj.getAverageSalary());
      return obj;
   }

   function onClick () {
      let textareaElement = document.querySelector('#inputs textarea').value;
      // REFACTOR WITH JSON PARSE!!!
      let arr = convertTextToArr(textareaElement);
      let restaurants = {}
      for (let text of arr) {
      
         let [name, ...workersText] = text.split(' - ');
         workersText = workersText[0].split(', ');
       
         if (restaurants[name]) {
            restaurants[name] = addMoreWorkers(workersText, restaurants[name]);
            console.log(restaurants[name]);
            console.log(restaurants[name].getAverageSalary());
         } else {
            let restaurant = returnWorkers(workersText);
            restaurants[name] = restaurant;
         }  
      }

      sortedRestaurants = Object.entries(restaurants).sort((a, b) => b[1].getAverageSalary() - a[1].getAverageSalary());
      
      let bestRestaraunt = sortedRestaurants[0][1];
      let bestRestarauntName = sortedRestaurants[0][0];
      let bestRestarauntElement = document.querySelector('#bestRestaurant p');

      bestRestarauntElement.textContent = `Name: ${bestRestarauntName} Average Salary: ${bestRestaraunt.getAverageSalary().toFixed(2)} Best Salary: ${bestRestaraunt.bestSalary.toFixed(2)}`;

      let workersElement = document.querySelector('#workers p');
      workersElement.textContent = bestRestaraunt.sortBestWorkers();
   }
}

function cityTaxes(name, population, treasury) {
    let obj = {
        name,
        population,
        treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += this.taxRate * this.population;
        },
        applyGrowth(percentage) {
            this.population += this.population * (percentage / 100);
        },
        applyRecession(percentage) {
            this.treasury -= this.treasury * (percentage / 100);
        }
    }

    return obj;
}

const city =
  cityTaxes('Tortuga',
  7000,
  15000);

console.log(city);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);
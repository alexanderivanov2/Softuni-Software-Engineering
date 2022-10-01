window.addEventListener("load", solve);

function solve() {
  const tbody = document.getElementById('table-body');
  const soldSections = document.getElementById('cars-list');
  const profitElement = document.getElementById('profit');

  // form inputs
  const makeInput = document.getElementById('make');
  const modelInput = document.getElementById('model');
  const yearInput = document.getElementById('year');
  const fuelSelect = document.getElementById('fuel');
  const originalCostInput = document.getElementById('original-cost');
  const sellingPriceInput = document.getElementById('selling-price');

  document.getElementById('publish').addEventListener('click', (e) => {
    e.preventDefault();
    const formData = {
      make: makeInput.value,
      model: modelInput.value,
      year: yearInput.value,
      fuel: fuelSelect.value,
      originalCost: originalCostInput.value,
      sellingPrice: sellingPriceInput.value
    }

    if (formData.make && formData.model && formData.year && formData.fuel && formData.originalCost && formData.sellingPrice && (Number(formData.originalCost) <= Number(formData.sellingPrice))) {
      publish(formData);  
      makeInput.value = '';
      modelInput.value = '';
      yearInput.value = '';
      fuelSelect.value = '';
      originalCostInput.value = '';
      sellingPriceInput.value = '';
      // document.querySelector('form').reset();
    }
  });

  function publish(data) {
    const tr = createElement('tr', tbody, '', ['class', 'row']);
    createElement('td', tr, data.make);
    createElement('td', tr, data.model);
    createElement('td', tr, data.year);
    createElement('td', tr, data.fuel);
    createElement('td', tr, data.originalCost);
    createElement('td', tr, data.sellingPrice);
    const tdForBtns = createElement('td', tr);
    const btnEdit = createElement('button', tdForBtns, 'Edit', ['class', 'action-btn edit']);
    const btnSell = createElement('button', tdForBtns, 'Sell', ['class', 'action-btn sell']);

    btnEdit.addEventListener('click', (e) => editOffer(e, data));
    btnSell.addEventListener('click', (e) => sellOffer(e, data));
  }
  
  function editOffer(e, data) {
    e.preventDefault();
    makeInput.value = data.make;
    modelInput.value = data.model;
    yearInput.value = data.year;
    fuelSelect.value = data.fuel;
    originalCostInput.value = data.originalCost;
    sellingPriceInput.value = data.sellingPrice;
    e.currentTarget.parentNode.parentNode.remove();
  }

  function sellOffer(e, data) {
    e.preventDefault();

    const sellPice = Number(data.sellingPrice);
    const originalPrice = Number(data.originalCost);

    const liElement = createElement('li', soldSections, '', ['class', 'each-list']);
    createElement('span', liElement, `${data.make} ${data.model}`);
    createElement('span', liElement, data.year);
    createElement('span', liElement, `${sellPice - originalPrice}`);

    profitElement.textContent = (Number(profitElement.textContent) + (sellPice - originalPrice)).toFixed(2);
    e.currentTarget.parentNode.parentNode.remove();
  }
  
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
}

window.addEventListener('load', solve);

function solve() {
    let tableElement = document.getElementById('furniture-list');
    let totalPriceElement = document.querySelector('.total-price');

    let modelInput = document.getElementById('model');
    let yearInput = document.getElementById('year');
    let descriptionInput = document.getElementById('description');
    let priceInput = document.getElementById('price');

    let buttonAddElement = document.getElementById('add');

    buttonAddElement.addEventListener('click', (e) => {
        e.preventDefault();
        if(formValidation(modelInput.value, yearInput.value, descriptionInput.value, priceInput.value)) {
            renderToTable(modelInput.value, yearInput.value, descriptionInput.value, priceInput.value);
        }

        modelInput.value = '';
        yearInput.value = '';
        descriptionInput.value = '';
        priceInput.value = '';
    });

    function formValidation(model, year, description, price) {
        if (model.length === 0){
            return false;
        }
        if (year.length === 0 || isNaN(year) || Number(year) < 0) {
            return false
        }
        if (description.length === 0) {
            return false;
        }
        if (price.length === 0 || isNaN(price) || Number(price) < 0) {
            return false;
        }
        return true;
    }

    function renderToTable(model, year, description, price){
        // Create tr info
        let trElementInfo = document.createElement('tr');
        trElementInfo.className = 'info';
        // Create td Model and Price and append them to tr info
        let tdModel = document.createElement('td');
        tdModel.textContent = model;
        let tdPrice = document.createElement('td');
        tdPrice.textContent = `${Number(price).toFixed(2)}`;
        trElementInfo.appendChild(tdModel);
        trElementInfo.appendChild(tdPrice);
        // Create td with buttons more info and buy it and append them to tr info
        let tdButtons = document.createElement('td');
        let tdButtonMoreInfo = document.createElement('button');
        tdButtonMoreInfo.className = 'moreBtn';
        tdButtonMoreInfo.textContent = 'More Info';
        let tdButtonBuyIt = document.createElement('button');
        tdButtonBuyIt.className = 'buyBtn';
        tdButtonBuyIt.textContent = 'Buy it';
        tdButtons.appendChild(tdButtonMoreInfo);
        tdButtons.appendChild(tdButtonBuyIt);
        trElementInfo.appendChild(tdButtons);
        // Add event listeners to the buttons
        tdButtonMoreInfo.addEventListener('click', tableRenderMoreInfo);
        tdButtonBuyIt.addEventListener('click', buyItem);
        // create tr class=hide
        let trElementHide = document.createElement('tr');
        trElementHide.className = 'hide';
        let tdYear = document.createElement('td');
        tdYear.textContent = `Year: ${year}`;
        let tdDescription = document.createElement('td');
        tdDescription.colSpan = '3';
        
        tdDescription.textContent = `Description: ${description}`;
        trElementHide.appendChild(tdYear);
        trElementHide.appendChild(tdDescription);

        tableElement.appendChild(trElementInfo);
        tableElement.appendChild(trElementHide)
    }

    function tableRenderMoreInfo(e) {
        let btn = e.currentTarget;
        let trHide = e.currentTarget.parentNode.parentNode.nextSibling;
    
        if (btn.textContent == 'More Info') {
            btn.textContent = 'Less Info';
            trHide.style.display = 'contents';
        } else {
            btn.textContent = 'More Info';
            trHide.style.display = 'none';
        }
        // console.log(e.currentTarget.parentNode);
    }

    function buyItem(e) {
        let trParrentInfo = e.currentTarget.parentNode.parentNode;
        let trParrentSiblingHide = trParrentInfo.nextSibling;
        let price = trParrentInfo.querySelector('td:nth-child(2)');
        totalPriceElement.textContent = (Number(totalPriceElement.textContent) + Number(price.textContent)).toFixed(2);
        trParrentInfo.remove();
        trParrentSiblingHide.remove();
    }
}



// Unexpected error: expected '<trclass="info"><td>Chair</td><td>48.00</td><td><buttonclass="moreBtn">MoreInfo</button><buttonclass="buyBtn">Buyit</button></td></tr><trclass="hide"><td>Year:2016</td><tdcolspan="3">Description:Comfortableforyouandyourpet!</td></tr>' to equal '<trclass="info"><td>Chair</td><td>48.00</td><td><buttonclass="moreBtn">LessInfo</button><buttonclass="buyBtn">Buyit</button></td></tr><trclass="hide"style="display:contents;"><td>Year:2016</td><tdcolspan="3">Description:Comfortableforyouandyourpet!</td></tr>'
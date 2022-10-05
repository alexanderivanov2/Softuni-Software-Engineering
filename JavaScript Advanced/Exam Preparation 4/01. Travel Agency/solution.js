window.addEventListener('load', solution);

function solution() {
  // div id=block content
  let divBlockElement = document.getElementById('block');
  let ulInfoPreviewElement = document.getElementById('infoPreview');

  // let inputs
  let inputFullNameElement = document.getElementById('fname');
  let inputEmailElement = document.getElementById('email');
  let inputPhoneNumberElement = document.getElementById('phone');
  let inputAddressElement = document.getElementById('address');
  let inputPostalCodeElement = document.getElementById('code');

  // buttons
  let btnSubmit = document.getElementById('submitBTN');
  let btnEdit = document.getElementById('editBTN');
  let btnContinue = document.getElementById('continueBTN');

  btnSubmit.addEventListener('click', (e) => {
    e.preventDefault();
    if(inputFullNameElement.value && inputEmailElement.value) {
      let liFullName = document.createElement('li');
      let liEmail = document.createElement('li');
      let liPhoneNumber = document.createElement('li');
      let liAddress = document.createElement('li');
      let liPostalCode = document.createElement('li');

      liFullName.textContent = `Full Name: ${inputFullNameElement.value}`;
      liEmail.textContent = `Email: ${inputEmailElement.value}`;
      liPhoneNumber.textContent = `Phone Number: ${inputPhoneNumberElement.value}`;
      liAddress.textContent = `Address: ${inputAddressElement.value}`;
      liPostalCode.textContent = `Postal Code: ${inputPostalCodeElement.value}`;
   
      ulInfoPreviewElement.appendChild(liFullName);
      ulInfoPreviewElement.appendChild(liEmail);
      ulInfoPreviewElement.appendChild(liPhoneNumber);
      ulInfoPreviewElement.appendChild(liAddress);
      ulInfoPreviewElement.appendChild(liPostalCode);

      btnContinue.disabled = '';
      btnEdit.disabled = '';

      btnEdit.addEventListener('click', editInformation);
      btnContinue.addEventListener('click', completeReservation);

      e.currentTarget.disabled = 'true';
    }

    inputFullNameElement.value = '';
    inputEmailElement.value = '';
    inputPhoneNumberElement.value = '';
    inputAddressElement.value = '';
    inputPostalCodeElement.value = '';
  });

  function editInformation(e) {
    let children = Array.from(ulInfoPreviewElement.childNodes);
    inputFullNameElement.value = children[0].textContent.split(': ')[1];
    inputEmailElement.value = children[1].textContent.split(': ')[1];
    inputPhoneNumberElement.value = children[2].textContent.split(': ')[1];
    inputAddressElement.value = children[3].textContent.split(': ')[1];
    inputPostalCodeElement.value = children[4].textContent.split(': ')[1];
    removeAllChildNodes(ulInfoPreviewElement);
    btnSubmit.disabled = '';
    btnEdit.disabled = 'true';
    btnContinue.disabled = 'true';
  }

  function completeReservation(e) {
      removeAllChildNodes(divBlockElement);
      let headingElement = document.createElement('h3');
      headingElement.textContent = 'Thank you for your reservation!';
      divBlockElement.appendChild(headingElement);
  }

  function removeAllChildNodes(parent) {
      while(parent.firstChild) {
          parent.removeChild(parent.firstChild);
      }
  }
}

function solve() {
   let buttonElements = document.querySelectorAll('.add-product')
   buttonElements = Array.from(buttonElements);
   let buttonCheckoutElement = document.querySelector('.checkout');
   let textareaElement = document.querySelector('textarea');
   
   let totalPrice = 0;
   let products = [];

   buttonElements.forEach(btn => {

      btn.addEventListener('click', (e) => {
         let parentElement = btn.parentNode.parentNode;
         let productName = parentElement.querySelector('.product-title').textContent;
         let productPrice = parentElement.querySelector('.product-line-price');

         textareaElement.value += `Added ${productName} for ${productPrice.textContent} to the cart.\n`
         totalPrice += Number(productPrice.textContent);
         
         if (!products.includes(productName)) {
            products.push(productName);
         }
      })
      
   });

   buttonCheckoutElement.addEventListener('click', (e) => {
      textareaElement.value += `You bought ${products.join(', ')} for ${totalPrice.toFixed(2)}.`;

      buttonElements.forEach(btn => {
         btn.disabled = true;
      })

      buttonCheckoutElement.disabled = true;
   }); 


}
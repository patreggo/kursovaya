// checkout.js

function readCookie(name) {
    const nameEQ = name + "=";
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
        let cookie = cookies[i];
        while (cookie.charAt(0) === ' ') cookie = cookie.substring(1, cookie.length);
        if (cookie.indexOf(nameEQ) === 0) return cookie.substring(nameEQ.length, cookie.length);
    }
    return null;
}

document.addEventListener('DOMContentLoaded', function () {
    const cartItemsContainer = document.getElementById('cart-items');
    const confirmOrderBtn = document.getElementById('confirm-order-btn');

    // Fetch items from the shopping cart
    const savedBin = readCookie('bin');
    const bin = savedBin ? JSON.parse(decodeURIComponent(savedBin)) : [];
    updateCart();

    confirmOrderBtn.addEventListener('click', function () {
        // Implement logic to send the order to the server and update the database

        // Show a confirmation message
        alert('Thank you for your order!');

        // Clear the shopping cart
        bin.length = 0;
        updateCart();
        setCookie('bin', '', -1); // Remove the 'bin' cookie

        // Redirect to a thank you page if needed
        window.location.href = '/thank-you'; // Replace with the desired URL
    });

    function updateCart() {
        // Clear existing items in the cart container
        cartItemsContainer.innerHTML = '';
        const totalPriceElement = document.getElementById('total-price');
        let totalPrice = 0;
        // Display items from the shopping cart on the checkout page
        bin.forEach((item, index) => {
            const cartItem = document.createElement('div');
            cartItem.classList.add('cart-item');

            const itemName = document.createElement('span');
            itemName.textContent = item.model;

            const itemPrice = document.createElement('span');
            itemPrice.textContent = '₽' + item.price;

            const removeBtn = document.createElement('span');
            removeBtn.classList.add('remove-btn');
            removeBtn.textContent = 'Удалить';
            removeBtn.addEventListener('click', function () {
                removeFromCart(index);
            });

            const itemQuantity = document.createElement('span');
            itemQuantity.textContent = 'Количество: ' + item.count;

            cartItem.appendChild(itemName);
            cartItem.appendChild(itemPrice);
            cartItem.appendChild(itemQuantity);
            cartItem.appendChild(removeBtn);

            cartItemsContainer.appendChild(cartItem);

            totalPrice += item.price * item.count;;
        });

        totalPriceElement.textContent = 'Итоговая сумма: ₽' + totalPrice;
    } 

    function removeFromCart(index) {
        bin.splice(index, 1);
        updateCart();
        setCookie('bin', encodeURIComponent(JSON.stringify(bin)), 7);
    }
});


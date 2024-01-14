function setCookie(name, value, days) {
    let expires = "";
    if (days) {
        let date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "")  + expires + "; path=/";
}

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

    
    const savedBin = readCookie('bin');
    const bin = savedBin ? JSON.parse(decodeURIComponent(savedBin)) : [];
    updateCart();

    confirmOrderBtn.addEventListener('click', function () {
        alert('Спасибо за заказ!');
        bin.length = 0;
        updateCart();
        setCookie('bin', '', -1); 

        
        window.location.href = '/'; 
    });

    function updateCart() {
        
        cartItemsContainer.innerHTML = '';
        const totalPriceElement = document.getElementById('total-price');
        let totalPrice = 0;
        
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


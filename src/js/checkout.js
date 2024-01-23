(function () {

    function setCookie(name, value, days) {
        let expires = "";
        if (days) {
            let date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
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
    const cartItemsContainer = document.getElementById('cart-items');
    const confirmOrderForm = document.getElementById('orderForm');


    const savedBin = readCookie('bin');
    const bin = savedBin ? JSON.parse(decodeURIComponent(savedBin)) : [];
    updateCart();

    const binCookie = document.cookie.split(';').find(cookie => cookie.trim().startsWith('bin='));
    const binUserString = decodeURIComponent(binCookie.split('=')[1]);
    var binUser = JSON.parse(binUserString);

    var resultStringCount = binUser.map(obj => `${obj.model}: ${obj.count}`).join(', ');
    console.log(resultStringCount);

    var resultString = binUser.map(obj => obj.model).join(', ');
    console.log(resultString);

    confirmOrderForm.addEventListener('submit', function (event) {
        event.preventDefault();

        let models = resultString;
        let total_price = localStorage.getItem("totalPrice")
        let count = resultStringCount;
        let name_user = document.getElementById('nameUser').value
        let address_user = document.getElementById('addressUser').value
        let mail_user = document.getElementById('mailUser').value


        const formData = new FormData();
        formData.append('models', models);
        formData.append('total_price', total_price);
        formData.append('count', count);
        formData.append('name_user', name_user);
        formData.append('address_user', address_user);
        formData.append('mail_user', mail_user);
        console.log(formData)
        createOrder(formData);
        console.log("Good")
        bin.length = 0;
        updateCart();
        setCookie('bin', '', -1);
    });

    async function createOrder(formData) {
        const url = '/api/create_order';
        try {
            const response = await fetch(url, {
                method: 'POST',
                body: formData,
            });
            if (response.ok) {
                const result = await response.json();
                document.location.href = "/"
                console.log(result);
            } else {
                console.error('Ошибка при оформлении заказа');
            }
        } catch (error) {
            console.error('Ошибка:', error);
        }
    }




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
        localStorage.setItem("totalPrice", totalPrice)
    }

    function removeFromCart(index) {
        bin.splice(index, 1);
        updateCart();
        setCookie('bin', encodeURIComponent(JSON.stringify(bin)), 7);
    }
})()




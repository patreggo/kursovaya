(function () {
    let bin = [];

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

    function setCookie(name, value, days) {
        let expires = '';
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + value + expires + "; path=/";
    }

    window.onload = function () {
        try {
            const savedBin = readCookie("bin");
            if (savedBin) {
                bin = JSON.parse(decodeURIComponent(savedBin));
                console.log("Загруженная корзина:", bin);
                updateCart();
            }
        } catch (error) {
            console.error("Error parsing JSON:", error);
            // Handle the error as needed
        }
    };

fetch('/api/products')
    .then(response => response.json())
    .then(products => {
        const productCards = document.querySelector('.product-cards');
        products.forEach(product => {
            const card = document.createElement('div');
            card.className = 'card';

            const img = document.createElement('img');
            img.src = product.image;
            card.appendChild(img);

            const name = document.createElement('h2');
            name.textContent = product.model;
            card.appendChild(name);

            const description = document.createElement('p');
            description.textContent = product.description.length > 100 ? product.description.substring(0, 100) + '...' : product.description;
            card.appendChild(description);

            const price = document.createElement('p');
            price.textContent = `Цена: ${product.price}`+'₽';
            card.appendChild(price);

            const buyButton = document.createElement('button');
            buyButton.textContent = 'Купить';
            buyButton.className = 'btn';
            
            if (product.count==0) {
                buyButton.setAttribute('disabled', 'disabled');
                buyButton.textContent = 'Нет в наличии';
            }

            img.addEventListener("click", function () {
                window.location.href = "/product/" + product.id;
            });


            buyButton.addEventListener("click", function () {
                addToCart(product);
            });

            card.appendChild(buyButton);

            productCards.appendChild(card);
        });
    });
    function addToCart(product) {

        
        // Проверяем, есть ли уже такой продукт в корзине 
        const existingProduct = bin.find(item => item.id === product.id); 
 
        if (existingProduct) { 
            // Если продукт уже есть, увеличиваем количество 
            if (existingProduct.count >= product.count) {
                alert('Вы не можете добавить больше товаров, чем есть в наличии');
                return;
            }
            existingProduct.count += 1; 
        } else { 
            // Иначе добавляем новый продукт в корзину 
            bin.push({ id: product.id, model: product.model, description: product.description, price: product.price, count: 1 }); 
        } 
 
        console.log("Добавлено в корзину:", product.name); 
        console.log(bin); 
 
        setCookie("bin", encodeURIComponent(JSON.stringify(bin)), 7); 
        updateCart(); 
    }

    

    function updateCart() {
        const cartItemsContainer = document.getElementById('cart-items');
        const totalPriceElement = document.getElementById('total-price');
        const checkoutBtn = document.getElementById('checkout-btn');
        let totalPrice = 0;

        cartItemsContainer.innerHTML = '';

        bin.forEach((item, index) => {

            console.log(item);
            const itemQuantity = document.createElement('span'); 
            itemQuantity.textContent = 'Количество: ' + item.count;

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

            

            cartItem.appendChild(itemName);
            cartItem.appendChild(itemPrice);
            cartItem.appendChild(removeBtn);
            cartItem.appendChild(itemQuantity);
            

            cartItemsContainer.appendChild(cartItem);
            
            totalPrice += item.price * item.count;;

            
        });

        if (bin.length > 0) {
            document.getElementById('checkout-button').style.display = 'block';
        } else {
            document.getElementById('checkout-button').style.display = 'none';
        }

        document.getElementById('checkout-button').addEventListener('click', function() {
            window.location.href = '/checkout'; // replace 'checkout.html' with your checkout page URL
        });

        totalPriceElement.textContent = 'Итоговая сумма: ₽' + totalPrice;
    }
    


    function removeFromCart(index) {
        bin.splice(index, 1);
        updateCart();
        setCookie("bin", encodeURIComponent(JSON.stringify(bin)), 7);
    }
})();
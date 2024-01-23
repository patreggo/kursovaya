(function () {
    fetch('/api/products')
        .then((response) => {
            return response.json();
        })
        .then((myjson) => {
            console.log(myjson)
            let path = window.location.href;
            let productId = new URL(path).pathname.split('/').pop();
            productId = parseInt(productId, 10);
            let productWithId = myjson.find(product => product.id === productId);
            if (productWithId) {
                document.querySelector(".name").innerHTML = productWithId.model;
                document.querySelector(".desc").innerHTML = productWithId.description;
                document.querySelector(".cost").innerHTML = productWithId.price;
                document.querySelector(".img-product").src = "http://127.0.0.1:8080/"+productWithId.image;
            }
            else {
                alert("Такого продукта нет!")
            }

            console.log(productWithId);
        });
})();
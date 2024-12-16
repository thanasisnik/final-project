// A part of code was created with the help of AI and it handles the form submission
// its logic was fully understood first

document.getElementById("addProductsForm").addEventListener("submit", function(event) {
    event.preventDefault(); //prevent the default form submit
    
    //taking the table from the input
    var product = document.getElementById("product").value.trim();
    var price = document.getElementById("price").value;

    if (!product || !price || isNaN(price) || parseFloat(price) < 0) {
        alert("Please enter a valid product name and price!");
        return;
    }
    
    // making an object XMLHttpRequest to send data to the server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add_product", true); //declare the url for the post
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); //declare that the data will be URL encoded
    //when we send a POST request method this is the default Content-type so the server will understand the data

    //when submit completed
    xhr.onreadystatechange = function(){
        // check the state of the request, 4 menas request finished succesfully, 
        if (xhr.readyState === 4 && xhr.status === 200) {
            // connverts the server res to json
                var response = JSON.parse(xhr.responseText);

                var newProduct = `<li id="product-${response.id}">
                                    ${response.p_name} - ${response.price}$
                                </li>`;
                

                document.getElementById("products-list").innerHTML += newProduct;

                document.getElementById("product").value = "";
                document.getElementById("price").value = "";
        
        } else {
            console.error(xhr.responseText);
        }
    
    };
    xhr.send("product=" + encodeURIComponent(product) + "&price=" + encodeURIComponent(price));  // Using encodeURIComponent for safety
});
// A part of code was created with the help of AI and it handles the form submission
// its logic was fully understood first

document.addEventListener("DOMContentLoaded", () => {
    const orderList = document.getElementById("order-list");
    
    const submitOrderbtn = document.getElementById("submitOrderbtn");

    
    let currentOrder = [];

    document.querySelectorAll(".add").forEach(button => {
        button.addEventListener("click", () => {
            const productId = button.getAttribute("data-id");
            const productName = button.getAttribute("data-name");
            const productPrice = button.getAttribute("data-price");

            currentOrder.push({id : productId, name : productName, price : productPrice});

            const crntList = document.createElement("li");
            crntList.textContent = `${productName} - ${productPrice}$`
            orderList.appendChild(crntList);
            // we show the product with the price as a list
        });
    });

       // order submit
       submitOrderbtn.addEventListener("click", () => {
        console.log("Sending order for table", tableId);
        
        fetch(`/order/${tableId}`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(currentOrder),
        })
        // executes when fetch is succesfull
        .then(response => {
            if (response.ok) {
                window.location.href = "/"; // Reload the page after the order is submitted
            } else {
                alert("There was an issue with the order submission.");
            }
        })
        // error handling with jS
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while submitting the order.");
        });
        
    });
    const closeTable = document.getElementById("close-table");
    closeTable.addEventListener("click", () => {
        fetch(`/order/${tableId}/close`,{
            method: "POST",
            headers: {"Content-type":"application/json"}
        })
        .then(response => {
            if (response.ok){
                window.location.href = "/";
            } else {
                alert("There was an issue settling the order.");
            }
        })
        .catch(error => {
            console.error("Error:", error);
            alert("An error occurred while settling the order.");
        });
    })
});
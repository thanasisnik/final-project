// A part of code was created with the help of AI and it handles the form submission
// its logic was fully understood first

document.getElementById("addTableForm").addEventListener("submit", function(event) {
    event.preventDefault(); //prevent the default form submit
    
    //taking the table from the input
    var table_number = document.getElementById("table_number").value;
    
    // making an object XMLHttpRequest to send data to the server
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/add_table", true); //declare the url for the post
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded"); //declare that the data will be URL encoded
    //when we send a POST request method this is the default Content-type so the server will understand the data

    //when submit completed
    xhr.onreadystatechange = function(){
        if (xhr.readyState === 4 && xhr.status === 200) {
            var response = JSON.parse(xhr.responseText); // we take the response at JSON

            //making a new table and add it to the list
            // var newTable = "<li>Table #" + table_number + " </li>";
            // document.getElementById("table-list").innerHTML += newTable;

            // //we clear the insert field
            // document.getElementById("table_number").value= "";
                // var newTable = document.createElement("li");
                
                // newTable.classList.add("available"); //default
                // newTable.id = `table-${response.table_number}`;
                // newTable.innerHTML = `<a class="my-border padding-xsm" href="/order/${response.table_number}">Table #${table_number}</a>`;
                // document.getElementById("table-list").appendChild(newTable);
                
                // console.log(newTable.className);
                 // Create the entire structure, including the parent div
                 //Here becouse my previus attempts doesnt loaded my css instantly i get the AI help and now it works like i wanted
                 // difference from previus code is just adding and the div and not just the li something simple.
            var newTableContainer = document.createElement("div");
            newTableContainer.classList.add("my-border", "wrap", "d-flex", "font-size-m", "padding-17", "available");
            
            var newTable = document.createElement("li");
            newTable.id = `table-${response.table_number}`;
            
            var newTableLink = document.createElement("a");
            newTableLink.classList.add("my-border", "padding-8", "available");
            newTableLink.href = `/order/${response.table_number}`;
            newTableLink.textContent = `${table_number}`;
            
            newTable.appendChild(newTableLink);
            newTableContainer.appendChild(newTable);
            
            document.getElementById("table-list").appendChild(newTableContainer);
            
            // Clear the input field
            document.getElementById("table_number").value = "";
        }
    };
    xhr.send("table_number=" + encodeURIComponent(table_number));  // Using encodeURIComponent for safety
});
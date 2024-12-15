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
            var newTable = document.createElement("li");
            newTable.className = "available"; //default
            newTable.id = `table-${response.table_number}`;
            newTable.innerHTML = `<a class="my-border padding-xsm" href="/order/${response.table_number}">Table #${table_number}</a>`;
            document.getElementById("table-list").appendChild(newTable);
            console.log(newTable.className);
        }
    };
    xhr.send("table_number=" + encodeURIComponent(table_number));  // Using encodeURIComponent for safety
});
function addRow() {
    // get the values from the input fields
    var name = document.getElementById("name").value;
    var weight = document.getElementById("weight").value;
    var date = document.getElementById("date").value;
  
    // create a new row and cells
    var table = document.getElementById("myTable");
    var row = table.insertRow();
    var nameCell = row.insertCell(0);
    var weightCell = row.insertCell(1);
    var dateCell = row.insertCell(2);
    var actionCell = row.insertCell(3);
  
    // set the values of the new cells
    nameCell.innerHTML = name;
    weightCell.innerHTML = weight;
    dateCell.innerHTML = date;
    actionCell.innerHTML = '<button onclick="deleteRow(this)">Delete</button>';
  
    // clear the input fields
    document.getElementById("name").value = "";
    document.getElementById("weight").value = "";
    document.getElementById("date").value = "";
  
    // store the data in local storage
    var data = { name: name, weight: weight, date: date };
    var storedData = JSON.parse(localStorage.getItem('myData')) || [];
    storedData.push(data);
    localStorage.setItem('myData', JSON.stringify(storedData));
  }
  
  // function to load the data from local storage when the page is loaded
  window.onload = function() {
    var storedData = JSON.parse(localStorage.getItem('myData')) || [];
    for (var i = 0; i < storedData.length; i++) {
      var data = storedData[i];
  
      // create a new row and cells
      var table = document.getElementById("myTable");
      var row = table.insertRow();
      var nameCell = row.insertCell(0);
      var weightCell = row.insertCell(1);
      var dateCell = row.insertCell(2);
      var actionCell = row.insertCell(3);
  
      // set the values of the new cells
      nameCell.innerHTML = data.name;
      weightCell.innerHTML = data.weight;
      dateCell.innerHTML = data.date;
      actionCell.innerHTML = '<button onclick="deleteRow(this)">Delete</button>';
    }
  }
  
  
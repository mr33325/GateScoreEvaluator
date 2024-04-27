document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("myTable");
    var rows = table.getElementsByTagName("tr");
  
    // Hide the Colour column
    for (var i = 0; i < rows.length; i++) {
      var cells = rows[i].getElementsByTagName("td");
      if (cells.length > 0) {
        var colourCell = cells[cells.length - 1]; // Assuming "Colour" column is the last column
        var colourValue = colourCell.textContent.trim();
        if (colourValue === "R") {
          cells[1].style.backgroundColor = "#FFCDD2"; // Set background color of 2nd column to red
          cells[2].style.backgroundColor = "#FFCDD2"; // Set background color of 3rd column to red
        } else if (colourValue === "G") {
          cells[1].style.backgroundColor = "#C8E6C9"; // Set background color of 2nd column to green
          cells[2].style.backgroundColor = "#C8E6C9"; // Set background color of 3rd column to green
        } else if (colourValue === "Y") {
          cells[1].style.backgroundColor = "#FFF9C4"; // Set background color of 2nd column to yellow
          cells[2].style.backgroundColor = "#FFF9C4"; // Set background color of 3rd column to yellow
        }
      }
    }
  });
  
  document.addEventListener("DOMContentLoaded", function() {
    var table = document.getElementById("myTable");
    var cells = table.getElementsByTagName("td");
    
    for (var i = 0; i < cells.length; i++) {
      if (cells[i].textContent.trim() === 'NaN') {
        cells[i].textContent = ''; // Set the cell content to blank
      }
    }
  });
  
  function sortTableByColour() {
      var table = document.getElementById("myTable");
      var rows = Array.from(table.rows).slice(1); // Skip header row
      
      rows.sort(function(a, b) {
          var aColour = a.cells[3].textContent.trim();
          var bColour = b.cells[3].textContent.trim();
          
          if (aColour === "G" && bColour !== "G") {
              return -1;
          } else if (aColour !== "G" && bColour === "G") {
              return 1;
          } else if (aColour === "R" && bColour !== "R") {
              return -1;
          } else if (aColour !== "R" && bColour === "R") {
              return 1;
          } else {
              return 0;
          }
      });
  
      // Re-append sorted rows to the table
      rows.forEach(function(row) {
          table.appendChild(row);
      });
  }
  
  document.addEventListener("DOMContentLoaded", function() {
      var filterDropdown = document.getElementById("filterDropdown");
  
      filterDropdown.addEventListener("change", function() {
          var selectedValue = filterDropdown.value;
  
          // Sort the table rows based on the colour column
          sortTableByColour();
  
          // Filter rows based on the selected option
          var table = document.getElementById("myTable");
          var rows = Array.from(table.rows).slice(1); // Skip header row
  
          rows.forEach(function(row) {
              var colour = row.cells[6].textContent.trim();
              if (selectedValue === "all" || (selectedValue === "correct" && colour === "G") || 
                  (selectedValue === "wrong" && colour === "R") ||
                  (selectedValue === "notAttempted" && colour === "Y")) {
                  row.style.display = "";
              } else {
                  row.style.display = "none";
              }
          });
      });
  });
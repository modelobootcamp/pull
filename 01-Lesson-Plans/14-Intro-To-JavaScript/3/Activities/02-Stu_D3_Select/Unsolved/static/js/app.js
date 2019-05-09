// The new student and grade to add to the table
var newGrade = ["Wash", 79];

// Use D3 to select the table

// d3.select("html element")
var table = d3.select("table");

//d3.select("table").attr("class", "table table-striped")
table.attr("class", "table table-striped");


// Use d3 to create a bootstrap striped table
// http://getbootstrap.com/docs/3.3/css/#tables-striped

// Use D3 to select the table body
// var body = d3.select("tbody");
// // Append one table row `tr` 
 var row = body.append("tr");
// // Append one cell for the student name
// row.append("td").text("79")
 row.append("td").text(newGrade[0]);
// // Append one cell for the student grade
 row.append("td").text(newGrade[1]);

d3.select("tbody")
    .append("tr")
    .append("td").text("Wash")

d3.select("tbody")
    .append("tr")
    .append("td").text("Phillip")
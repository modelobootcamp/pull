/* data route */
var url = "/data";

function buildPlot() {
    d3.json("/data").then( function(response) {


var trace = {
    x : response.map(row => row[0]),
    y :response.map(row => row[1]),
    type: "scatter",
    mode:  "line"

}





    }
        
    )


}

buildPlot();

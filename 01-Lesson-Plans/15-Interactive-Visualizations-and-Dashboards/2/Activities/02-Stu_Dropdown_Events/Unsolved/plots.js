function init() {
  var data = [{
    values: [19, 26, 55, 88],
    labels: ["Spotify", "Soundcloud", "Pandora", "Itunes"],
    type: "pie"
  }];

  var layout = {
    height: 600,
    width: 800
  };

  Plotly.plot("pie", data, layout);
}

function updatePlotly(data_arg) {
  // YOUR CODE HERE
  
   Plotly.restyle("pie", "values", [data_arg])
  }

function getData(dataset) {
  switch (dataset) {
    case "option1":
      console.log("USA!!");
      data = [1, 20, 300, 10]
      break;
    case "option2":
      console.log("UK!!!");
      data = [35,6, 11, 20]
      break;
    case "option3":
      console.log("Canada!!!")
      data = [5,5,5,5]
      break;
    default:
      console.log("default")
  }
  console.log(data)
  updatePlotly(data);


}

init();

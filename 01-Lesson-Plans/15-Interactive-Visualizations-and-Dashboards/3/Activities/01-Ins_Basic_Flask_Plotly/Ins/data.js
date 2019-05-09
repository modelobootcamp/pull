d3.json('/data').then(function(data) {
    var layout = { margin: { t: 0 } }
    var LINE = document.getElementById('line');
    Plotly.plot(LINE, data)
  })
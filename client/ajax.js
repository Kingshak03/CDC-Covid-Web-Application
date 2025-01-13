        function ajaxGetRequest(path, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("GET", path);
    request.send();
}

function getData(){
  ajaxGetRequest("/bar", barChart);
  ajaxGetRequest("/pie", pieChart);
}

function barChart(response) {
  let data = JSON.parse(response)
  dicts = {'x': [], 'y': []}
  for (let info of data){
     dicts['x'].push(info['location']);
     dicts['y'].push(info['series_complete_pop_pct']);
  }

  console.log(dicts); 

  var chart = [
    {
      title: 'Fully Vaccinated By Location',
      x: dicts['x'],
      y: dicts['y'],
      type: 'bar'
    }
  ];

  Plotly.newPlot("BarChart", chart);
}

function pieChart(response) {
  let vac_data = JSON.parse(response)
  dicts = {'vaccine': [], 'sum': []}
  for (let sum_info in vac_data){
     dicts['vaccine'].push(sum_info);
     dicts['sum'].push(vac_data[sum_info]);
  }
  console.log(dicts);
  
  var pie_chart = [{
      // title: 'Vaccine Manufacturer Market Share',
      values: dicts['sum'],
      labels: dicts['vaccine'],
      type: 'pie'
    }];

  var layout = {
  height: 400,
  width: 500
  };

  Plotly.newPlot("PieChart", pie_chart, layout);
}

       
function ajaxPostRequest(path, data, callback) {
    let request = new XMLHttpRequest();
    request.onreadystatechange = function() {
          if (this.readyState===4 && this.status ===200) {
              callback(this.response);
            }
    }
    request.open("POST", path);
    request.send(data);
}

function getLocData(){
  let location = document.getElementById("locText").value;
  let loc = {"location": location}
  let locblob = JSON.stringify(loc);
  console.log(locblob);
  ajaxPostRequest("/line", locblob, lineChart);
}

function lineChart(response){
  let loc_data = JSON.parse(response);
  console.log(loc_data);

  if (loc_data.length == 0){
    alert("404 Location does not exist, try again with State Abbreviation ")
  }

  dicts = {'date': [], 'num_vaccines': []}
  for (let info of loc_data){
     dicts['date'].push(info['date']);
     dicts['num_vaccines'].push(info['series_complete_pop_pct']);
  }

  console.log(dicts);

  var lineChart = [{
    x: dicts['date'],
    y: dicts['num_vaccines'],
    type: 'lines'
  }]

  Plotly.newPlot('LineChart', lineChart);
}


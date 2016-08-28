        var linesData = {
                labels:{{time|safe }},
                datasets: [
                        {
                            
                            label:'Number of People online' ,
                            
                            lineTension: 0.1,
                            backgroundColor: "rgba(255, 0, 123,0.25) ",
                            borderColor: "#FF007B",
                            borderCapStyle: 'butt',
                            borderDash: [],
                            borderDashOffset: 0.0,
                            borderJoinStyle: 'miter',
                            pointBorderColor: "#FF007B",
                            pointBackgroundColor: "#2BFF00",
                            pointBorderWidth: 1,
                            pointHoverRadius: 5,
                            pointHoverBackgroundColor: "#2BFF00",
                            pointHoverBorderColor: "#2BFF00",
                            pointHoverBorderWidth: 2,
                            pointRadius: 1,
                            pointHitRadius: 10,
                            data: {{number}},
                            
                        }
                ]
        };

        window.onload = function(){
            var ctx1 = document.getElementById("chart-area-bar").getContext("2d");
            Chart.defaults.global.title.fontSize =20
            Chart.defaults.global.elements.point.borderColor="#2BFF00"
            var myLines= new Chart.Line(ctx1, {
                    
                    data: linesData,
                    options:{
                                title: {
                                    display: true,
                                    text: 'People online'
                                    }
                            }
                    });
        };
        

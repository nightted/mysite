{% include "home.html" %}
window.onload = function()
{
    
    var linesData = {
                labels:{{time}},
                datasets: [
                        {
                            
                            label:'' ,
                            
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
                            data: {{number_people}},
                            
                        }
                ]
        };

    var BarData = {
                labels: ["原味", "抹茶紅豆", "芝麻", "蔓越莓"],
                datasets: [
                    {
                           label: "",
                           backgroundColor: [
                                'rgba(255, 191,0,0.2)',
                                'rgba(4, 255, 0,0.2)',
                                'rgba(91,91,91,0.5)',
                                'rgba(255, 0, 89,0.2)',
                            ],
                            borderColor: [
                                'rgba(255, 191,0,0.2)',
                                'rgba(4, 255, 0,0.2)',
                                'rgba(91,91,91,0.2)',
                                'rgba(255, 0, 89,0.2)',
                            ],
                            borderWidth: 0.5,
                            data: {{number_cake}}, 
                        }
                    ]
                };


            Chart.defaults.global.title.fontSize =20
            Chart.defaults.global.elements.point.borderColor="#2BFF00"

            var ctx1 = document.getElementById("chart-area-line").getContext("2d");
            var myLines= new Chart.Line(ctx1, {
                    data: linesData,
                    options:{
                                title: {
                                    display: true,
                                    text: 'People online',
                                    fontFamily: "cursive",
                                    fontsize: 20,
                                    fontStyle: 'oblique'
                                        }
                                ,scales: {
                                    yAxes: [{
                                        ticks: {
                                            beginAtZero:true,
                                            stepSize:1
                                                }
                                            }],

                                        }
                            }
                    });

            var ctx2 = document.getElementById("chart-area-bar").getContext("2d");  
            var myBars= new Chart.Bar(ctx2, {
                    data:BarData,
                    options:{
                                title: {
                                    display: true,
                                    text: 'What Rabbits Buy !',
                                    fontFamily: "cursive",
                                    fontsize: 20,
                                    fontStyle: 'oblique'
                                    }
                                ,scales: {
                                    yAxes: [{
                                        ticks: {
                                            beginAtZero:true,
                                            stepSize:1
                                                }
                                            }]
                                        }
                            }
                    });
};
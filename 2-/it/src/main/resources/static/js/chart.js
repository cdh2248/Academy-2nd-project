navigator.geolocation.getCurrentPosition((position) => {
    latitude = position.coords.latitude;
    longitude = position.coords.longitude;
}, (err) => {
    console.error('Error getting location:', err);
});

const socket = new WebSocket("ws://localhost:8060");
socket.onopen = () => {
    console.log("웹소켓 연결!");
    const dataToSend = [latitude,longitude];
    socket.send(dataToSend);
    console.log("위도 : " + latitude + "경도 : " + longitude + "전송 완료!")
};
var num = 0;
socket.onmessage = function(event) {
    console.log("파이썬에서 데이터 전달 받음!")


    var time = []
    var temp = []
        var myRainData = JSON.parse(event.data);
        console.log(myRainData)
        var ctx = document.getElementById("chart").getContext("2d");


        for (var i = 0; i < myRainData.length; i++) {
            time.push(myRainData[i].fcstDate)
            temp.push(myRainData[i].기온)
            label.push(time[i]);
            data_1.datasets[0].data.push(temp[i]);

        }
        num+=1
        chart = new Chart(ctx, {
            type: 'line',
            data: data_1,
            options: {
                legend: {
                    display: false
                },
                responsive: false,
                scales: {
                    x: {
                        min: 0,
                        max: 8,
                        // display: true,
                        title: {
                            display: true,
                            text: 'TIME'
                        }
                    },
                    y: {
                        display: true,
                        min: 10,
                        max: 40,
                        title: {
                            // display: true,
                            text: '기온'
                        }
                    },
                }
            }
        });

        var myButton = document.getElementById("my-button");
        myButton.addEventListener('click', () => {

            chart.destroy()

            var ctx = document.getElementById("chart").getContext("2d");

            var data_2 = {
                datasets: [
                    {
                        label: '강수량',
                        yAxisID: 'y-left',
                        data: [],
                        backgroundColor: "#00BFFF",
                        borderColor: "#00BFFF",
                        borderWidth: 1
                    },
                    {
                        label: '강수확률',
                        yAxisID: 'y-right',
                        data: [],
                        backgroundColor: "#1E90FF",
                        borderColor: "#1E90FF",
                        borderWidth: 1
                    },
                ],
                borderWidth: 1,
                labels: label,
            };
            var precipitation = [] // 강수량
            var probability = [] // 강수확률
            for (var i = 0; i < myRainData.length; i++) {
                time.push(myRainData[i].fcstDate)
                precipitation.push(myRainData[i].강수량)
                probability.push(myRainData[i].강수확률)
                label.push(time[i]);
                data_2.datasets[0].data.push(precipitation[i]);
                data_2.datasets[1].data.push(probability[i]);
            }

            chart = new Chart(ctx, {
                type: 'bar',
                data: data_2,
                options: {
                    responsive: false,
                    scales: {
                        x: {
                            min: 0,
                            max: 8,
                            display: true,
                            title: {
                                display: true,
                                text: 'TIME'
                            }
                        },
                        'y-left': {
                            type: 'linear',
                            position: 'left',
                            min: 0,
                            max: 20,
                            title: {
                                display: true,
                                text: '강수량'
                            }
                        },
                        'y-right': {
                            type: 'linear',
                            position: 'right',
                            min: 0,
                            max: 100,
                            title: {
                                display: true,
                                text: '강수확률'
                            }
                        },
                    }
                }
            });
            console.log("고맙다")
            chart.update();
        });

        var myButton2 = document.getElementById("my-button2");
        myButton2.addEventListener('click', () => {

            chart.destroy()

            var ctx = document.getElementById("chart").getContext("2d");

            var time = []
            var temp = []

            for (var i = 0; i < myRainData.length; i++) {
                time.push(myRainData[i].fcstDate)
                temp.push(myRainData[i].기온)
                label.push(time[i]);
                data_1.datasets[0].data.push(temp[i]);

            }

            chart = new Chart(ctx, {
                type: 'line',
                data: data_1,
                options: {
                    responsive: false,
                    scales: {
                        x: {
                            min: 0,
                            max: 8,
                            display: true,
                            title: {
                                display: true,
                                text: 'TIME'
                            }
                        },
                        y: {
                            display: true,
                            min: 10,
                            max: 40,
                            title: {
                                display: true,
                                text: '기온'
                            }
                        },
                    }
                }
            });
            console.log("고맙다")
            chart.update();
        });

        function scroller(scroll, chart) {

            const dataLength = label.length
            if (scroll.deltaY > 0) {
                chart.options.scales.x.min += 1
                chart.options.scales.x.max += 1

                if (chart.options.scales.x.max >= dataLength) {
                    chart.options.scales.x.min = dataLength - 9;
                    chart.options.scales.x.max = dataLength;
                }
            } else if (scroll.deltaY < 0) {
                if (chart.options.scales.x.min <= 0) {
                    chart.options.scales.x.min = 0
                    chart.options.scales.x.max = 8
                } else {
                    chart.options.scales.x.min -= 1
                    chart.options.scales.x.max -= 1
                }
                chart.options.scales.x.min -= 1
                chart.options.scales.x.max -= 1
            } else {

            }
            chart.update();
        }

        chart.canvas.addEventListener('wheel', (e) => {
            scroller(e, chart);
        })
        console.log("고맙다")
        i += 1
        chart.update();
    }


    // ===================================================================================================




    label = []
    var data_1 = {
        datasets: [{
            data: [],
            borderColor: function (context) {
                const chart = context.chart;
                const {ctx, chartArea} = chart;
                if (!chartArea) {
                    return;
                }
                return getGradient(ctx, chartArea);
            },
        }],
        borderWidth: 1,
        labels: label,
    };
    document.addEventListener('DOMContentLoaded', function () {
        var ctx = document.getElementById("chart").getContext("2d");
        var rainJson = $('input[name=rainJson]').val()
        rainData = JSON.parse(rainJson)
        var time = []
        var temp = []

        for (var i = 0; i < rainData.length; i++) {
            time.push(rainData[i].fcstDate)
            temp.push(rainData[i].temp)
            label.push(time[i]);
            data_1.datasets[0].data.push(temp[i]);

        }


        chart = new Chart(ctx, {
            type: 'line',
            data: data_1,
            options: {
                responsive: false,
                scales: {
                    x: {
                        min: 0,
                        max: 8,
                        display: true,
                        title: {
                            display: true,
                            text: 'TIME'
                        }
                    },
                    y: {
                        display: true,
                        min: 10,
                        max: 40,
                        title: {
                            display: true,
                            text: '기온'
                        }
                    },
                }
            }
        });
        var myButton = document.getElementById("my-button");
        myButton.addEventListener('click', () => {

            chart.destroy()

            var ctx = document.getElementById("chart").getContext("2d");

            var data_2 = {
                datasets: [
                    {
                        label: '강수량',
                        yAxisID: 'y-left',
                        data: [],
                        backgroundColor: "#00BFFF",
                        borderColor: "#00BFFF",
                        borderWidth: 1
                    },
                    {
                        label: '강수확률',
                        yAxisID: 'y-right',
                        data: [],
                        backgroundColor: "#1E90FF",
                        borderColor: "#1E90FF",
                        borderWidth: 1
                    },
                ],
                borderWidth: 1,
                labels: label,
            };
            var precipitation = [] // 강수량
            var probability = [] // 강수확률
            for (var i = 0; i < rainData.length; i++) {
                time.push(rainData[i].fcstDate)
                precipitation.push(rainData[i].precipitation)
                probability.push(rainData[i].probability)
                label.push(time[i]);
                data_2.datasets[0].data.push(precipitation[i]);
                data_2.datasets[1].data.push(probability[i]);
            }

            chart = new Chart(ctx, {
                type: 'bar',
                data: data_2,
                options: {
                    responsive: false,
                    scales: {
                        x: {
                            min: 0,
                            max: 8,
                            display: true,
                            title: {
                                display: true,
                                text: 'TIME'
                            }
                        },
                        'y-left': {
                            type: 'linear',
                            position: 'left',
                            min: 0,
                            max: 20,
                            title: {
                                display: true,
                                text: '강수량'
                            }
                        },
                        'y-right': {
                            type: 'linear',
                            position: 'right',
                            min: 0,
                            max: 100,
                            title: {
                                display: true,
                                text: '강수확률'
                            }
                        },
                    }
                }
            });
            console.log("고맙다")
            chart.update();
        });

        var myButton2 = document.getElementById("my-button2");
        myButton2.addEventListener('click', () => {

            chart.destroy()

            var ctx = document.getElementById("chart").getContext("2d");

            var time = []
            var temp = []

            for (var i = 0; i < rainData.length; i++) {
                time.push(rainData[i].fcstDate)
                temp.push(rainData[i].temp)
                label.push(time[i]);
                data_1.datasets[0].data.push(temp[i]);

            }

            chart = new Chart(ctx, {
                type: 'line',
                data: data_1,
                options: {
                    responsive: false,
                    scales: {
                        x: {
                            min: 0,
                            max: 8,
                            display: true,
                            title: {
                                display: true,
                                text: 'TIME'
                            }
                        },
                        y: {
                            display: true,
                            min: 10,
                            max: 40,
                            title: {
                                display: true,
                                text: '기온'
                            }
                        },
                    }
                }
            });
            console.log("고맙다")
            chart.update();
        });
        function scroller(scroll, chart) {

            const dataLength = label.length
            if (scroll.deltaY > 0) {
                chart.options.scales.x.min += 1
                chart.options.scales.x.max += 1

                if (chart.options.scales.x.max >= dataLength) {
                    chart.options.scales.x.min = dataLength - 9;
                    chart.options.scales.x.max = dataLength;
                }
            } else if (scroll.deltaY < 0) {
                if (chart.options.scales.x.min <= 0) {
                    chart.options.scales.x.min = 0
                    chart.options.scales.x.max = 8
                } else {
                    chart.options.scales.x.min -= 1
                    chart.options.scales.x.max -= 1
                }
                chart.options.scales.x.min -= 1
                chart.options.scales.x.max -= 1
            } else {

            }
            chart.update();
        }

        chart.canvas.addEventListener('wheel', (e) => {
            scroller(e, chart);
        })
    })

    let width, height, gradient;

    function getGradient(ctx, chartArea) {
        const chartWidth = chartArea.right - chartArea.left;
        const chartHeight = chartArea.bottom - chartArea.top;
        if (!gradient || width !== chartWidth || height !== chartHeight) {
            // Create the gradient because this is either the first render
            // or the size of the chart has changed
            width = chartWidth;
            height = chartHeight;
            gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
            gradient.addColorStop(0, 'blue');
            gradient.addColorStop(0.35, 'yellow');
            gradient.addColorStop(0.75, 'red');
        }

        return gradient;
    };


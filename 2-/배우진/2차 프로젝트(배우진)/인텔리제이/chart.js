label = []
var data_1 = {datasets:[{
        data: [],
        borderColor: function(context) {
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

$(document).ready(function () {
    var ctx = document.getElementById("chart").getContext("2d");

    var chart = new Chart(ctx, {
        type: 'line',
        data:data_1,
        options: {
            responsive: false,
            scales: {
                x: {
                    // min: 0,
                    // max: 8,
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

    const myButton = document.getElementById("my-button");
    myButton.addEventListener('click', () => {
        data_1.datasets[0].data.push(15)
        label.push(15);
        chart.update();
    });

    const socket = new WebSocket("ws://localhost:8060");
    socket.onopen = () => {
        console.log("웹소켓 연결!");
        const dataToSend = [latitude,longitude];
        socket.send(dataToSend);
        console.log("위도 : " + latitude + "경도 : " + longitude + "전송 완료!")
    };

    socket.onmessage = (event) => {
        console.log("날씨 데이터 수집 완료!")

    };

    navigator.geolocation.getCurrentPosition((position) => {
        latitude = position.coords.latitude;
        longitude = position.coords.longitude;
    }, (err) => {
        console.error('Error getting location:', err);
    });



    socket.onmessage = function (event) {
        var data = JSON.parse(event.data);
            var time = []
            var temperature = []

        for (var i = 0; i < data.length; i++) {
            time.push(data[i].fcstDate)
            temperature.push(data[i].기온)
            label.push(time[i]);
            data_1.datasets[0].data.push(temperature[i]);

        }

        chart.update();
    };

});

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

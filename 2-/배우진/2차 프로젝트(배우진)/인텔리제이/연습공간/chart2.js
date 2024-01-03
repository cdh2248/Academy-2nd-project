label = []
var data_1 = {datasets:[{
        data: [],
        borderColor: "blue",
    }],
    borderWidth: 1,
    labels: label,
};

$(document).ready(function () {
    var ctx = document.getElementById("chart").getContext("2d");
    console.log("hi")

    var time = []
    var temp = []


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
});





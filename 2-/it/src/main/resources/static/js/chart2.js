// label = []
// var data_1 = {
//     datasets: [{
//         data: [],
//         borderColor: function (context) {
//             const chart = context.chart;
//             const {ctx, chartArea} = chart;
//             if (!chartArea) {
//                 return;
//             }
//             return getGradient(ctx, chartArea);
//         },
//     }],
//     borderWidth: 1,
//     labels: label,
// };
// document.addEventListener('DOMContentLoaded', function () {
//     var ctx = document.getElementById("chart").getContext("2d");
//     var rainJson = $('input[name=rainJson]').val()
//     rainData = JSON.parse(rainJson)
//     var time = []
//     var temp = []
//
//     for (var i = 0; i < rainData.length; i++) {
//         time.push(rainData[i].fcstDate)
//         temp.push(rainData[i].temp)
//         label.push(time[i]);
//         data_1.datasets[0].data.push(temp[i]);
//
//     }
//
//
//     chart = new Chart(ctx, {
//         type: 'line',
//         data: data_1,
//         options: {
//             responsive: false,
//             scales: {
//                 x: {
//                     min: 0,
//                     max: 8,
//                     display: true,
//                     title: {
//                         display: true,
//                         text: 'TIME'
//                     }
//                 },
//                 y: {
//                     display: true,
//                     min: 10,
//                     max: 40,
//                     title: {
//                         display: true,
//                         text: '기온'
//                     }
//                 },
//             }
//         }
//     });
//
//     function scroller(scroll, chart) {
//
//         const dataLength = label.length
//         if (scroll.deltaY > 0) {
//             chart.options.scales.x.min += 1
//             chart.options.scales.x.max += 1
//
//             if (chart.options.scales.x.max >= dataLength) {
//                 chart.options.scales.x.min = dataLength - 9;
//                 chart.options.scales.x.max = dataLength;
//             }
//         } else if (scroll.deltaY < 0) {
//             if (chart.options.scales.x.min <= 0) {
//                 chart.options.scales.x.min = 0
//                 chart.options.scales.x.max = 8
//             } else {
//                 chart.options.scales.x.min -= 1
//                 chart.options.scales.x.max -= 1
//             }
//             chart.options.scales.x.min -= 1
//             chart.options.scales.x.max -= 1
//         } else {
//
//         }
//         chart.update();
//     }
//
//     chart.canvas.addEventListener('wheel', (e) => {
//         scroller(e, chart);
//     })
// })
//
//
//
//
//
//
// let width, height, gradient;
//
// function getGradient(ctx, chartArea) {
//     const chartWidth = chartArea.right - chartArea.left;
//     const chartHeight = chartArea.bottom - chartArea.top;
//     if (!gradient || width !== chartWidth || height !== chartHeight) {
//         // Create the gradient because this is either the first render
//         // or the size of the chart has changed
//         width = chartWidth;
//         height = chartHeight;
//         gradient = ctx.createLinearGradient(0, chartArea.bottom, 0, chartArea.top);
//         gradient.addColorStop(0, 'blue');
//         gradient.addColorStop(0.35, 'yellow');
//         gradient.addColorStop(0.75, 'red');
//     }
//
//     return gradient;
// };
//

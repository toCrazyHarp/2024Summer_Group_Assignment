var chartDom = document.getElementById('hotchart');
var myChart = echarts.init(chartDom);
var option;
var color=7
function generatePieces(maxValue, colorBox) {
    var pieces = [];
    var quotient = 1;
    var temp = {};
    temp.lt = 1;
    temp.label = '0';
    temp.color = colorBox[0];
    pieces.push(temp);

    if (maxValue && maxValue >= color) {

        quotient = Math.floor(maxValue / color);

        for (var i = 1; i <= color; i++) {
            var temp = {};
            if (i == 1) {
                temp.gte = 1;
            } else {
                temp.gte = quotient * (i - 1);
            }
            temp.lte = quotient * i;
            temp.color = colorBox[i];
            // temp.label = '等级'+i;
            pieces.push(temp);
        }
    }

    return pieces;
}
function getVirtualData(year) {
  const date = +echarts.time.parse(year + '-01-01');
  const end = +echarts.time.parse(+year + 1 + '-01-01');
  const dayTime = 3600 * 24 * 1000;
  const data = [];
  for (let time = date; time < end; time += dayTime) {
    data.push([
      echarts.time.format(time, '{yyyy}-{MM}-{dd}', false),
      Math.floor(Math.random() * 10000)
    ]);
  }
  return data;
}
var maxValue=10000
var colorBox = ['white', '#9de2b5', '#87d2a1', '#70c38c', '#5ab378','#43a464','#2d9450','#16853b'];
option = {
  title: {
    top: 20,
    left: 'left',
    text: '足迹',
      textStyle: {
       fontSize: 40
    }
  },
  tooltip: {},
  visualMap: {
            min: 0,
            max: maxValue,
            type: 'piecewise',
            align: 'left',
            orient: 'horizontal',  //vertical  horizontal
            left: 'left',
            bottom: '30',
            textGap: 5,
            itemGap: 5,
            pieces: generatePieces(maxValue, colorBox)
        },
  calendar: {
    top: 100,
    left: 30,
    right: 30,
    cellSize: ['auto', '16'],
    range: '2016',
    itemStyle: {
      borderWidth: 0.5
    },
    yearLabel: { show: true }
  },
  series: {
    type: 'heatmap',
    coordinateSystem: 'calendar',
    data: getVirtualData('2016')
  }
};

option && myChart.setOption(option);
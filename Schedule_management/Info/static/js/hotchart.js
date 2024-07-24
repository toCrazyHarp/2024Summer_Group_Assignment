var chartDom = document.getElementById('hotchart');
var myChart = echarts.init(chartDom);
var option;
var color=8


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
            max: 50,
            type: 'piecewise',
            align: 'left',
            orient: 'horizontal',  //vertical  horizontal
            left: 'left',
            bottom: '30',
            textGap: 5,
            itemGap: 5,
            pieces: [{gt: 0, lte: 6, color: '#9de2b5'}, // 注意：这里使用了 gt 而不是 lt，因为 lt 已经用于第一个元素

    {gt: 6, lte: 12, color: '#87d2a1'},

    {gt: 12, lte: 18, color: '#70c38c'},

    {gt: 18, lte: 24, color: '#5ab378'},

    {gt: 24, lte: 30, color: '#43a464'},

    {gt: 30, lte: 36, color: '#2d9450'},

    {gt: 36, lte: 42, color: '#16853b'},]
        },
  calendar: {
    top: 100,
    left: 30,
    right: 30,
    cellSize: ['auto', '16'],
    range: '2024',
    itemStyle: {
      borderWidth: 0.5
    },
    yearLabel: { show: false }
  },
  series: {
    type: 'heatmap',
    coordinateSystem: 'calendar',
    data: []
  }
};
option && myChart.setOption(option);

 fetch('/get-data/')
            .then(response => response.json())
            .then(data => {
                // 将数据转换为ECharts需要的时间戳格式
                const newData = data.map(item => [echarts.time.parse(item[0]), item[1]]);
                // 更新图表数据
                myChart.setOption({
                    series: [{
                        data: newData
                    }]
                });
            })
            .catch(error => console.error('Error:', error));

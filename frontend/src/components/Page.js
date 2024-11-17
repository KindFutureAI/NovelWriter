import React from 'react';
import ReactECharts from 'echarts-for-react';

const Page = () => {
  const options = {
    // 设置图表的布局
    // containLabel: true 表示图表的内容不会超出图表的边界
    grid: { top: 25, right: 25, bottom: 25, left: 25, containLabel: true},

    // 设置图表的标题
    title: {
      text: 'ECharts 入门示例',
    },

    // 设置背景颜色为浅灰色
    backgroundColor: 'black',

    // 设置x轴
    xAxis: {
      type: 'category',
      data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
    },

    // 设置y轴
    yAxis: {
      type: 'value',
    },

    // 设置数据
    series: [
      {
        data: [820, 932, 901, 934, 1290, 1330, 1320],
        type: 'line',
        smooth: true,
      },
    ],

    // 设置提示框
    tooltip: {
      trigger: 'axis',
    },
  };
  return <ReactECharts option={options} />;
};
export default Page;

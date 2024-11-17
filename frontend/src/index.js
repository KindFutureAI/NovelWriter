import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Page from './components/Page';
import ChildComponent from './components/ChildComponent';
import MyButton from './components/MyButton';
import MyButton2 from './components/MyButton2';
import Greeting from './components/Greeting';
import FetchApi from './components/FetchApi';
import RouterDemo from './components/RouterDemo';

// 定义一个react组件
const App = (
    <div className="border">
        <h1>Manually React</h1>
        <button>click me</button>
        <p>hello</p>
        
        {/* 引入echarts组件 */}
        <Page />
        <br></br>

        {/* 引入子组件 */}
        <ChildComponent name="张三" age={18} />
        <br></br>
        {/* 引入自定义按钮组件 */}
        <MyButton />
        <br></br>

        <div className='container mt-3'>
            <MyButton text="Default" style="btn-primary mr-3" />
            <MyButton text="Success" style="btn-success mr-3" /> 
            <MyButton2 text="danger" style="danger" />
        </div>
        <br></br>
        {/* 引入输入框组件 */}
        <div className="container">
            <Greeting />
        </div>
        <br></br>

        {/* 引入fetchApi组件 */}
        <FetchApi />
        <br></br>
        <hr></hr>

        {/* 引入路由组件 */}
        {/* <RouterDemo /> */}


    </div>
)

// 渲染组件到页面的root元素中
ReactDOM.createRoot(document.getElementById('root')).render(App);

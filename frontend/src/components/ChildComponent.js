import React from 'react';

const ChildComponent = (props) => {
    // 接收父组件传递的props： props: {name: '张三', age: 18}
    return (<div>
        {/* 使用props */}
        <p>这里是子组件，下面是父组件传递的props</p>
        <ol>
            <li>姓名: {props.name}</li>
            <li>年龄: {props.age}</li>
        </ol>
    </div>);
};

export default ChildComponent;
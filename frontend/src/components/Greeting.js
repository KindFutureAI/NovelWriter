import React, { useState } from 'react';

const Greeting = () => {
    const [name, setName] = useState('张三');

    // 定义一个函数，用于处理输入框的改变: event是事件对象, event.target.value是输入框的值
    function handleChange(event) {
        setName(event.target.value);
    }

    return (
        <div>
            <p>hello, {name}</p>
            {/* 使用input输入框，value绑定name，onChange绑定handleChange函数 */}
            <label>
                <input type="text/babel" placeholder="请输入你的名字" value={name} onChange={handleChange} />
            </label>
            <h3>hello, {name}</h3>
        </div>
    );
};

export default Greeting;
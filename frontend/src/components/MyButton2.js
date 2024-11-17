import React, { useState } from 'react';

const MyButton = ({text, style}) => {
    // 使用useState来定义一个状态变量count，初始值为0
    const [count, setCount] = useState(0);

    // 返回一个按钮，点击按钮时，count的值会增加1
    return (
        <div>
            <button className={`btn_${style}`} text={text} onClick={() => setCount(count + 1)}>
                click me: {count} {text}
            </button>
        </div>
    );
};

export default MyButton;
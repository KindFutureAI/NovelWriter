import React, { useState } from 'react';

const MyButton = () => {
    // 使用useState来定义一个状态变量count，初始值为0
    const [count, setCount] = useState(0);

    // 返回一个按钮，点击按钮时，count的值会增加1
    return (
        <div>
            <button className="my-button" onClick={() => setCount(count + 1)}>
                click me: {count}
            </button>
        </div>
    );
};

export default MyButton;
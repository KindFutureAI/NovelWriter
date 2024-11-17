import React, { useState } from 'react';

const WritingArea = () => {
  const [text, setText] = useState('');

  const handleChange = (e) => {
    setText(e.target.value);
  };

  return (
    <div className="writing-area">
      <h2>小说写作区</h2>
      <textarea
        value={text}
        onChange={handleChange}
        placeholder="在这里写你的小说..."
        rows="10"
        cols="50"
      />
    </div>
  );
};

export default WritingArea;
import React, { useState } from 'react';

const ChatHistory = ({ history }) => {
  return (
    <div className="chat-history">
      <h2>历史对话</h2>
      <ul>
        {history.map((entry, index) => (
          <li key={index}>
            <strong>{entry.agentName}:</strong> {entry.message}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ChatHistory;
import React, { useState } from 'react';

const AgentChatBox = ({ agentName, messages }) => {
  return (
    <div className="chat-box">
      <h3>{agentName}</h3>
      <div className="messages">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.type}`}>
            <strong>{msg.sender}:</strong> {msg.content}
          </div>
        ))}
      </div>
    </div>
  );
};

export default AgentChatBox;
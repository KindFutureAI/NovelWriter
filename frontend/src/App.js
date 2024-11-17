import React, { useState } from 'react';
import './styles.css';
import WritingArea from './components/WritingArea';
import AgentChatBox from './components/AgentChatBox';
import ChatHistory from './components/ChatHistory';
import MaterialLibrary from './components/MaterialLibrary';
import AgentStatus from './components/AgentStatus';

const APP = () => {
  const [messages, setMessages] = useState([
    { sender: 'Manager', content: '开始新的任务...', type: 'manager' },
    { sender: 'Expert', content: '提供专业知识支持...', type: 'expert' },
    { sender: 'Senior', content: '处理复杂任务...', type: 'senior' },
    { sender: 'Junior1', content: '处理基础任务...', type: 'junior' },
    { sender: 'Junior2', content: '处理基础任务...', type: 'junior' },
  ]);

  const [history, setHistory] = useState([]);

  const [agents, setAgents] = useState([
    { name: 'Manager', status: '在线', task: '分配任务' },
    { name: 'Expert', status: '在线', task: '提供专业知识' },
    { name: 'Senior', status: '在线', task: '处理复杂任务' },
    { name: 'Junior1', status: '在线', task: '处理基础任务' },
    { name: 'Junior2', status: '在线', task: '处理基础任务' },
  ]);

  const addMessage = (sender, content, type) => {
    const newMessage = { sender, content, type };
    setMessages([...messages, newMessage]);
    setHistory([...history, { agentName: sender, message: content }]);
  };

  return (
    <div className="app">
      <h1>小说写作智能体系统</h1>
      <div className="main-content">
        <div className="left-panel">
          <WritingArea />
          <MaterialLibrary />
        </div>
        <div className="right-panel">
          <AgentChatBox agentName="Manager" messages={messages.filter(msg => msg.type === 'manager')} />
          <AgentChatBox agentName="Expert" messages={messages.filter(msg => msg.type === 'expert')} />
          <AgentChatBox agentName="Senior" messages={messages.filter(msg => msg.type === 'senior')} />
          <AgentChatBox agentName="Junior1" messages={messages.filter(msg => msg.type === 'junior' && msg.sender === 'Junior1')} />
          <AgentChatBox agentName="Junior2" messages={messages.filter(msg => msg.type === 'junior' && msg.sender === 'Junior2')} />
          <ChatHistory history={history} />
        </div>
      </div>
      <AgentStatus agents={agents} />
    </div>
  );
};

export default APP;
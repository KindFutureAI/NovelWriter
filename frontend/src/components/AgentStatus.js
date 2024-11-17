import React from 'react';

const AgentStatus = ({ agents }) => {
  return (
    <div className="agent-status">
      <h2>智能体工作情况</h2>
      <table>
        <thead>
          <tr>
            <th>智能体</th>
            <th>状态</th>
            <th>任务</th>
          </tr>
        </thead>
        <tbody>
          {agents.map((agent, index) => (
            <tr key={index}>
              <td>{agent.name}</td>
              <td>{agent.status}</td>
              <td>{agent.task || '无'}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default AgentStatus;
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/agents/';

export const getAgents = async () => {
  // 模拟异步请求: 使用GET 请求从服务器获取数据
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching agents:', error);
    throw error;
  }
};

export const createAgent = async (agentData) => {
  // 模拟异步请求：使用POST请求将数据发送到服务器
  try {
    const response = await axios.post(API_URL, agentData);
    return response.data;
  } catch (error) {
    console.error('Error creating agent:', error);
    throw error;
  }
};

// 其他CRUD操作...
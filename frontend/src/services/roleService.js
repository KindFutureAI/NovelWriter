import axios from 'axios';

const API_URL = 'http://localhost:8000/api/roles/';

export const getRoles = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    console.error('Error fetching roles:', error);
    throw error;
  }
};

export const createRole = async (roleData) => {
  try {
    const response = await axios.post(API_URL, roleData);
    return response.data;
  } catch (error) {
    console.error('Error creating role:', error);
    throw error;
  }
};

// 其他CRUD操作...
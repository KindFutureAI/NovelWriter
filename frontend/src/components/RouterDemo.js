import React, { createContext, useState, useContext, useEffect } from 'react';
import { BrowserRouter, Route, Link, Routes } from 'react-router-dom';

// 创建一个UserContext的上下文，用于在组件之间共享用户信息
export const UserContext = createContext();

// 创建一个简单的用户列表（实际中应从后台服务获取）
const users = [
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' },
  { id: 3, name: 'Charlie' },
];

// 用户页面组件，负责显示单个用户的详细信息
const UserPage = ({ userId }) => {
  const [user, setUser] = useState(null); // 定义一个user状态，初始值为null

  // 在组件挂载时，从用户列表中查找对应的用户信息并设置到本地状态
  useEffect(() => {
    // 使用find方法查找用户信息; u => u.id === userId 含义是: u 是 users 数组中的一个元素，u.id 是 u 对象的 id 属性，u.id === userId 是判断 u.id 是否等于 userId
    // 这里的 u 从何而来：是find方法的参数，find方法的参数是一个函数，这个函数有一个参数u，这个参数u就是users数组中的一个元素
    const user = users.find(u => u.id === userId);  
    setUser(user);
  }, [userId]);

  // 判断是否已成功获取用户信息
  if (!user) {
    return <div>Loading...</div>;
  }

  // 显示用户信息
  return (
    <div>
      <h1>{user.name}</h1>
      <p>ID: {user.id}</p>
    </div>
  );
};

// 用户列表页面组件，负责显示所有用户的概要信息
const UsersPage = () => {
  return (
    <div>
      <h1>Users</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            <Link to={`/users/${user.id}`}>{user.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

// 应用程序启动组件
const RouterDemo = () => {
  const [user, setUser] = useState(null);

  // 用户登录函数，将用户信息存储到上下文中
  const login = ({ id, name }) => {
    setUser({ id, name });
  };

  // 用户登出函数，将用户信息从上下文中清除
  const logout = () => {
    setUser(null);
  };

  // 渲染应用程序，包括页面导航、用户信息和路由处理
  return (
    <BrowserRouter>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/users">Users</Link>
          </li>
        </ul>
      </nav>
      <UserContext.Provider value={{ user, login, logout }}>
        <div>
          {user ? (
            <p>
              Logged in as <b>{user.name}</b>. <button onClick={logout}>Logout</button>
            </p>
          ) : (
            <p>
              <Link to="/login">Login</Link>
            </p>
          )}
          <Routes>
            <Route path="/" element={<h1>Welcome to My App</h1>} />
            <Route path="/login" element={<LoginForm />} />
            <Route path="/users" element={<UsersPage />} />
            <Route path="/users/:userId" element={<UserPage />} />
          </Routes>
        </div>
      </UserContext.Provider>
    </BrowserRouter>
  );
};

// 登录表单组件，负责接收用户输入并处理登录逻辑
const LoginForm = () => {
  const { login } = useContext(UserContext);
  const [formData, setFormData] = useState({ name: '张三' });

  const handleChange = e => {
  // ...展开语法，用于展开对象，数组，不确定参数等
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = e => {
    e.preventDefault();
    login({ id: 123, name: formData.name });
    setFormData({ name: '' });
  };

  return (
    <div>
      <h1>Login</h1>
      <form onSubmit={handleSubmit}>
        <label>
          Name:
          <input type="text" name="name" value={formData.name} onChange={handleChange} />
        </label>
        <button type="submit">Login</button>
      </form>
    </div>
  );
};

export default RouterDemo;

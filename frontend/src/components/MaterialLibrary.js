import React, { useState } from 'react';
// import '../styles.css';

const MaterialLibrary = () => {
  const [materials, setMaterials] = useState([]);
  const [newMaterial, setNewMaterial] = useState('');

  const addMaterial = () => {
    if (newMaterial.trim() !== '') {
      setMaterials([...materials, newMaterial]);
      setNewMaterial('');
    }
  };

  return (
    <div className="material-library">
      <h2>素材库</h2>
      <input
        type="text"
        value={newMaterial}
        onChange={(e) => setNewMaterial(e.target.value)}
        placeholder="输入新素材"
      />
      <button onClick={addMaterial}>添加素材</button>
      <ul>
        {materials.map((material, index) => (
          <li key={index}>{material}</li>
        ))}
      </ul>
    </div>
  );
};

export default MaterialLibrary;
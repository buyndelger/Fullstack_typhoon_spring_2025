import React from 'react';

import './App.css'; // Энгийн загварчлал нэмж болно
import CourseListPage from './pages/courseListPage';

function App() {
  return (
    <div className="App">
      <header className="App-header">
         {/* Энд Routing хийж болно */}
        <CourseListPage />
      </header>
    </div>
  );
}

export default App;

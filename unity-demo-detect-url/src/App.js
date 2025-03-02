import React from 'react';
import { BrowserRouter as Router, Routes } from 'react-router-dom';
import { Alert, Spinner } from './components';
import createRoutes from './components/routes/createRoutes'
import routesConfig from './components/routes/routesConfig';
function AppContent() {

  return (
    <div className="">
      <div className='!fixed z-20 top-0 right-0 left-0'>
        <Alert />
        <Spinner />
      </div>
      <Routes>
        {createRoutes(routesConfig)}
      </Routes>
    </div>
  );
}

function App() {
  return (
    <Router>
      <AppContent />
    </Router>
  );
}

export default App;

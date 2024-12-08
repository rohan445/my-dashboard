import React from "react";
import DashboardLayout from "./DashboardLayout";
import AnalyticsDashboard from "./AnalyticsDashboard";
import './custom.css';

const App = () => {
  return (
    <DashboardLayout>
      <AnalyticsDashboard />
    </DashboardLayout>
  );
};

export default App;

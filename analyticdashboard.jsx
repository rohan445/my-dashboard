import React from "react";
import { Line } from "react-chartjs-2";
import { Box, Typography } from "@mui/material";

const AnalyticsDashboard = () => {
  const data = {
    labels: ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    datasets: [
      {
        label: "Traffic",
        data: [1200, 1500, 1400, 1800, 2200, 2000, 2500],
        backgroundColor: "rgba(75,192,192,0.4)",
        borderColor: "rgba(75,192,192,1)",
        borderWidth: 2,
      },
    ],
  };

  return (
    <Box>
      <Typography variant="h6" gutterBottom>
        Website Analytics
      </Typography>
      <Line data={data} />
    </Box>
  );
};

export default AnalyticsDashboard;

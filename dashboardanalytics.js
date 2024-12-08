import React from "react";
import { Box, Drawer, List, ListItem, Toolbar, Typography } from "@mui/material";

const DashboardLayout = ({ children }) => {
  return (
    <Box sx={{ display: "flex" }}>
      {/* Sidebar */}
      <Drawer variant="permanent" sx={{ width: 240, flexShrink: 0 }}>
        <Toolbar />
        <Box sx={{ overflow: "auto" }}>
          <List>
            {["Analytics", "CRM", "Ecommerce", "Academy", "Logistics"].map((text) => (
              <ListItem button key={text}>
                <Typography>{text}</Typography>
              </ListItem>
            ))}
          </List>
        </Box>
      </Drawer>

      {/* Main Content */}
      <Box component="main" sx={{ flexGrow: 1, p: 3 }}>
        <Toolbar />
        {children}
      </Box>
    </Box>
  );
};

export default DashboardLayout;

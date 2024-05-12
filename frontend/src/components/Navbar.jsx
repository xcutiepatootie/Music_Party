import React from "react";
import { AppBar, Toolbar, Box, Typography } from "@mui/material";

const Navbar = () => {
  return (
    <Box sx={{ width: "100%", margin: 0 }}>
      <AppBar color="primary_g" position="sticky" sx={{ width: "100%", margin: 0 }}>
        <Toolbar>
          <Typography variant="h6" component="" sx={{ flexGrow: 1 }}>
            Test
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
};

export default Navbar;

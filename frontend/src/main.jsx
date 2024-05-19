import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";
import Navbar from "./components/Navbar.jsx";
import { Box, Stack, ThemeProvider } from "@mui/material";
import { theme } from "./utils/CustomTheme.js";
import Footer from "./components/Footer.jsx";

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <Box
        sx={{
          display: "flex",
          flexDirection: "column",
          minHeight: "100vh",
        }}
      >
        <Navbar />
        <App />
        <Footer />
      </Box>
    </ThemeProvider>
  </React.StrictMode>
);

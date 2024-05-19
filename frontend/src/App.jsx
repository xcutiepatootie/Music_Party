import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import Navbar from "./components/Navbar";
import { Box } from "@mui/material";
import SignIn from "./components/Signin/SignIn";

function App() {
  return (
    <Box p={4}>
      <SignIn />
    </Box>
  );
}

export default App;

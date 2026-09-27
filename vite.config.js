import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
import tailwindcss from "@tailwindcss/vite";

// Served from https://julianschelb.github.io/latin-edit-script-review/
export default defineConfig({
  base: "/latin-edit-script-review/",
  plugins: [react(), tailwindcss()],
});

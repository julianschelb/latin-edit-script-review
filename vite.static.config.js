import { defineConfig, mergeConfig } from "vite";
import base from "./vite.config.js";

// The static build (scripts/static_build.py): relative paths and one classic script, so the page runs from a local
// folder without a server; the records are inlined as data/records.js.
export default mergeConfig(base, defineConfig({
  base: "./",
  build: { modulePreload: false, rollupOptions: { output: { format: "iife", inlineDynamicImports: true } } },
}));

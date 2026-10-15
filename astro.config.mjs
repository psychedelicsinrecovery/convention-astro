import { defineConfig } from "astro/config";

// Served from the PIR hub origin as a project page: psychedelicsinrecovery.github.io/convention-astro
const BASE = "/convention-astro";

export default defineConfig({
  site: "https://psychedelicsinrecovery.github.io",
  base: BASE,
  trailingSlash: "never",
});

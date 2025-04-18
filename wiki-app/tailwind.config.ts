import type { Config } from "tailwindcss";
import daisyui from "daisyui";

const config: Config = {
  content: ["./django/templates/**/*.html", "./django/**/templates/**/*.html"],
  darkMode: "media",
  theme: {
    extend: {},
  },
  plugins: [daisyui],
  daisyui: {
    themes: ["light", "dark"],
  },
};

export default config;
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    // Escuchar en todas las interfaces de red (necesario para acceso remoto via Tailscale)
    host: '0.0.0.0',
    port: 5173,
    // Proxy para desarrollo: redirige /api al backend FastAPI local
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})

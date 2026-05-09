import React from 'react';
import { Box, Typography, Button, Container, Paper } from '@mui/material';
import { ArrowLeft, Download } from 'lucide-react';
import { useNavigate, useParams, useLocation } from 'react-router-dom';

const ExpandChartPage: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const { chartId } = useParams<{ chartId: string }>();

  // This page would ideally receive the data and config via state or context
  const { title, children } = location.state || { title: 'Gráfico', children: null };

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Box sx={{ mb: 4, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
          <Button
            startIcon={<ArrowLeft size={20} />}
            onClick={() => navigate(-1)}
            variant="text"
          >
            Volver al Dashboard
          </Button>
          <Typography variant="h4" sx={{ fontWeight: 800 }}>{title}</Typography>
        </Box>
        <Button
          variant="contained"
          startIcon={<Download size={20} />}
          sx={{ borderRadius: 3, px: 3 }}
        >
          Descargar Informe
        </Button>
      </Box>

      <Paper sx={{ p: 4, borderRadius: 6, minHeight: 600 }}>
        {children || <Typography>Contenido no disponible</Typography>}
      </Paper>
    </Container>
  );
};

export default ExpandChartPage;

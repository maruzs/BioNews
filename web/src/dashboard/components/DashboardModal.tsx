import React from 'react';
import {
  Dialog, DialogTitle, DialogContent, Box, IconButton,
  Typography, Button, Stack
} from '@mui/material';
import { X, Download, ExternalLink } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

interface DashboardModalProps {
  open: boolean;
  onClose: () => void;
  title: string;
  children: React.ReactNode;
  onExport?: (format: 'png' | 'svg') => void;
  onOpenPage?: () => void;
}

const DashboardModal: React.FC<DashboardModalProps> = ({
  open,
  onClose,
  title,
  children,
  onExport,
  onOpenPage
}) => {
  return (
    <AnimatePresence>
      {open && (
        <Dialog
          open={open}
          onClose={onClose}
          maxWidth="lg"
          fullWidth
          slotProps={{
            paper: {
              component: motion.div,
              initial: { opacity: 0, scale: 0.9, y: 20 },
              animate: { opacity: 1, scale: 1, y: 0 },
              exit: { opacity: 0, scale: 0.9, y: 20 },
              transition: { type: 'spring', damping: 25, stiffness: 300 },
              sx: {
                borderRadius: 6,
                overflow: 'hidden',
                bgcolor: 'background.paper',
              }
            } as any
          }}
        >
      <DialogTitle sx={{
        m: 0,
        p: 3,
        display: 'flex',
        justifyContent: 'space-between',
        alignItems: 'center',
        borderBottom: '1px solid',
        borderColor: 'divider'
      }}>
        <Typography variant="h6" sx={{ fontWeight: 800 }}>{title}</Typography>
        <Stack direction="row" spacing={1}>
          {onExport && (
            <Button
              startIcon={<Download size={18} />}
              variant="outlined"
              size="small"
              onClick={() => onExport('png')}
              sx={{ borderRadius: 2 }}
            >
              Exportar
            </Button>
          )}
          {onOpenPage && (
            <Button
              startIcon={<ExternalLink size={18} />}
              variant="outlined"
              size="small"
              onClick={onOpenPage}
              sx={{ borderRadius: 2 }}
            >
              Abrir Página
            </Button>
          )}
          <IconButton onClick={onClose} sx={{ color: 'text.secondary' }}>
            <X size={24} />
          </IconButton>
        </Stack>
      </DialogTitle>
      <DialogContent sx={{ p: 4, minHeight: 500, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
        <Box sx={{ width: '100%', height: '100%', minHeight: 400 }}>
          {children}
        </Box>
      </DialogContent>
      </Dialog>
      )}
    </AnimatePresence>
  );
};

export default DashboardModal;

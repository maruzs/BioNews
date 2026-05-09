import { normalizeLabel } from './normalizeLabels';
import type { ChartDataPoint, DimensionConfig } from '../types/dashboard';

export const aggregateData = (data: any[], dim: DimensionConfig): ChartDataPoint[] => {
  if (!data || data.length === 0) return [];

  const counts: Record<string, any> = {};
  
  if (dim.type === 'grouped-vertical' && dim.groupField) {
    data.forEach(item => {
      const primary = normalizeLabel(item[dim.key], dim.key);
      const secondary = normalizeLabel(item[dim.groupField!], dim.groupField!);
      if (!counts[primary]) counts[primary] = { name: primary };
      counts[primary][secondary] = (counts[primary][secondary] || 0) + 1;
      counts[primary].total = (counts[primary].total || 0) + 1;
    });
    return Object.values(counts).sort((a, b) => a.name.localeCompare(b.name));
  }

  data.forEach(item => {
    const val = normalizeLabel(item[dim.key], dim.key);
    counts[val] = (counts[val] || 0) + 1;
  });

  const total = data.length;
  const result = Object.entries(counts).map(([name, count]) => ({
    name,
    count: count as number,
    percentage: Number(((count / total) * 100).toFixed(1))
  }));

  // Sorting based on type
  if (dim.type === 'bar-horizontal' || dim.type === 'relative-bar') {
    return result.sort((a, b) => b.count - a.count);
  }
  
  // Year sorting (numeric if possible)
  if (dim.key.toLowerCase().includes('anio') || dim.key.toLowerCase().includes('año')) {
    return result.sort((a, b) => a.name.localeCompare(b.name, undefined, { numeric: true }));
  }

  return result.sort((a, b) => b.count - a.count);
};

export const exportToImage = async (elementId: string, filename: string, format: 'png' | 'svg' = 'png') => {
  const element = document.getElementById(elementId);
  if (!element) return;

  const svg = element.querySelector('svg');
  if (!svg) return;

  const svgData = new XMLSerializer().serializeToString(svg);
  
  if (format === 'svg') {
    const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(svgBlob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `${filename}.svg`;
    link.click();
    return;
  }

  // PNG Export
  const canvas = document.createElement('canvas');
  const img = new Image();
  const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
  const url = URL.createObjectURL(svgBlob);

  img.onload = () => {
    canvas.width = img.width * 2; // High DPI
    canvas.height = img.height * 2;
    const ctx = canvas.getContext('2d');
    if (ctx) {
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvas.width, canvas.height);
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      const pngUrl = canvas.toDataURL('image/png');
      const downloadLink = document.createElement('a');
      downloadLink.href = pngUrl;
      downloadLink.download = `${filename}.png`;
      downloadLink.click();
    }
    URL.revokeObjectURL(url);
  };
  img.src = url;
};

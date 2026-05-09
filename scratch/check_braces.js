import fs from 'fs';
const content = fs.readFileSync('c:\\Users\\maria\\Desktop\\BioNews\\web\\src\\components\\AdvancedDashboard.tsx', 'utf8');
let open = 0;
for (let i = 0; i < content.length; i++) {
  if (content[i] === '{') open++;
  if (content[i] === '}') open--;
}
console.log('Final open braces:', open);

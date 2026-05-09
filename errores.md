(.venv) PS C:\Users\maria\Desktop\BioNews\web> npm run build

> web@0.0.0 build
> tsc -b && vite build

src/components/DGAConsultasPage.tsx:2:77 - error TS6133: 'Filter' is declared but its value is never read.

2 import { Search, ExternalLink, X, HelpCircle, Pencil, ClipboardList, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';

    ~~~~~~

src/components/DGAConsultasPage.tsx:2:85 - error TS6133: 'ChevronDown' is declared but its value is never read.

2 import { Search, ExternalLink, X, HelpCircle, Pencil, ClipboardList, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';

            ~~~~~~~~~~~

src/components/DGAConsultasPage.tsx:2:98 - error TS6133: 'ChevronUp' is declared but its value is never read.

2 import { Search, ExternalLink, X, HelpCircle, Pencil, ClipboardList, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';

                         ~~~~~~~~~

src/components/DGAConsultasPage.tsx:2:109 - error TS6133: 'LayoutDashboard' is declared but its value is never read.

2 import { Search, ExternalLink, X, HelpCircle, Pencil, ClipboardList, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';

                                    ~~~~~~~~~~~~~~~

src/components/DGAConsultasPage.tsx:2:126 - error TS6133: 'BookOpen' is declared but its value is never read.

2 import { Search, ExternalLink, X, HelpCircle, Pencil, ClipboardList, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';

                                                     ~~~~~~~~

src/components/DGAConsultasPage.tsx:23:10 - error TS6133: 'showFilters' is declared but its value is never read.

23 const [showFilters, setShowFilters] = useState(false);
~~~~~~~~~~~

src/components/DGAConsultasPage.tsx:23:23 - error TS6133: 'setShowFilters' is declared but its value is never read.

23 const [showFilters, setShowFilters] = useState(false);
~~~~~~~~~~~~~~

src/components/DGAConsultasPage.tsx:24:10 - error TS6133: 'activeTab' is declared but its value is never read.

24 const [activeTab, setActiveTab] = useState('reporte');
~~~~~~~~~

src/components/DGAConsultasPage.tsx:24:21 - error TS6133: 'setActiveTab' is declared but its value is never read.

24 const [activeTab, setActiveTab] = useState('reporte');
~~~~~~~~~~~~

src/components/DGAConsultasPage.tsx:32:9 - error TS6133: 'resetFilters' is declared but its value is never read.

32 const resetFilters = () => {
~~~~~~~~~~~~

src/components/MINSALConsultasPage.tsx:2:64 - error TS6133: 'Filter' is declared but its value is never read.

2 import { Search, Calendar, FileText, X, Info, Download, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';  
 ~~~~~~

src/components/MINSALConsultasPage.tsx:2:72 - error TS6133: 'ChevronDown' is declared but its value is never read.

2 import { Search, Calendar, FileText, X, Info, Download, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';  
 ~~~~~~~~~~~

src/components/MINSALConsultasPage.tsx:2:85 - error TS6133: 'ChevronUp' is declared but its value is never read.

2 import { Search, Calendar, FileText, X, Info, Download, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';

            ~~~~~~~~~

src/components/MINSALConsultasPage.tsx:2:113 - error TS6133: 'BookOpen' is declared but its value is never read.

2 import { Search, Calendar, FileText, X, Info, Download, Heart, Filter, ChevronDown, ChevronUp, LayoutDashboard, BookOpen } from 'lucide-react';

                                        ~~~~~~~~

src/components/MINSALConsultasPage.tsx:31:10 - error TS6133: 'showFilters' is declared but its value is never read.

31 const [showFilters, setShowFilters] = useState(false);
~~~~~~~~~~~

src/components/MINSALConsultasPage.tsx:31:23 - error TS6133: 'setShowFilters' is declared but its value is never read.

31 const [showFilters, setShowFilters] = useState(false);
~~~~~~~~~~~~~~

src/components/MINSALConsultasPage.tsx:32:21 - error TS6133: 'setActiveTab' is declared but its value is never read.

32 const [activeTab, setActiveTab] = useState('reporte');
~~~~~~~~~~~~

src/components/MINSALConsultasPage.tsx:42:9 - error TS6133: 'resetFilters' is declared but its value is never read.

42 const resetFilters = () => {
~~~~~~~~~~~~

src/components/MMAConsultasPage.tsx:30:21 - error TS6133: 'setActiveTab' is declared but its value is never read.

30 const [activeTab, setActiveTab] = useState('reporte');
~~~~~~~~~~~~

src/components/MMAConsultasPage.tsx:42:9 - error TS6133: 'resetFilters' is declared but its value is never read.

42 const resetFilters = () => {
~~~~~~~~~~~~

src/components/NewsPage.tsx:85:9 - error TS6133: 'handleSourceChange' is declared but its value is never read.

85 const handleSourceChange = (source: string) => {
~~~~~~~~~~~~~~~~~~

src/dashboard/components/AnnualChart.tsx:6:20 - error TS6133: 'alpha' is declared but its value is never read.

6 import { useTheme, alpha } from '@mui/material';
~~~~~

src/dashboard/components/AnnualChart.tsx:24:9 - error TS6133: 'colors' is declared but its value is never read.

24 const { colors } = useDashboardTheme();
~~~~~~~~~~

src/dashboard/components/AnnualChart.tsx:26:9 - error TS6133: 'activeValue' is declared but its value is never read.

26 const activeValue = filters[filterKey as keyof typeof filters];  
 ~~~~~~~~~~~

src/dashboard/components/AnnualChart.tsx:58:62 - error TS7053: Element implicitly has an 'any' type because expression of type 'string' can't be used to index type 'Props'.
No index signature with a parameter of type 'string' was found on type 'Props'.

58 onClick={(entry) => toggleFilter(filterKey as any, entry[xAxisKey])}
~~~~~~~~~~~~~~~

src/dashboard/components/DashboardTooltip.tsx:17:9 - error TS6133: 'theme' is declared but its value is never read.

17 const theme = useTheme();
~~~~~

src/dashboard/components/ExpandChartPage.tsx:9:9 - error TS6133: 'chartId' is declared but its value is never read.

9 const { chartId } = useParams<{ chartId: string }>();
~~~~~~~~~~~

src/dashboard/components/GroupedBarChart.tsx:6:10 - error TS6133: 'Box' is declared but its value is never read.

6 import { Box, useTheme } from '@mui/material';
~~~

src/dashboard/components/GroupedBarChart.tsx:71:64 - error TS7053: Element implicitly has an 'any' type because expression of type 'string' can't be used to index type 'BarRectangleItem'.
No index signature with a parameter of type 'string' was found on type 'BarRectangleItem'.

71 onClick={(entry) => toggleFilter(filterKey as any, entry[xAxisKey])}
~~~~~~~~~~~~~~~

src/dashboard/components/PieDonutChart.tsx:3:10 - error TS6133: 'Box' is declared but its value is never read.

3 import { Box, useTheme, alpha } from '@mui/material';
~~~

src/dashboard/components/PieDonutChart.tsx:17:9 - error TS6133: 'theme' is declared but its value is never read.

17 const theme = useTheme();
~~~~~

src/dashboard/components/PieDonutChart.tsx:31:62 - error TS2345: Argument of type 'string | undefined' is not assignable to parameter of type 'string | null'.
Type 'undefined' is not assignable to type 'string | null'.

31 onClick={(entry) => toggleFilter(filterKey as any, entry.name)}
~~~~~~~~~~

src/dashboard/components/RelativeBarPanel.tsx:14:62 - error TS6133: 'title' is declared but its value is never read.

14 const RelativeBarPanel: React.FC<RelativeBarPanelProps> = ({ title, data, filterKey }) => {
~~~~~

src/dashboard/components/RelativeBarPanel.tsx:24:26 - error TS6133: 'index' is declared but its value is never read.

24 {data.map((item, index) => {
~~~~~

src/dashboard/DashboardManager.tsx:1:27 - error TS6133: 'useMemo' is declared but its value is never read.

1 import React, { useState, useMemo } from 'react';
~~~~~~~

src/dashboard/DashboardManager.tsx:2:48 - error TS6133: 'useTheme' is declared but its value is never read.

2 import { Box, Grid, Typography, Button, Stack, useTheme, alpha } from '@mui/material';
~~~~~~~~

src/dashboard/DashboardManager.tsx:3:27 - error TS6133: 'FilterX' is declared but its value is never read.

3 import { LayoutDashboard, FilterX, Download, ExternalLink, RefreshCcw } from 'lucide-react';
~~~~~~~

src/dashboard/DashboardManager.tsx:3:36 - error TS6133: 'Download' is declared but its value is never read.

3 import { LayoutDashboard, FilterX, Download, ExternalLink, RefreshCcw } from 'lucide-react';
~~~~~~~~

src/dashboard/DashboardManager.tsx:3:46 - error TS6133: 'ExternalLink' is declared but its value is never read.

3 import { LayoutDashboard, FilterX, Download, ExternalLink, RefreshCcw } from 'lucide-react';
~~~~~~~~~~~~

src/dashboard/DashboardManager.tsx:32:34 - error TS6133: 'height' is declared but its value is never read.

32 const renderChart = (dim: any, height: number | string = '100%') => {
~~~~~~

src/dashboard/hooks/useDashboardFilters.ts:4:1 - error TS6133: 'DashboardFilters' is declared but its value is never read.

4 import { DashboardFilters } from '../types/dashboard';

```

src/dashboard/hooks/useDashboardFilters.ts:4:10 - error TS1484: 'DashboardFilters' is a type and must be imported using a type-only import when 'verbatimModuleSyntax' is enabled.

4 import { DashboardFilters } from '../types/dashboard';
         ~~~~~~~~~~~~~~~~


Found 42 errors.
```

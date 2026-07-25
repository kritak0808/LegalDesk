'use client';

import React from 'react';
import { motion } from 'framer-motion';
import {
  Briefcase,
  Search,
  FileText,
  ShieldCheck,
  Building2,
  Users,
  KeyRound,
  Laptop,
  UserCheck,
  Command,
  Sun,
  Moon,
  PanelLeft,
  PanelRight,
  Sparkles,
  BookOpen,
  RefreshCw,
  GitBranch,
  Network,
  Cpu,
  BrainCircuit,
  Gavel,
  ShieldAlert,
  Calendar,
  FileSpreadsheet,
  Grid,
  Landmark,
  Bot,
  FileCheck2,
  Library,
  Bookmark,
  FileSearch,
  Workflow,
  CheckSquare,
  Zap,
  Crown,
  TrendingUp,
  PieChart,
  Brain,
  BarChart3,
  Link2,
  Mail,
  PenTool,
  Radio,
  Activity,
  Shield,
  Gauge,
  Server,
  Database,
} from 'lucide-react';
import { useWorkspaceStore, WorkspaceViewMode } from '@/store/useWorkspaceStore';
import { useThemeStore } from '@/store/useThemeStore';
import { cn } from '@/lib/utils';

interface NavItem {
  id: WorkspaceViewMode;
  label: string;
  icon: React.ElementType;
  badge?: string;
}

const navItems: NavItem[] = [
  { id: 'operations_center', label: 'Platform Ops', icon: Activity, badge: '99.99%' },
  { id: 'security_operations', label: 'SOC Security', icon: Shield },
  { id: 'observability_studio', label: 'Observability', icon: Gauge },
  { id: 'job_monitoring', label: 'Celery Queues', icon: Server },
  { id: 'executive_command_center', label: 'Executive HQ', icon: Crown },
  { id: 'matters', label: 'Matter Canvas', icon: Briefcase },
  { id: 'contracts', label: 'Contract Studio', icon: FileText },
  { id: 'litigation', label: 'Litigation Studio', icon: Gavel },
  { id: 'integration_hub', label: 'Integration Hub', icon: Link2 },
  { id: 'workflow_studio', label: 'Workflow Studio', icon: Workflow },
];

export const FloatingDock: React.FC = () => {
  const {
    activeView,
    setActiveView,
    toggleLeftPanel,
    toggleRightCopilot,
    leftPanelOpen,
    rightCopilotOpen,
    setCommandPaletteOpen,
  } = useWorkspaceStore();
  const { theme, toggleTheme } = useThemeStore();

  return (
    <div className="fixed bottom-6 left-1/2 -translate-x-1/2 z-50 pointer-events-none">
      <motion.div
        initial={{ y: 50, opacity: 0 }}
        animate={{ y: 0, opacity: 1 }}
        transition={{ type: 'spring', stiffness: 300, damping: 25 }}
        className="pointer-events-auto flex items-center gap-1.5 px-3 py-2 rounded-2xl glass-dock"
      >
        <button
          onClick={toggleLeftPanel}
          title={leftPanelOpen ? 'Collapse Tool Drawer' : 'Expand Tool Drawer'}
          className={cn(
            'p-2.5 rounded-xl transition-all duration-200 text-slate-400 hover:text-slate-100 hover:bg-white/10 dark:hover:bg-slate-800/60',
            leftPanelOpen && 'text-brand-400 bg-brand-500/10'
          )}
        >
          <PanelLeft className="w-4 h-4" />
        </button>

        <div className="w-[1px] h-6 bg-slate-300/20 dark:bg-slate-700/50 my-auto mx-1" />

        <div className="flex items-center gap-1">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = activeView === item.id;
            return (
              <button
                key={item.id}
                onClick={() => setActiveView(item.id)}
                className={cn(
                  'relative group flex items-center gap-2 px-3 py-1.5 rounded-xl text-xs font-medium transition-all duration-200',
                  isActive
                    ? 'bg-brand-600 text-white shadow-lg shadow-brand-600/30 font-semibold'
                    : 'text-slate-400 hover:text-slate-200 hover:bg-white/10 dark:hover:bg-slate-800/60'
                )}
              >
                <Icon className="w-3.5 h-3.5" />
                <span className="hidden xl:inline">{item.label}</span>

                {item.badge && !isActive && (
                  <span className="hidden lg:inline-block px-1.5 py-0.2 text-[9px] font-semibold bg-emerald-500/20 text-emerald-400 rounded-full border border-emerald-500/30">
                    {item.badge}
                  </span>
                )}

                <div className="absolute bottom-full mb-2 left-1/2 -translate-x-1/2 opacity-0 group-hover:opacity-100 pointer-events-none transition-opacity duration-150 px-2 py-1 text-[11px] font-medium bg-slate-900 text-white rounded-md whitespace-nowrap shadow-xl border border-slate-800">
                  {item.label}
                </div>
              </button>
            );
          })}
        </div>

        <div className="w-[1px] h-6 bg-slate-300/20 dark:bg-slate-700/50 my-auto mx-1" />

        <button
          onClick={() => setCommandPaletteOpen(true)}
          className="flex items-center gap-1.5 px-2.5 py-1.5 rounded-xl text-xs font-medium text-slate-400 hover:text-slate-100 hover:bg-white/10 dark:hover:bg-slate-800/60 transition-all"
        >
          <Command className="w-3.5 h-3.5 text-gold-400" />
          <kbd className="hidden lg:inline-block px-1.5 py-0.5 text-[10px] bg-slate-800/80 border border-slate-700 rounded text-slate-400 font-mono">
            ⌘K
          </kbd>
        </button>

        <button
          onClick={toggleTheme}
          title={`Switch to ${theme === 'dark' ? 'Light' : 'Dark'} Mode`}
          className="p-2.5 rounded-xl text-slate-400 hover:text-slate-100 hover:bg-white/10 dark:hover:bg-slate-800/60 transition-all"
        >
          {theme === 'dark' ? (
            <Sun className="w-4 h-4 text-amber-400" />
          ) : (
            <Moon className="w-4 h-4 text-slate-600" />
          )}
        </button>

        <button
          onClick={toggleRightCopilot}
          title={rightCopilotOpen ? 'Collapse Legal Copilot' : 'Expand Legal Copilot'}
          className={cn(
            'p-2.5 rounded-xl transition-all duration-200 text-slate-400 hover:text-slate-100 hover:bg-white/10 dark:hover:bg-slate-800/60',
            rightCopilotOpen && 'text-brand-400 bg-brand-500/10'
          )}
        >
          <div className="relative">
            <PanelRight className="w-4 h-4" />
            <Sparkles className="w-2.5 h-2.5 text-gold-400 absolute -top-1 -right-1" />
          </div>
        </button>
      </motion.div>
    </div>
  );
};

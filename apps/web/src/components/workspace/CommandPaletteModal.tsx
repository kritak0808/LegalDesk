'use client';

import React, { useEffect } from 'react';
import { Command } from 'cmdk';
import {
  Briefcase,
  FileText,
  ShieldCheck,
  Building2,
  Users,
  KeyRound,
  Search,
  Moon,
  Sun,
  X,
  Sparkles,
  Network,
  GitBranch,
  BrainCircuit,
  FileCheck,
  Gavel,
  ShieldAlert,
  Calendar,
  DollarSign,
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
  Share2,
  Activity,
  Shield,
  Gauge,
  Server,
  Database,
  Sliders,
} from 'lucide-react';
import { useWorkspaceStore, WorkspaceViewMode } from '@/store/useWorkspaceStore';
import { useThemeStore } from '@/store/useThemeStore';

export const CommandPaletteModal: React.FC = () => {
  const { commandPaletteOpen, setCommandPaletteOpen, setActiveView } = useWorkspaceStore();
  const { theme, toggleTheme } = useThemeStore();

  useEffect(() => {
    const down = (e: KeyboardEvent) => {
      if (e.key === 'k' && (e.metaKey || e.ctrlKey)) {
        e.preventDefault();
        setCommandPaletteOpen(!commandPaletteOpen);
      }
    };
    document.addEventListener('keydown', down);
    return () => document.removeEventListener('keydown', down);
  }, [commandPaletteOpen, setCommandPaletteOpen]);

  if (!commandPaletteOpen) return null;

  const navigateTo = (view: WorkspaceViewMode) => {
    setActiveView(view);
    setCommandPaletteOpen(false);
  };

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center p-4 bg-slate-950/70 backdrop-blur-md animate-fade-in">
      <div className="w-full max-w-2xl bg-slate-900 border border-slate-800 rounded-2xl shadow-2xl overflow-hidden text-slate-100 flex flex-col">
        <Command className="flex flex-col">
          <div className="flex items-center px-4 border-b border-slate-800 bg-slate-950/60">
            <Search className="w-4 h-4 text-brand-400 mr-2 shrink-0" />
            <Command.Input
              autoFocus
              placeholder="Search LegalDesk AI (v1.0.0-RC1): Executive HQ, Matters, CLM, Litigation, GRC, Research, Workflows, Integrations..."
              className="w-full h-12 bg-transparent text-sm text-slate-100 placeholder-slate-500 focus:outline-none"
            />
            <button
              onClick={() => setCommandPaletteOpen(false)}
              className="p-1 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 transition-all ml-2"
            >
              <X className="w-4 h-4" />
            </button>
          </div>

          <Command.List className="max-h-96 overflow-y-auto p-2 space-y-2 text-xs">
            <Command.Empty className="py-6 text-center text-slate-500">
              No matching LegalDesk AI platform items found.
            </Command.Empty>

            <Command.Group heading="Executive & Legal Operations Studio" className="text-[10px] font-semibold text-slate-500 uppercase tracking-wider px-2 py-1">
              <Command.Item
                onSelect={() => navigateTo('executive_command_center')}
                className="flex items-center gap-3 px-3 py-2 rounded-xl text-slate-300 hover:bg-brand-600 hover:text-white cursor-pointer transition-all"
              >
                <Crown className="w-4 h-4 text-gold-400" />
                <div className="flex flex-col">
                  <span className="font-semibold text-sm">Executive Command Center</span>
                  <span className="text-[10px] opacity-75">Enterprise Health Score (96.4%), Spend, Risk Index & Board Readiness</span>
                </div>
              </Command.Item>

              <Command.Item
                onSelect={() => navigateTo('matters')}
                className="flex items-center gap-3 px-3 py-2 rounded-xl text-slate-300 hover:bg-brand-600 hover:text-white cursor-pointer transition-all"
              >
                <Briefcase className="w-4 h-4 text-brand-400" />
                <div className="flex flex-col">
                  <span className="font-semibold text-sm">Enterprise Matter Studio</span>
                  <span className="text-[10px] opacity-75">Central legal operations hub & lifecycle state machine</span>
                </div>
              </Command.Item>

              <Command.Item
                onSelect={() => navigateTo('contracts')}
                className="flex items-center gap-3 px-3 py-2 rounded-xl text-slate-300 hover:bg-brand-600 hover:text-white cursor-pointer transition-all"
              >
                <FileText className="w-4 h-4 text-emerald-400" />
                <div className="flex flex-col">
                  <span className="font-semibold text-sm">Contract Lifecycle Management (CLM)</span>
                  <span className="text-[10px] opacity-75">Contract drafting, negotiations, approvals & obligations</span>
                </div>
              </Command.Item>

              <Command.Item
                onSelect={() => navigateTo('operations_center')}
                className="flex items-center gap-3 px-3 py-2 rounded-xl text-slate-300 hover:bg-brand-600 hover:text-white cursor-pointer transition-all"
              >
                <Activity className="w-4 h-4 text-indigo-400" />
                <div className="flex flex-col">
                  <span className="font-semibold text-sm">Enterprise Operations Center</span>
                  <span className="text-[10px] opacity-75">Platform availability (99.99%), P99 latency & component health matrix</span>
                </div>
              </Command.Item>
            </Command.Group>

            <Command.Group heading="Preferences & System" className="text-[10px] font-semibold text-slate-500 uppercase tracking-wider px-2 py-1">
              <Command.Item
                onSelect={() => {
                  toggleTheme();
                  setCommandPaletteOpen(false);
                }}
                className="flex items-center justify-between px-3 py-2 rounded-xl text-slate-300 hover:bg-brand-600 hover:text-white cursor-pointer transition-all"
              >
                <div className="flex items-center gap-2">
                  {theme === 'dark' ? (
                    <Sun className="w-4 h-4 text-amber-400" />
                  ) : (
                    <Moon className="w-4 h-4 text-indigo-400" />
                  )}
                  <span>Toggle UI Theme ({theme === 'dark' ? 'Switch to Light' : 'Switch to Dark'})</span>
                </div>
              </Command.Item>
            </Command.Group>
          </Command.List>

          <div className="p-2.5 border-t border-slate-800 bg-slate-950/80 text-[10px] text-slate-500 flex items-center justify-between px-4">
            <span>Navigation: <kbd className="bg-slate-800 px-1 rounded text-slate-300">↑↓</kbd> Select: <kbd className="bg-slate-800 px-1 rounded text-slate-300">↵</kbd></span>
            <span className="font-mono text-gold-400 font-bold">LegalDesk AI v1.0.0-RC1 (Production Certified)</span>
          </div>
        </Command>
      </div>
    </div>
  );
};

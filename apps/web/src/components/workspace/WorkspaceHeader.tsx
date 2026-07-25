'use client';

import React from 'react';
import {
  Scale,
  Search,
  Building2,
  ChevronRight,
  Sparkles,
  ShieldCheck,
  Bell,
  Cpu,
  UserCheck,
} from 'lucide-react';
import { useWorkspaceStore } from '@/store/useWorkspaceStore';

export const WorkspaceHeader: React.FC = () => {
  const { activeView, activeMatterId, setCommandPaletteOpen } = useWorkspaceStore();

  const viewLabels: Record<string, string> = {
    matters: 'Matter Operating Studio',
    contracts: 'AI Contract Intelligence',
    litigation: 'Litigation & Dispute Canvas',
    governance: 'Corporate Governance Platform',
    compliance: 'Regulatory Compliance Matrix',
  };

  return (
    <header className="h-14 border-b border-slate-200 dark:border-slate-800/80 bg-white/70 dark:bg-slate-900/70 backdrop-blur-md px-4 flex items-center justify-between z-30 sticky top-0">
      {/* Left: Organization & Breadcrumbs */}
      <div className="flex items-center gap-3">
        <div className="flex items-center gap-2 px-2.5 py-1.5 rounded-lg bg-gradient-to-r from-brand-900 to-slate-900 text-white shadow-sm border border-brand-700/30">
          <Scale className="w-4 h-4 text-gold-400" />
          <span className="font-bold text-xs tracking-wide">LegalDesk AI</span>
          <span className="text-[9px] uppercase px-1.5 py-0.2 rounded bg-brand-500/20 text-brand-300 font-mono">
            ENT
          </span>
        </div>

        <ChevronRight className="w-3.5 h-3.5 text-slate-400 dark:text-slate-600" />

        <div className="flex items-center gap-1.5 text-xs text-slate-600 dark:text-slate-300">
          <Building2 className="w-3.5 h-3.5 text-slate-400" />
          <span className="font-medium text-slate-900 dark:text-slate-100">Acme Global Corp</span>
          <ChevronRight className="w-3.5 h-3.5 text-slate-400 dark:text-slate-600" />
          <span className="text-brand-600 dark:text-brand-400 font-semibold">
            {viewLabels[activeView]}
          </span>
          {activeMatterId && (
            <>
              <span className="text-slate-400 dark:text-slate-600">/</span>
              <span className="font-mono text-[11px] bg-slate-100 dark:bg-slate-800 px-1.5 py-0.5 rounded text-slate-500 dark:text-slate-400">
                {activeMatterId}
              </span>
            </>
          )}
        </div>
      </div>

      {/* Middle: Quick Search / Command Bar Trigger */}
      <div className="hidden md:flex items-center flex-1 max-w-md mx-6">
        <button
          onClick={() => setCommandPaletteOpen(true)}
          className="w-full flex items-center justify-between px-3 py-1.5 rounded-xl bg-slate-100 dark:bg-slate-800/60 border border-slate-200 dark:border-slate-700/60 text-slate-400 text-xs hover:border-brand-500/40 hover:bg-slate-200/50 dark:hover:bg-slate-800 transition-all"
        >
          <div className="flex items-center gap-2">
            <Search className="w-3.5 h-3.5 text-slate-400" />
            <span>Search matters, contracts, compliance rules...</span>
          </div>
          <kbd className="px-1.5 py-0.5 text-[10px] bg-white dark:bg-slate-900 border border-slate-200 dark:border-slate-700 rounded text-slate-400 font-mono shadow-xs">
            ⌘K
          </kbd>
        </button>
      </div>

      {/* Right: System Status & User Profile */}
      <div className="flex items-center gap-3">
        {/* System Health Pulse */}
        <div className="hidden lg:flex items-center gap-2 px-2.5 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/20 text-emerald-400 text-[11px] font-medium">
          <span className="w-2 h-2 rounded-full bg-emerald-400 animate-pulse" />
          <span>System Healthy</span>
        </div>

        {/* Notifications */}
        <button className="p-2 rounded-lg text-slate-500 hover:text-slate-800 dark:text-slate-400 dark:hover:text-slate-100 hover:bg-slate-100 dark:hover:bg-slate-800 transition-all relative">
          <Bell className="w-4 h-4" />
          <span className="absolute top-1.5 right-1.5 w-1.5 h-1.5 rounded-full bg-brand-500" />
        </button>

        <div className="w-[1px] h-4 bg-slate-200 dark:bg-slate-800" />

        {/* User Account */}
        <div className="flex items-center gap-2 pl-1 cursor-pointer group">
          <div className="w-7 h-7 rounded-full bg-gradient-to-tr from-brand-600 to-indigo-600 text-white flex items-center justify-center text-xs font-bold ring-2 ring-brand-500/20 group-hover:ring-brand-500/50 transition-all">
            JD
          </div>
          <div className="hidden xl:block text-left">
            <div className="text-xs font-semibold leading-tight text-slate-800 dark:text-slate-200">
              Jonathan Vance, Esq.
            </div>
            <div className="text-[10px] text-slate-400 leading-tight">General Counsel</div>
          </div>
        </div>
      </div>
    </header>
  );
};

'use client';

import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Folder,
  FolderOpen,
  FileText,
  Filter,
  AlertTriangle,
  Clock,
  CheckCircle2,
  ChevronDown,
  ChevronRight,
  Plus,
  Search,
  SlidersHorizontal,
} from 'lucide-react';
import { useWorkspaceStore } from '@/store/useWorkspaceStore';
import { cn } from '@/lib/utils';

interface MatterFolder {
  id: string;
  name: string;
  count: number;
  items: { id: string; name: string; status: 'active' | 'review' | 'archived'; risk: 'low' | 'medium' | 'high' }[];
}

const mockFolders: MatterFolder[] = [
  {
    id: 'f1',
    name: 'Corporate Restructuring 2026',
    count: 14,
    items: [
      { id: 'MAT-2026-089', name: 'Acme / Mergers & Acquisitions NDA', status: 'active', risk: 'low' },
      { id: 'MAT-2026-092', name: 'Cross-Border Share Purchase Agreement', status: 'review', risk: 'high' },
    ],
  },
  {
    id: 'f2',
    name: 'IP & Patent Disputes',
    count: 8,
    items: [
      { id: 'MAT-2026-104', name: 'SaaS Algorithm Patent Claims', status: 'active', risk: 'medium' },
      { id: 'MAT-2026-118', name: 'Trademark Opposition Briefing', status: 'review', risk: 'low' },
    ],
  },
  {
    id: 'f3',
    name: 'Regulatory & Data Privacy',
    count: 22,
    items: [
      { id: 'MAT-2026-201', name: 'EU AI Act Article 10 Audit', status: 'active', risk: 'high' },
      { id: 'MAT-2026-215', name: 'GDPR Cross-Border Transfer Assessment', status: 'active', risk: 'medium' },
    ],
  },
];

export const DockablePanels: React.FC = () => {
  const { leftPanelOpen, activeMatterId, setActiveMatter } = useWorkspaceStore();
  const [openFolders, setOpenFolders] = useState<Record<string, boolean>>({ f1: true, f2: true });
  const [filterRisk, setFilterRisk] = useState<string | null>(null);

  const toggleFolder = (id: string) => {
    setOpenFolders((prev) => ({ ...prev, [id]: !prev[id] }));
  };

  return (
    <AnimatePresence>
      {leftPanelOpen && (
        <motion.aside
          initial={{ x: -300, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          exit={{ x: -300, opacity: 0 }}
          transition={{ type: 'spring', stiffness: 300, damping: 30 }}
          className="w-72 border-r border-slate-200 dark:border-slate-800/80 bg-slate-50/50 dark:bg-slate-900/50 backdrop-blur-md flex flex-col h-[calc(100vh-3.5rem)] z-20 shrink-0"
        >
          {/* Panel Header */}
          <div className="p-3 border-b border-slate-200 dark:border-slate-800/80 flex items-center justify-between">
            <div className="flex items-center gap-2">
              <SlidersHorizontal className="w-4 h-4 text-brand-500" />
              <span className="text-xs font-semibold uppercase tracking-wider text-slate-500 dark:text-slate-400">
                Matter Workspace Navigator
              </span>
            </div>
            <button
              title="New Matter"
              className="p-1 rounded-md text-slate-400 hover:text-slate-100 hover:bg-brand-600 transition-all"
            >
              <Plus className="w-3.5 h-3.5" />
            </button>
          </div>

          {/* Quick Risk Filters */}
          <div className="p-3 border-b border-slate-200 dark:border-slate-800/60">
            <div className="text-[11px] font-medium text-slate-400 mb-2">Filter by Risk Index</div>
            <div className="flex items-center gap-1.5">
              <button
                onClick={() => setFilterRisk(filterRisk === 'all' ? null : 'all')}
                className={cn(
                  'px-2 py-1 rounded-lg text-[11px] font-medium transition-all',
                  filterRisk === null || filterRisk === 'all'
                    ? 'bg-slate-200 dark:bg-slate-800 text-slate-900 dark:text-slate-100 font-semibold'
                    : 'text-slate-400 hover:bg-slate-100 dark:hover:bg-slate-800/50'
                )}
              >
                All
              </button>
              <button
                onClick={() => setFilterRisk(filterRisk === 'high' ? null : 'high')}
                className={cn(
                  'px-2 py-1 rounded-lg text-[11px] font-medium flex items-center gap-1 transition-all',
                  filterRisk === 'high'
                    ? 'bg-rose-500/20 text-rose-400 border border-rose-500/30'
                    : 'text-slate-400 hover:text-rose-400'
                )}
              >
                <AlertTriangle className="w-3 h-3 text-rose-400" />
                High Risk
              </button>
              <button
                onClick={() => setFilterRisk(filterRisk === 'medium' ? null : 'medium')}
                className={cn(
                  'px-2 py-1 rounded-lg text-[11px] font-medium flex items-center gap-1 transition-all',
                  filterRisk === 'medium'
                    ? 'bg-amber-500/20 text-amber-400 border border-amber-500/30'
                    : 'text-slate-400 hover:text-amber-400'
                )}
              >
                <Clock className="w-3 h-3 text-amber-400" />
                Medium
              </button>
            </div>
          </div>

          {/* Folder & Matter Tree */}
          <div className="flex-1 overflow-y-auto p-3 space-y-3">
            {mockFolders.map((folder) => {
              const isOpen = openFolders[folder.id];
              return (
                <div key={folder.id} className="space-y-1">
                  {/* Folder Header */}
                  <button
                    onClick={() => toggleFolder(folder.id)}
                    className="w-full flex items-center justify-between p-1.5 rounded-lg text-xs font-medium text-slate-700 dark:text-slate-300 hover:bg-slate-200/50 dark:hover:bg-slate-800/50 transition-all"
                  >
                    <div className="flex items-center gap-2">
                      {isOpen ? (
                        <ChevronDown className="w-3.5 h-3.5 text-slate-400" />
                      ) : (
                        <ChevronRight className="w-3.5 h-3.5 text-slate-400" />
                      )}
                      {isOpen ? (
                        <FolderOpen className="w-4 h-4 text-brand-400" />
                      ) : (
                        <Folder className="w-4 h-4 text-slate-400" />
                      )}
                      <span className="truncate max-w-[150px]">{folder.name}</span>
                    </div>
                    <span className="text-[10px] px-1.5 py-0.5 rounded bg-slate-200 dark:bg-slate-800 text-slate-500 dark:text-slate-400 font-mono">
                      {folder.count}
                    </span>
                  </button>

                  {/* Folder Items */}
                  {isOpen && (
                    <div className="ml-4 pl-2 border-l border-slate-200 dark:border-slate-800 space-y-1">
                      {folder.items
                        .filter((item) => !filterRisk || filterRisk === 'all' || item.risk === filterRisk)
                        .map((item) => {
                          const isSelected = activeMatterId === item.id;
                          return (
                            <button
                              key={item.id}
                              onClick={() => setActiveMatter(item.id)}
                              className={cn(
                                'w-full text-left p-2 rounded-lg text-xs transition-all duration-150 flex flex-col gap-1',
                                isSelected
                                  ? 'bg-brand-600/10 text-brand-500 font-semibold border-l-2 border-brand-500 pl-2.5'
                                  : 'text-slate-600 dark:text-slate-400 hover:bg-slate-200/40 dark:hover:bg-slate-800/40 hover:text-slate-900 dark:hover:text-slate-200'
                              )}
                            >
                              <div className="flex items-center justify-between">
                                <span className="font-mono text-[10px] opacity-75">{item.id}</span>
                                <span
                                  className={cn(
                                    'w-1.5 h-1.5 rounded-full',
                                    item.risk === 'high'
                                      ? 'bg-rose-500'
                                      : item.risk === 'medium'
                                      ? 'bg-amber-500'
                                      : 'bg-emerald-500'
                                  )}
                                />
                              </div>
                              <span className="truncate leading-tight">{item.name}</span>
                            </button>
                          );
                        })}
                    </div>
                  )}
                </div>
              );
            })}
          </div>

          {/* Panel Footer */}
          <div className="p-3 border-t border-slate-200 dark:border-slate-800/80 text-[11px] text-slate-400 flex items-center justify-between">
            <span className="flex items-center gap-1.5">
              <CheckCircle2 className="w-3.5 h-3.5 text-emerald-400" />
              All Vault Syncs Active
            </span>
            <span className="font-mono text-[10px]">v1.0.0</span>
          </div>
        </motion.aside>
      )}
    </AnimatePresence>
  );
};

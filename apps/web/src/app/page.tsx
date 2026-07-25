'use client';

import React from 'react';
import { WorkspaceHeader } from '@/components/workspace/WorkspaceHeader';
import { DockablePanels } from '@/components/workspace/DockablePanels';
import { WorkspaceCanvas } from '@/components/workspace/WorkspaceCanvas';
import { RightCopilotPanel } from '@/components/workspace/RightCopilotPanel';
import { FloatingDock } from '@/components/workspace/FloatingDock';
import { CommandPaletteModal } from '@/components/workspace/CommandPaletteModal';

export default function WorkspacePage() {
  return (
    <div className="flex flex-col h-screen w-screen overflow-hidden bg-background text-foreground select-none">
      {/* Top Navigation Header */}
      <WorkspaceHeader />

      {/* Main Workspace Workspace Shell */}
      <div className="flex flex-1 overflow-hidden relative">
        {/* Left Tool Drawer */}
        <DockablePanels />

        {/* Central Immersive Working Canvas */}
        <WorkspaceCanvas />

        {/* Adaptive Right-Side AI Assistant Drawer */}
        <RightCopilotPanel />
      </div>

      {/* Floating Bottom Navigation Dock */}
      <FloatingDock />

      {/* Global Cmd+K Command Palette Modal */}
      <CommandPaletteModal />
    </div>
  );
}

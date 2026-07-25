'use client';

import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
  Sparkles,
  Send,
  Bot,
  User,
  Paperclip,
  Bookmark,
  ExternalLink,
  RotateCcw,
  Zap,
  ShieldCheck,
  FileCheck,
  X,
} from 'lucide-react';
import { useWorkspaceStore } from '@/store/useWorkspaceStore';
import { useCopilotStore } from '@/store/useCopilotStore';
import { cn } from '@/lib/utils';

export const RightCopilotPanel: React.FC = () => {
  const { rightCopilotOpen, toggleRightCopilot } = useWorkspaceStore();
  const { messages, addMessage, clearMessages, activeContext } = useCopilotStore();
  const [input, setInput] = useState('');
  const [isTyping, setIsTyping] = useState(false);

  const handleSend = () => {
    if (!input.trim()) return;
    const userText = input;
    setInput('');
    addMessage({ sender: 'user', content: userText });

    setIsTyping(true);
    setTimeout(() => {
      setIsTyping(false);
      addMessage({
        sender: 'assistant',
        content: `I analyzed **${userText}** in relation to your active matter. According to standard enterprise risk protocols and clause indexes: \n\n1. **Indemnification Exposure**: Uncapped liability risk detected in Section 14.2.\n2. **Governing Law**: Delaware jurisdiction applies.\n3. **Recommendation**: Insert mutual limitation of liability capped at 2x 12-month trailing fees.`,
        citations: [
          { title: 'Standard Liability Playbook 2026', ref: 'Section 4.1' },
          { title: 'Delaware Chancery Precedents', ref: 'In re Trados Tech' },
        ],
      });
    }, 1200);
  };

  const handleQuickPrompt = (prompt: string) => {
    setInput(prompt);
  };

  return (
    <AnimatePresence>
      {rightCopilotOpen && (
        <motion.aside
          initial={{ x: 340, opacity: 0 }}
          animate={{ x: 0, opacity: 1 }}
          exit={{ x: 340, opacity: 0 }}
          transition={{ type: 'spring', stiffness: 300, damping: 30 }}
          className="w-80 border-l border-slate-200 dark:border-slate-800/80 bg-slate-900/90 text-slate-100 backdrop-blur-xl flex flex-col h-[calc(100vh-3.5rem)] z-20 shrink-0 shadow-2xl"
        >
          {/* Header */}
          <div className="p-3 border-b border-slate-800 flex items-center justify-between bg-slate-950/50">
            <div className="flex items-center gap-2">
              <div className="p-1.5 rounded-lg bg-gradient-to-tr from-brand-600 to-indigo-600 shadow-md">
                <Sparkles className="w-4 h-4 text-gold-300 animate-pulse" />
              </div>
              <div>
                <div className="text-xs font-bold text-slate-100 flex items-center gap-1.5">
                  LegalDesk AI Copilot
                  <span className="text-[9px] px-1.5 py-0.2 rounded-full bg-gold-500/20 text-gold-400 font-mono font-semibold border border-gold-500/30">
                    PRO
                  </span>
                </div>
                <div className="text-[10px] text-slate-400 flex items-center gap-1">
                  <ShieldCheck className="w-3 h-3 text-emerald-400" />
                  Enterprise Encryption Active
                </div>
              </div>
            </div>
            <div className="flex items-center gap-1">
              <button
                onClick={clearMessages}
                title="Clear Chat History"
                className="p-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 transition-all"
              >
                <RotateCcw className="w-3.5 h-3.5" />
              </button>
              <button
                onClick={toggleRightCopilot}
                className="p-1.5 rounded-lg text-slate-400 hover:text-slate-200 hover:bg-slate-800 transition-all"
              >
                <X className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Active Context Banner */}
          <div className="px-3 py-2 bg-brand-950/40 border-b border-brand-900/40 flex items-center justify-between text-[11px]">
            <span className="text-slate-400 flex items-center gap-1.5">
              <FileCheck className="w-3.5 h-3.5 text-brand-400" />
              Context:
            </span>
            <span className="font-mono text-[10px] text-brand-300 font-semibold truncate max-w-[170px]">
              {activeContext}
            </span>
          </div>

          {/* Quick Action Chips */}
          <div className="p-2 border-b border-slate-800/80 flex items-center gap-1.5 overflow-x-auto no-scrollbar">
            {[
              'Risk Audit',
              'Counter Clause',
              'EU AI Act Check',
              'Executive Brief',
            ].map((chip) => (
              <button
                key={chip}
                onClick={() => handleQuickPrompt(`Perform ${chip} on active contract`)}
                className="px-2.5 py-1 rounded-full text-[10px] font-medium bg-slate-800 hover:bg-brand-600/30 hover:text-brand-300 text-slate-300 border border-slate-700/60 whitespace-nowrap transition-all flex items-center gap-1"
              >
                <Zap className="w-2.5 h-2.5 text-gold-400" />
                {chip}
              </button>
            ))}
          </div>

          {/* Message Stream */}
          <div className="flex-1 overflow-y-auto p-3 space-y-3.5 text-xs">
            {messages.map((msg) => (
              <div
                key={msg.id}
                className={cn(
                  'flex flex-col gap-1.5 max-w-[92%]',
                  msg.sender === 'user' ? 'ml-auto items-end' : 'mr-auto items-start'
                )}
              >
                <div className="flex items-center gap-1.5 text-[10px] text-slate-400">
                  {msg.sender === 'user' ? (
                    <>
                      <span>{msg.timestamp}</span>
                      <User className="w-3 h-3 text-brand-400" />
                    </>
                  ) : (
                    <>
                      <Bot className="w-3 h-3 text-gold-400" />
                      <span className="font-semibold text-slate-300">Legal AI Agent</span>
                      <span>• {msg.timestamp}</span>
                    </>
                  )}
                </div>

                <div
                  className={cn(
                    'p-3 rounded-2xl text-xs leading-relaxed shadow-sm',
                    msg.sender === 'user'
                      ? 'bg-brand-600 text-white rounded-tr-none'
                      : 'bg-slate-800/90 text-slate-200 border border-slate-700/60 rounded-tl-none'
                  )}
                >
                  <p className="whitespace-pre-line">{msg.content}</p>

                  {msg.citations && msg.citations.length > 0 && (
                    <div className="mt-2.5 pt-2 border-t border-slate-700/50 space-y-1">
                      <div className="text-[10px] font-bold text-gold-400 uppercase tracking-wider">
                        Indexed Citations
                      </div>
                      {msg.citations.map((cit, idx) => (
                        <div
                          key={idx}
                          className="flex items-center justify-between text-[10px] text-slate-300 bg-slate-900/60 p-1.5 rounded border border-slate-700/40"
                        >
                          <span className="truncate font-medium">{cit.title}</span>
                          <span className="font-mono text-[9px] text-brand-400 flex items-center gap-0.5">
                            {cit.ref}
                            <ExternalLink className="w-2.5 h-2.5" />
                          </span>
                        </div>
                      ))}
                    </div>
                  )}
                </div>
              </div>
            ))}

            {isTyping && (
              <div className="flex items-center gap-2 text-slate-400 text-xs italic p-2">
                <Bot className="w-4 h-4 text-gold-400 animate-spin" />
                <span>Legal AI analyzing precedents and clauses...</span>
              </div>
            )}
          </div>

          {/* Interactive Prompt Input Box */}
          <div className="p-3 border-t border-slate-800 bg-slate-950/80">
            <div className="relative flex items-center">
              <textarea
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyDown={(e) => {
                  if (e.key === 'Enter' && !e.shiftKey) {
                    e.preventDefault();
                    handleSend();
                  }
                }}
                placeholder="Ask Legal AI to review clauses, draft briefs, analyze risk..."
                rows={2}
                className="w-full bg-slate-900 border border-slate-700/70 rounded-xl p-2.5 pr-10 text-xs text-slate-100 placeholder-slate-500 focus:outline-none focus:border-brand-500 transition-all resize-none"
              />
              <button
                onClick={handleSend}
                disabled={!input.trim()}
                className="absolute right-2 bottom-2.5 p-2 rounded-lg bg-brand-600 hover:bg-brand-500 disabled:opacity-40 text-white transition-all shadow-md"
              >
                <Send className="w-3.5 h-3.5" />
              </button>
            </div>
            <div className="mt-1.5 flex items-center justify-between text-[10px] text-slate-500">
              <span>Shift+Enter for newline</span>
              <span className="font-mono">RAG Mode: Full Vault</span>
            </div>
          </div>
        </motion.aside>
      )}
    </AnimatePresence>
  );
};

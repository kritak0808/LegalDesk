import { create } from 'zustand';

export interface CopilotMessage {
  id: string;
  sender: 'user' | 'assistant' | 'system';
  content: string;
  timestamp: string;
  citations?: { title: string; ref: string }[];
  isStreaming?: boolean;
}

interface CopilotState {
  messages: CopilotMessage[];
  isStreaming: boolean;
  activeContext: string;
  addMessage: (message: Omit<CopilotMessage, 'id' | 'timestamp'>) => void;
  clearMessages: () => void;
  setActiveContext: (context: string) => void;
}

export const useCopilotStore = create<CopilotState>((set) => ({
  messages: [
    {
      id: '1',
      sender: 'assistant',
      content: 'Welcome to **LegalDesk AI Copilot**. I have indexed active matters, contract repositories, regulatory filings, and compliance rules for **Acme Enterprise Corp**. How can I assist your legal team today?',
      timestamp: '21:54',
      citations: [
        { title: 'Master Services Agreement v4.2', ref: 'Clause 14.3 - Indemnification' },
        { title: 'EU AI Act Compliance Checklist', ref: 'Article 10 Data Governance' },
      ],
    },
  ],
  isStreaming: false,
  activeContext: 'Global Workspace Context',

  addMessage: (msg) =>
    set((state) => ({
      messages: [
        ...state.messages,
        {
          ...msg,
          id: Math.random().toString(36).substring(7),
          timestamp: new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }),
        },
      ],
    })),

  clearMessages: () => set({ messages: [] }),
  setActiveContext: (context) => set({ activeContext: context }),
}));
